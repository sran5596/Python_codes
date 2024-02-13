


# import mysql.connector
# con=mysql.connector.connect(host="localhost",port=3306,user="root",password="sraveendra009403@@",database="p1")
# cur=con.cursor()
# cur.execute("insert into ravi1 values(6,'Dhudhu','1998-12-23')")
# con.commit()
# con.close()

# file="D:\Datasets\ddttest.xlsx"
# from Day24selenium_excel_actions import Utility
# rows=Utility.getRowCount(file,"Sheet1")
# for r in range(2,rows+1):
#     price=Utility.readData(file,"Sheet1",r,1)
#     rateofinterest=Utility.readData(file,"Sheet1",r,2)
#     pre1=Utility.readData(file, "Sheet1", r,3)
import mysql.connector

con=mysql.connector.connect(host="localhost",port=3306,user="root",password="sraveendra009403@@",database="p1")
cur=con.cursor()
cur.execute("insert into ravi1 values(8,'gova','1976-11-23')")
con.commit()
con.close()