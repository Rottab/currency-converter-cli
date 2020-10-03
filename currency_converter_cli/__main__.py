import argparse
from datetime import date

from currency_converter_cli.utils.crud import get_remote_rates_and_store, get_local_rates


def main(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', help='Base currency', type=str, default='EUR')
    parser.add_argument('-t', help='Currency to convert to', type=str)
    parser.add_argument('-a', help='Base currency amount', type=int, default=1)
    parser.add_argument('-d', help='Date of convertion rate in yyyy-mm-dd format',
                        type=date.fromisoformat, default=None)
    args = parser.parse_args(argv)
    return convert(
        amount=args.a,
        currency_from=args.f,
        currency_to=args.t,
        selected_date=args.d,
    )


def calculate_rate(x, y, amount):
    return round(((1/x) * y) * amount, 3)


def pretty_print(currency_from, currency_to, amount, calculated_amount, selected_date):
    print(f'{amount} {currency_from} is equal to {calculated_amount} {currency_to} based on {selected_date} rates.')


def convert(currency_to, currency_from=None, amount=1, selected_date=None):
    # Validate parameters

    # Check if exits in database
    rates = get_local_rates(currency_from, currency_to, selected_date)
    # If not. Then request from the api and save it locally
    if not rates:
        rates = get_remote_rates_and_store(
            currency_from, currency_to, selected_date)
    #
    if not rates:
        print('Something messed up')
        return 1
    calculated_amount = calculate_rate(
        rates['rate_from'], rates['rate_to'], amount)
    # Print and return
    return pretty_print(
        currency_from=currency_from,
        currency_to=currency_to,
        amount=amount,
        calculated_amount=calculated_amount,
        selected_date=selected_date or 'latest'
    )


if __name__ == '__main__':
    main()
