import mysql.connector

conn = mysql.connector.connect(host='localhost', database='mykdb', user='root', password='Ilovesql@143')

if conn.is_connected():
    print("DB connected successfully")

cursor = conn.cursor()


def printRowsFromDB():
    cursor.execute('select * from my_emp')
    # row = cursor.fetchone()
    rows = cursor.fetchall()
    print("Total number of rows", cursor.rowcount)
    print("The data fetched from the DB is ==========>>>>>>")
    for row in rows:
        print(row)


def insertRowsInDB():
    try:
        cursor.execute("insert into my_emp values(17, 'tbd', 200000, 'Hyderabad')")
        conn.commit()
        print("Employee added to DB")
    except:
        conn.rollback()


def deleteFromDB(EmpId):
    query = "delete from my_emp where id= '%d'"
    args = (EmpId)
    try:
        cursor.execute(query % args)
        conn.commit()
        print("Recorde deleted successfully ================>>>>>>>")
    except:
        conn.rollback()


#insertRowsInDB()
printRowsFromDB()
#deleteFromDB(17)

cursor.close()
conn.close()
