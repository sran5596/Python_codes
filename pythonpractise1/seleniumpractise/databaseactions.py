import mysql.connector
con=mysql.connector.connect(host="localhost",port=3306,user="root",password="sraveendra009403@@",database="p1")
curs=con.cursor()
curs.execute("select* from one")
con.commit()
con.close()