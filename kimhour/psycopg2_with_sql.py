import psycopg2
while True:
    print("Please choose :")
    print("1.Update")
    print("2.Delete")
    print("3.Stop")
    answer = int(input("Please write the answer by using the number:"))
    if answer == 1:
        try:
            db_conn = psycopg2.connect(host="localhost", port="5432",database="kit_b9", user="postgres", password="seak1812002")
            print("connection success")
            column_id =int(input("please enter column id:"))
            column_values=int(input("Enter Your mark values that want to update:"))
            cursor_statment = db_conn.cursor()
            cursor_statment.execute('UPDATE student_record SET mark = %s WHERE s_id = %s ' ,(column_values,column_id))
            db_conn.commit()
            print("completed task")
        except Exception as e:
            print(e)
            db_conn.rollback()
        finally:
            cursor_statment.close()
            db_conn.close()
    if answer == 2:
        try:
            db_conn = psycopg2.connect(host="localhost", port="5432",database="kit_b9", user="postgres", password="seak1812002")
            print("connection success")
            column_id2 = int(input("Which recod do you want to delete please enter id :"))
            cursor_statment = db_conn.cursor()
            cursor_statment.execute('DELETE FROM student_record WHERE s_id = %s ;',[column_id2])
            db_conn.commit()
            print("completed task")
        except Exception as e:
            print(e)
            db_conn.rollback()
        finally:
            cursor_statment.close()
            db_conn.close()
    elif answer ==3:
        print("Stopped")
        break

