import sqlite3

DATABASE = '../CRM.db'

def get_count_account():
    connection = sqlite3.connect(DATABASE)
    cursor = connection.cursor()

    # https://www.geeksforgeeks.org/python/using-sqlite-aggregate-functions-in-python/

    cursor.execute('SELECT COUNT(vat_code) FROM Account')

    print(cursor.fetchone())

if __name__ == '__main__':
    get_count_account()