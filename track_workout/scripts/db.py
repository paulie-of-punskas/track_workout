import pyodbc
import os

db_server :str = os.environ["db_server"]
db_name :str = os.environ["db_name"]
db_user :str = os.environ["db_user"]
db_pass :str = os.environ["db_pass"]

def test_connection():
    connectionString :str = f'DRIVER={{ODBC Driver 18 for SQL Server}};SERVER={db_server};DATABASE={db_name};UID={db_user};PWD={db_pass}'
    conn = pyodbc.connect(connectionString) 
    sql_query :str = """ SELECT * FROM track_workout """

    cursor = conn.cursor()
    cursor.execute(sql_query)
    columns = [column[0] for column in cursor.description]
    conn.close()
    return columns