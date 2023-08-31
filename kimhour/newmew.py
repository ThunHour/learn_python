import psycopg2
print("="*30, "Insert Value", "="*30, "\n") ###########################

db_conn = None            # can use this or not, it still work in python but if u don't use this in Java it will not work
cursor = None

# I have created database "kit_b9" and now i want to create table in DB "kit_b9"
try:
    db_conn = psycopg2.connect(host = "localhost", port = "5432", database = "kit_b9", user = "postgres", password = "seanghoR12345" )
    print("Connection successful.")     # if it connected it will print "connection success"
    cursor = db_conn.cursor()
    print("Cursor received")

    s_name = 'Hai Seanghor'
    marks = 99

    # Insert the record value
    cursor.execute("INSERT INTO student_mark (s_name, mark) VALUES(%s, %s);", (s_name, marks))
    db_conn.commit()                              # use this to commit, when you don't use auto commit
    print("Record inserted successfully")

except Exception as e:
    print("Issue: ", e)
finally:
    db_conn.close()              # when done all task, don't forgot to close file
    print("File is closed.")
    cursor.close()
    print("Cursor closed")
