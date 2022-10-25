import sqlite3


def create_connection(db_path):
    try:
        con = sqlite3.connect(db_path)
    except Exception as e:
        print("Exception:", e)
        con = None
    return con


def main():
    database = "data.db"
    con = create_connection(database)
    with con:
        pass


if __name__ == "__main__":
    main()
