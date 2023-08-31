import psycopg2
try:
    db_conn = psycopg2.connect(host='localhost',port='5432',database='hour_data',user='postgres',password='seak1812002')
    cursor = db_conn.cursor()
    cursor.execute("CREATE TABLE hour_record (id SERIAL,name varchar NOT NULL,age int CHECK(age<100),p_number int NOT NULL UNIQUE)")
    db_conn.commit()
    print('task completed')
except Exception as e:
    print(e)
finally:
    db_conn.close()
    cursor.close()
