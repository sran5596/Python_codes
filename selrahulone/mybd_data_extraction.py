# import mysql.connector
# con=mysql.connector.connect(host='localhost',port=3306,user='root',passwd='sraveendra009403@@',database='python_mysql_actions')
# curs=con.cursor()
# curs.execute("insert into mysql_python_operations1 values(1,'sraveendra')")
# curs.execute("insert into mysql_python_operations1 values(2,'herooss')")
# curs.execute("insert into mysql_python_operations1 values(3,'heroine')")
# con.commit()
# curs.close()

# import mysql.connector
# con=mysql.connector.connect(host='localhost',port=3306,user='root',password="sraveendra009403@@",database='python_mysql_actions')
# curs=con.cursor()
# curs.execute("set autocommit=0")
# curs.execute("set sql_safe_updates=0")
# print("before update")
# curs.execute("select * from mysql_python_operations1")
# for row in curs:
#     print(row[0],row[1])
# curs.execute("update mysql_python_operations1 set sname='sran' where sno=1")
# print("after update")
# curs.execute("select * from mysql_python_operations1")
# for row1 in curs:
#     print(row1[0],row1[1])
# con.commit()
# con.close()
# print()

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.service import Service
# import time
# import mysql.connector
# obj=Service("D:\drivers\chromedriver.exe")
# driver=webdriver.Chrome(service=obj)
# driver.get("https://demo.nopcommerce.com/register?returnUrl=%2Fregisterresult%2F1")
# con=mysql.connector.connect(host='localhost',port=3306,user='root',password="sraveendra009403@@",database='python_mysql_actions')
# curs=con.cursor()
# curs.execute("select * from mysql_python_operations1")
# for row in curs:
#     nmae=row[1]
# driver.find_element(By.XPATH,"//input[@id='FirstName']").send_keys(nmae)
# time.sleep(5)