import sqlite3


def create_connection(db_path):
    try:
        con = sqlite3.connect(db_path)
    except Exception as e:
        print("Exception:", e)
        con = None
    return con


def create_table(con):
    sql = ''' CREATE TABLE IF NOT EXISTS person(
       person_id INTEGER NOT NULL PRIMARY KEY,
       first_name VARCHAR(128) NOT NULL,
       last_name VARCHAR(128) NOT NULL,
       address VARCHAR(1024),
       job VARCHAR(128),
       age INTEGER
    )
    '''
    con.execute(sql)


def print_table(con):
    sql = ''' SELECT * FROM person;'''
    cur = con.cursor()
    persons = cur.execute(sql)
    for p in persons:
        print(p)


def main():
    database = "data.db"
    with create_connection(database) as con:
        create_table(con)
        print_table(con)


if __name__ == "__main__":
    main()
