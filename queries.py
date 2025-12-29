import sqlite3
from markupsafe import escape

DATABASE = '../crm.db'

def insert_account(fields):
    connection = sqlite3.connect(DATABASE)

    cursor = connection.cursor()

    # https://stackoverflow.com/questions/30039451/sqlite-insert-in-flask

    vatCode = escape(fields['vatCode'])
    companyName = escape(fields['companyName'])
    streetName = escape(fields['streetName'])
    region = escape(fields['region'])

    # https://zetcode.com/python/sqlite3-integrityerror/#:~:text=The%20sqlite3.,would%20break%20database%20integrity%20rules.

    try:
        cursor.execute('INSERT INTO account (vat_code, company_name, street_name, region) VALUES (?, ?, ?, ?)',
                    ( vatCode, companyName, streetName, region ))

        connection.commit()
    except sqlite3.IntegrityError as e:
        cursor.close()
        connection.close()

        return '500'

    cursor.close()
    connection.close()

    return '201'

def get_accounts():
    # https://docs.python.org/3/library/sqlite3.html#sqlite3.Connection.row_factory
    connection = sqlite3.connect(DATABASE)
    connection.row_factory = sqlite3.Row

    cursor = connection.cursor()
    cursor.execute('SELECT vat_code, company_name FROM account')
    res = cursor.fetchall()
    
    connection.close()

    return res