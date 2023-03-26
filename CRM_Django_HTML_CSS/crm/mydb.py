import mysql.connector

dataBase = mysql.connector.connect(
    host = '',
    user = '',
    passwd = ''
    )

## Preaparing a cursor object
cursorObject = dataBase.cursor()

## Creating a database
cursorObject.execute('CREATE DATABASE crm_db')

print('DataBase created !!')