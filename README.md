# currency-converter-cli
A cli program that converts between currencies. All the rates are pulled from the [frankfurter](https://www.frankfurter.app/) public api.
# Requirements
Python 3.6+
## Installation
> install pip install -e git+git://github.com/Rottab/currency-converter-cli#egg=currency_converter_cli
## Run it
Run the tool using:
> currency-converter [options]
or
> cc [options]
## Example
> cc --base usd --to eur --amount 10 --date 2014-01-01
## Options
>  -h, --help      show this help message and exit
>  -b , --base     Base currency
>  -t , --to       Currency to convert to
>  -a , --amount   Base currency amount
>  -d , --date     Date of convertion rate in yyyy-mm-dd format
>  -p , --pretty   Print result in pretty descriptive format
