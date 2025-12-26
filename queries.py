import sqlite3

DATABASE = '../crm.db'

def insert_account(fields):
    connection = sqlite3.connect(DATABASE)

    cursor = connection.cursor()

    # https://www.geeksforgeeks.org/python/using-sqlite-aggregate-functions-in-python/

    # Fai la query di INSERT
    # Se andato a buon fine ritorna 201
    # Altrimenti cercare un errore di ritorno quando fallisce 503

    return '200'