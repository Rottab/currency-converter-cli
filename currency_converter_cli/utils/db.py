from pony import orm
from currency_converter_cli.models.dates import create_dates
from currency_converter_cli.models.rates import create_rates


db = orm.Database()

Dates = create_dates(db, orm)
Rates = create_rates(db, orm, Dates)

db.bind(provider='sqlite', filename='../data/db.sqlite3', create_db=True)
db.generate_mapping(create_tables=True)
