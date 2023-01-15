import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='popa1993',
    port='3306',
    database='petclinic'
)

mycursor = mydb.cursor()
mycursor.execute('SELECT * FROM pets')

pets = mycursor.fetchall()
for pet in pets:
    print(pet)


mycursor = mydb.cursor()
mycursor.execute('SELECT * FROM owners')

owners = mycursor.fetchall()
for owner in owners:
    print(owner)