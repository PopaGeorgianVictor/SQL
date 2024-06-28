import mysql.connector


mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='popa1993',
    port='3306',
    database='classicmodels'
)

mycursor = mydb.cursor()


'''Check table presence in database schema'''

mycursor.execute('show tables')

query1 = mycursor.fetchall()
for q1 in query1:
    print(q1)


    
'''Check number of columns in a table'''

mycursor.execute('SELECT count(*) AS NumbersOfColumns FROM information_schema.columns WHERE table_name = "customers" ')

query1 = mycursor.fetchall()
for q1 in query1:
    print(q1)