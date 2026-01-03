import sqlite3
from markupsafe import escape
from datetime import datetime

DATABASE = '../crm.db'

def insert_contact(fields):
    connection = sqlite3.connect(DATABASE)

    cursor = connection.cursor()

    # https://stackoverflow.com/questions/30039451/sqlite-insert-in-flask

    date = datetime.today().strftime('%Y-%m-%d')

    firstName = fields["firstName"]
    lastName = fields["lastName"]
    taxCode = fields["taxCode"]
    email = fields["email"]
    phone = fields["phone"]
    vatCode = fields["vatCode"]
    try:
        cursor.execute('''INSERT INTO contacts (tax_code, first_name, last_name, phone, email, created_date, vat_code) 
                       VALUES (?, ?, ?, ?, ?, ?, ?)''', (taxCode, firstName, lastName, phone, email, date, vatCode))
        
        connection.commit()
    except sqlite3.InterruptedError as e:
        cursor.close()
        connection.close()

        return '500'
    
    return '201'

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
    cursor.execute('''SELECT vat_code, company_name 
                   FROM account
                   ORDER BY company_name ASC''')
    res = cursor.fetchall()

    connection.close()

    return res

def get_contacts():
    connection = sqlite3.connect(DATABASE)
    connection.row_factory = sqlite3.Row

    cursor = connection.cursor()
    cursor.execute('''SELECT first_name, last_name, company_name 
                   FROM contacts c
                   JOIN account a
                   ON c.vat_code = a.vat_code
                   ORDER BY company_name, first_name, last_name ASC
    ''')
    contacts = cursor.fetchall()
    
    cursor.close()
    connection.close()
    return contacts

def view_contact_by_vatcode(vat_Code):
    connection = sqlite3.connect(DATABASE)
    connection.row_factory = sqlite3.Row
    
    cursor = connection.cursor()
    cursor.execute('''SELECT first_name, last_name, company_name 
                   FROM contacts c
                   JOIN account a
                   ON c.vat_code = a.vat_code
                   WHERE c.vat_code = ?
                   ORDER BY first_name, last_name ASC''', (vat_Code,))
    contacts = cursor.fetchall()
    return contacts