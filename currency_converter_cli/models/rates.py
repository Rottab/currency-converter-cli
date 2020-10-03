def create_rates(db, orm, Dates):
    class Rates(db.Entity):
        code = orm.Required(str)
        rate = orm.Required(float)
        date = orm.Required(Dates)
    return Rates
