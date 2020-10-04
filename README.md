# currency-converter-cli
A cli program that converts between currencies. All the rates are pulled from the [frankfurter](https://www.frankfurter.app/) public api.
## Requirements
Python 3.6+
## Installation
> pip install -e git+git://github.com/Rottab/currency-converter-cli#egg=currency_converter_cli
## Run it
Run the tool using:
> currency-converter [options]

or

> cc [options]
## Example
> currency-converter --to usd

> cc --base usd --to eur

> cc --base usd --to eur --amount 5.5 --pretty true

> cc --base usd --to eur --amount 10 --date 2014-01-01
## Options
*  -h, --help      show this help message and exit
*  -b , --base     Base currency
*  -t , --to       Currency to convert to
*  -a , --amount   Base currency amount
*  -d , --date     Date of convertion rate in yyyy-mm-dd format
*  -p , --pretty   Print result in pretty descriptive format
## Issues
* frankfurter api doesn't seem to daily rates properly on time
## Todo
- [ ] Complete unit test
- [ ] Add list option to list available currencies
- [ ] Improve pretty print option
- [ ] Utilize the time series request

