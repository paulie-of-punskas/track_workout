import pyodbc
import os
import logging

db_server :str = os.environ["db_server"]
db_name :str = os.environ["db_name"]
db_user :str = os.environ["db_user"]
db_pass :str = os.environ["db_pass"]
driver= '{ODBC Driver 18 for SQL Server}'

# === pasak 
with pyodbc.connect('DRIVER='+driver+';SERVER=tcp:'+db_server+';PORT=1433;DATABASE='+db_name+';UID='+db_user+';PWD='+db_pass+';Connection Timeout=60;Encrypt=yes;TrustServerCertificate=no') as conn:
    with conn.cursor() as cursor:
        rows = []
        cursor.execute("SELECT * from track_workout")
        # row = cursor.fetchall()
        row = cursor.fetchall()
        print(row[0])
