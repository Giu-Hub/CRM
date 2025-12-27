import sqlite3

DATABASE = '../crm'

def insert_account():
    connection = sqlite3.connect(DATABASE)

    cursor = connection.cursor()

    # https://stackoverflow.com/questions/30039451/sqlite-insert-in-flask

    cursor.execute('INSERT INTO contacts (vat_code, company_name, region) VALUES (IT123, Giuseppe, Campania)',
                   ( 'IT123','BMB', 'Campania' ))
    
    return '201'

def get_contacts():
    connection = sqlite3.connect(DATABASE)

    cursor = connection.cursor()
    cursor.execute('SELECT * FROM Account')
    res = cursor.fetchall()
    cursor.close()

    print(res)