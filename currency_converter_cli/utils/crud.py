import requests
from datetime import date, timedelta
from pony.orm import db_session, select, desc
from currency_converter_cli.utils.db import Dates, Rates


@db_session
def get_local_rates(currency_from, currency_to, selected_date):
    date_result = None
    if selected_date:
        query_result = Dates.get(date=selected_date)
        if query_result:
            date_result = query_result.to_dict()
    else:
        # Finds the latest entry by date in the database
        query_result = Dates.select().order_by(desc(Dates.date)).first()
        if query_result:
            date_result = query_result.to_dict()
    if not date_result:
        return False
    # Return nothing if the top most entry is outdated
    if date_result['date'] < (date.today() - timedelta(days=1)) and not selected_date:
        return False
    # Get 'from' rate based on the latest date
    rate_from = None
    if currency_from in [None, 'EUR']:
        rate_from = 1
    else:
        rate_result = Rates.get(code=currency_from, date=date_result['id'])
        if rate_result:
            rate_from = rate_result.to_dict()['rate']
    # Get 'to' rate based on latest date
    rate_to = None
    if currency_to in [None, 'EUR']:
        rate_to = 1
    else:
        rate_result = Rates.get(code=currency_to, date=date_result['id'])
        if rate_result:
            rate_to = rate_result.to_dict()['rate']
        else:
            raise Exception('CODE IS INCORRECT YOU PIECE OF SHIT')

    return {
        'rate_from': rate_from,
        'rate_to': rate_to,
    }


def _rates_from_json(currency_from, currency_to, json):
    return {
        'rate_from': json['rates'][currency_from] if currency_from not in [None, 'EUR'] else 1,
        'rate_to': json['rates'][currency_to] if currency_to not in [None, 'EUR'] else 1,
    }


@db_session
def get_remote_rates_and_store(currency_from, currency_to, selected_date=None):
    if selected_date:
        json = requests.get(
            f'https://api.frankfurter.app/{selected_date}').json()
    else:
        json = requests.get('https://api.frankfurter.app/latest').json()

    # If entry already in database for some reason
    query_result = Dates.get(date=selected_date)
    if query_result:
        return _rates_from_json(currency_from, currency_to, json)

    # Save into database
    date_obj = Dates(base=json['base'], date=json['date'])
    for code, rate in json['rates'].items():
        Rates(date=date_obj, code=code, rate=rate)

    return _rates_from_json(currency_from, currency_to, json)
