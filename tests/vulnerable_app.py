password = "hunter2"
def get_user(db, name):
    db.execute(f"SELECT * FROM users WHERE name = '{name}'")
def calc(x):
    return eval(x)
