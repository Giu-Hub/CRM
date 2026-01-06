import sqlite3
from markupsafe import escape

DATABASE = 'crm.db'

def insert_contact(fields):
    connection = sqlite3.connect(DATABASE)

    cursor = connection.cursor()

    # https://stackoverflow.com/questions/30039451/sqlite-insert-in-flask

    firstName = fields["firstName"]
    lastName = fields["lastName"]
    taxCode = fields["taxCode"]
    email = fields["email"]
    phone = fields["phone"]
    vatCode = fields["vatCode"]
    try:
        cursor.execute('''INSERT INTO contacts (tax_code, first_name, last_name, phone, email, vat_code) 
                       VALUES (?, ?, ?, ?, ?, ?)''', (taxCode, firstName, lastName, phone, email, vatCode))
        
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

def get_account_details(vatCode):
    connection = sqlite3.connect(DATABASE)
    connection.row_factory = sqlite3.Row
    
    cursor=connection.cursor()
    cursor.execute('''SELECT *
                    FROM account
                    WHERE vat_code = ?
                    ''', (vatCode,))
    
    account = cursor.fetchone()

    return account

def get_contacts():
    connection = sqlite3.connect(DATABASE)
    connection.row_factory = sqlite3.Row

    cursor = connection.cursor()
    cursor.execute('''SELECT first_name, last_name, company_name , tax_code
                   FROM contacts c
                   JOIN account a
                   ON c.vat_code = a.vat_code
                   ORDER BY company_name, first_name, last_name ASC
    ''')
    contacts = cursor.fetchall()
    
    cursor.close()
    connection.close()
    return contacts

def get_contact(tax_code):
    connection = sqlite3.connect(DATABASE)
    connection.row_factory = sqlite3.Row

    cursor = connection.cursor()
    cursor.execute('''SELECT first_name, last_name, company_name , tax_code, email, phone
                   FROM contacts c
                   JOIN account a
                   ON c.vat_code = a.vat_code
                   WHERE tax_code = ?''', (tax_code, ))
    contact = cursor.fetchone()
    
    cursor.close()
    connection.close()

    return contact

def view_contact_by_vatcode(vat_Code):
    connection = sqlite3.connect(DATABASE)
    connection.row_factory = sqlite3.Row
    
    cursor = connection.cursor()
    cursor.execute('''SELECT first_name, last_name, company_name, tax_code 
                   FROM contacts c
                   JOIN account a
                   ON c.vat_code = a.vat_code
                   WHERE c.vat_code = ?
                   ORDER BY first_name, last_name ASC''', (vat_Code,))
    contacts = cursor.fetchall()
    return contacts

def delete_account(vat_code):
    connection = sqlite3.connect(DATABASE)

    cursor = connection.cursor()
    # https://stackoverflow.com/questions/5890250/on-delete-cascade-in-sqlite3
    cursor.execute("PRAGMA foreign_keys=ON")

    try:
        cursor.execute('''DELETE FROM account
                       WHERE vat_code = ? ''', (vat_code,))

        connection.commit()
    except sqlite3.Error as e:
        cursor.close()
        connection.close()

        return '500'

    cursor.close()
    connection.close()

    return '204'

def get_count_contacts():
    conn = sqlite3.connect(DATABASE)
    
    cursor = conn.cursor()
    cursor.execute("""
    SELECT COUNT(*)
                  FROM contacts
                   """)

    counters = cursor.fetchone()

    conn.close()
    return counters[0] 

def get_count_accounts():
    conn = sqlite3.connect(DATABASE)

    cursor = conn.cursor()
    cursor.execute("""  
      SELECT COUNT(*)
        FROM account
                   """,)
    
    counters = cursor.fetchone()
    
    conn.close()
    return counters[0]