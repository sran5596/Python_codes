

try:
    import time
    import mysql.connector #it connect the db
#in host ip address is also okay
    con=mysql.connector.connect(host="localhost",port=3306,user="root",password="sraveendra009403@@",database="p1")
#host=ip address or localhost give anything is okay
#user=root & password
#database=in mysql which one you need to do actions give here[[pi]]
    time.sleep(2)
    curs=con.cursor() #through to this we actions
    curs.execute("insert into one values(2)") # insert the values here
    con.commit() # it commit the update value store
    con.close() # close the
    print("finish")
except ExceptionGroup as e:
    print(e)
    print("Connection failed")

