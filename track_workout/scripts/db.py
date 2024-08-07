import pyodbc
import os
import logging
import time
from datetime import datetime

db_server :str = os.environ["db_server"]
db_name :str = os.environ["db_name"]
db_user :str = os.environ["db_user"]
db_pass :str = os.environ["db_pass"]

def db_connect():
    connection_string :str = f'DRIVER={{ODBC Driver 18 for SQL Server}};SERVER={db_server};DATABASE={db_name};UID={db_user};PWD={db_pass};Connection Timeout=60;Encrypt=yes;TrustServerCertificate=no'
    # db_connection = pyodbc.connect(connection_string) 
    # === investigate timetout
    # cursor = db_connection.cursor()
    retry_flag = True
    retry_count :int = 0

    print("[SQL] Connecting to database")
    while retry_flag and retry_count < 5:
        try:
            db_connection = pyodbc.connect(connection_string)
            retry_flag :bool = False
        # except pyodbc.OperationalError as e:
        except pyodbc.InterfaceError as e:
            retry_flag :bool = True
            error_message :str = e.args[1]
            retry_count = retry_count + 1
        except pyodbc.ProgrammingError as e:
            error_message :str = e.args[1]
            retry_count = retry_count + 1
        except pyodbc.OperationalError as e:
            retry_count = retry_count + 1
            retry_flag :bool = True
            error_message :str = e.args[1]
            print(">> Retry after 5 seconds")
            time.sleep(5)
            # db_connection = pyodbc.connect(connection_string)

    if retry_flag == True:
        print(f"[SQL Error] Login failed after 5 tries: {error_message}")
        return None
    else:
        print(f"[SQL] Connection successful at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        cursor = db_connection.cursor()
        return cursor


def db_connect_old2():
    connection_string :str = f'DRIVER={{ODBC Driver 18 for SQL Server}};SERVER={db_server};DATABASE={db_name};UID={db_user};PWD={db_pass};Connection Timeout=60;Encrypt=yes;TrustServerCertificate=no'
    db_connection = pyodbc.connect(connection_string) 
    # === investigate timetout
    retry_flag = True
    retry_count = 0
    cursor = db_connection.cursor()

    try:
        db_connection.cursor()
    # except pyodbc.OperationalError as e:
    except pyodbc.OperationalError as e:
        print(e)
        print(">> Retry after 5 sec")
        time.sleep(5)
        cursor = db_connection.cursor()
    return cursor


def db_connect_old1():
    connection_string :str = f'DRIVER={{ODBC Driver 18 for SQL Server}};SERVER={db_server};DATABASE={db_name};UID={db_user};PWD={db_pass};Connection Timeout=60;Encrypt=yes;TrustServerCertificate=no'

    db_connection = pyodbc.connect(connection_string)
    
    # === investigate timetout
    error_message = None

    try:
        cursor = db_connection.cursor()
    except pyodbc.Error as e:
        sql_state = e.args[0]
        error_message = e.args[1]
        logging.getLogger(__name__).warning("ODBC driver does not implement the connection timeout attribute. "
                    "Error code: %s - %s", sql_state, error_message)
        pass
    cursor.execute("SELECT * from track_workout")

    if error_message is None:
        query_result = cursor.fetchall()
        db_connection.close()
        return query_result
    else:
        db_connection.close()
        return error_message

def db_get_all_data():
    # === connect
    # === get data
    # === return data
    sql_query :str = " SELECT * FROM track_workout "
    cursor = db_connect()
    if cursor is not None:
        cursor.execute(sql_query)
        query_result = cursor.fetchall()
        return query_result
    else:
        return f"[SQL error] Error while obtaining cursor."

def db_insert(values) -> None:
    """
    Method is used for adding attribute values of Workout class.
    "values", needs following pattern: (2024-01-01, nugara, prisitraukimai, 8, 8, '') 
    """
    # cursor = db_connect()
    sql_query :str = f"INSERT INTO track_workout (date, muscle, exercise, kg, rep, comment) VALUES ({values});"
    print(">> SQL query: ")
    print(sql_query)
    cursor = db_connect()
    cursor.execute(sql_query)
    cursor.commit()
    print(">> Records were added")
