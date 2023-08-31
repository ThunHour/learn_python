import psycopg2

try :
    db_conn=psycopg2.connect(host='localhost',port="5432",database='hour_data',user="postgres",passsword="seak1812002")
    cursor=db_conn.cursor()
    cursor.execute()
