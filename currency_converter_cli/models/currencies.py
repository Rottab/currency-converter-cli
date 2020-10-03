# Unused for now
def create_currencies(db, orm):
    class Currencies(db.Entity):
        code = orm.Required(str)
        name = orm.Required(str)
    return Currencies
