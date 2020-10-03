from datetime import date


def create_dates(db, orm):
    class Dates(db.Entity):
        date = orm.Required(date)
        base = orm.Required(str)
        rates = orm.Set('Rates')
    return Dates
