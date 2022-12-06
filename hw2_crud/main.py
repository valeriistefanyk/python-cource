import sqlite3
from faker import Faker


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


def create_persons(con, entries=10):
    fake = Faker()
    records = []
    for _ in range(entries):
        address = fake.address()
        last_name = fake.last_name()
        first_name = fake.first_name()
        job = fake.job()
        age = fake.random_int(14, 100)
        records.append((first_name, last_name, address, job, age))

    sql = ''' INSERT INTO person(first_name, last_name, address, job, age) 
            VALUES (?,?,?,?,?); '''
    cur = con.cursor()
    cur.executemany(sql, records)
    con.commit()


def update_person(con, person_id):
    fake = Faker()
    first_name = fake.first_name()
    last_name = fake.last_name()
    address = fake.address()
    job = fake.job()
    age = fake.random_int(14, 100)
    person = (first_name, last_name, address, job, age, person_id)
    sql = ''' UPDATE person 
            SET first_name = ?,
                last_name = ?,
                address = ?,
                job = ?,
                age = ? 
            WHERE person_id = ?'''
    cur = con.cursor()
    cur.execute(sql, person)
    con.commit()


def delete_person(con, person_id):
    sql = ''' DELETE FROM person WHERE person_id = ? '''
    cur = con.cursor()
    cur.execute(sql, (person_id,))
    con.commit()


def print_table(con):
    sql = ''' SELECT * FROM person;'''
    cur = con.cursor()
    persons = cur.execute(sql)
    for p in persons:
        print(p)


def print_person(con, person_id):
    sql = ''' SELECT * FROM person WHERE person_id = ? '''
    cur = con.cursor()
    cur.execute(sql, (person_id,))
    print(cur.fetchone())


def main():
    database = "data.db"
    with create_connection(database) as con:
        create_table(con)
        create_persons(con, entries=15)
        delete_person(con, 7)
        print_table(con)

        print("-" * 20)

        print_person(con, 1)
        update_person(con, 1)
        print_person(con, 1)


if __name__ == "__main__":
    main()
