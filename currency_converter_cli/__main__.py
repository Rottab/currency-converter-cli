import argparse
import sys
from datetime import date

from .utils.crud import get_remote_rates_and_store, get_local_rates


def main(argv=None):
    parser = argparse.ArgumentParser(
        description='Simple currency converter cli tool based on frankfurter api')
    parser.add_argument(
        '-b', '--base', help='Base currency', metavar='', type=str, default='EUR')
    parser.add_argument(
        '-t', '--to', help='Currency to convert to', metavar='', type=str, required=True)
    parser.add_argument(
        '-a', '--amount', help='Base currency amount', metavar='', type=float, default=1)
    parser.add_argument(
        '-d', '--date', help='Date of convertion rate in yyyy-mm-dd format', metavar='',
        type=date.fromisoformat, default=None)
    parser.add_argument(
        '-p', '--pretty', help='Print result in pretty descriptive format', metavar='',
        type=bool, default=False)

    args = parser.parse_args(argv)
    return convert(
        amount=args.amount,
        currency_from=args.base.upper(),
        currency_to=args.to.upper(),
        selected_date=args.date,
        pretty=args.pretty
    )


def calculate_rate(x, y, amount):
    return round(((1/x) * y) * amount, 3)


def pretty_print(currency_from, currency_to, amount, calculated_amount, selected_date, pretty):
    if not pretty:
        return print(calculated_amount)
    if selected_date >= date.today():
        selected_date = 'latest'
    print(f'{amount} {currency_from} is equal to {calculated_amount} {currency_to} based on {selected_date} rates.')


def convert(currency_to, currency_from=None, amount=1, selected_date=None, pretty=False):
    # Validate parameters
    if selected_date:
        if selected_date > date.today():
            sys.exit(f'Invalid date argument: date entered {selected_date} current date {date.today()}')
        elif selected_date < date(year=1999, month=1, day=4):
            sys.exit(f'Invalid date argument: date entered {selected_date} available rates begin from {date(year=1999, month=1, day=4)}')
    # Check if entry exits in database
    rates = get_local_rates(currency_from, currency_to, selected_date)
    # If not. Then request from the api and save it locally
    if not rates:
        rates = get_remote_rates_and_store(
            currency_from, currency_to, selected_date)
    # Exchange based on the rates
    calculated_amount = calculate_rate(
        rates['rate_from'], rates['rate_to'], amount)
    # Print and return
    return pretty_print(
        currency_from=currency_from,
        currency_to=currency_to,
        amount=amount,
        calculated_amount=calculated_amount,
        selected_date=selected_date or date.today(),
        pretty=pretty
    )


if __name__ == '__main__':
    main()
