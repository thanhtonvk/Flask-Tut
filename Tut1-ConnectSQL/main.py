from cgitb import reset
import pyodbc
import pandas as pd

#driver: 
#server name:
#database name:
#trusted_connection:  default yes

# connect to sql
connection = pyodbc.connect('Driver={SQL Server};'
                            'Server=DESKTOP-IDBDCHG\SQLEXPRESS;'
                            'Database=ConnectSQL;'
                            'Trusted_Connection=yes;')
cursor = connection.cursor()
query = "select * from Person"



# execute query

def insert(person):
    query = "insert into Person(Name,Address) values (N'{name}',N'{address}')".format(name = person[0],address = person[1])
    return cursor.execute(query)



person = ("Do thanhton ","Huwng yen")


result = insert(person)
connection.commit()
print(result)

if result:
    print('Thanh cong')
else:
    print('That bai')




# read sql from scratch
cursor.execute(query)
for i in cursor:
    print(i[0])


#using pandas
df = pd.read_sql_query(query,connection)
print(df)