import pyodbc
from models.account import account

server = 'DESKTOP-9DCUPJF\SQLEXPRESS'
db = 'Flask_TUT'
tcon = True
uname = 'sa'
pword = '12345'
connection=pyodbc.connect(driver='{SQL Server}',
                      host=server, database=db, trusted_connection=tcon,
                      user=uname, password=pword)


def login_account(username, password):
    cursor = connection.cursor()
    query = f"exec login_account {username},{password}".format(username=username, password=password)
    cursor.execute(query)
    for i in cursor:
        acc  = account(username = i[0],password=i[1],address=i[2],email=i[3])
        return acc



