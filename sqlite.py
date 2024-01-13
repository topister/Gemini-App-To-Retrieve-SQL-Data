import sqlite3

## connect to the sqlite database
connection =sqlite3.connect("student.db")

## create a cursor object to insert records/create table

cursor=connection.cursor()



## create a table
table_info="""
create table STUDENT(NAME VARCHAR(25), CLASS VARCHAR(25),
SECTION VARCHAR(25));

"""

#

cursor.execute(table_info)
## insert more records

cursor.execute("""Insert into STUDENT values('Krish','Software Engineering', 'A')""")
cursor.execute("""Insert into STUDENT values('Topister','Data Science', 'B')""")
cursor.execute("""Insert into STUDENT values('Onyango','Data Science', 'A')""")
cursor.execute("""Insert into STUDENT values('Nandera','Data Science', 'B')""")
## commit the transaction
## Display all records
print("The inserted records are")
data=cursor.execute("""Select * from STUDENT""")
for row in data:
    print(row)


connection.commit()
connection.close()