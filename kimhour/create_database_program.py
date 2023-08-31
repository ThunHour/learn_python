import psycopg2
try:
    db_conn = psycopg2.connect(host="localhost",port="5432",user="postgres",password="seak1812002")
    print("connected")
    db_conn.autocommit=True
    cursor=db_conn.cursor()
    print("received")
    cursor.execute('CREATE DATABASE hour_data')
    print("task completed")
except Exception as e:
    print(e)
finally:
    cursor.close()
    db_conn.close()
