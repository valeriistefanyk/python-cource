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
       jog VARCHAR(128),
       age INTEGER
    )
    '''
    con.execute(sql)


def main():
    database = "data.db"
    con = create_connection(database)
    with con:
        create_table(con)


if __name__ == "__main__":
    main()
