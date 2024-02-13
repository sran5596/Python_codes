
try:
    import mysql.connector
    con=mysql.connector.connect(host="localhost",port=3306,user="root",password="sraveendra009403@@",database="p1")
    cur=con.cursor()
    cur.execute("select * from ravi1")
    for row in cur:
        print(row[0],row[1],row[2]) # here it print the rows 1 2 3
        #row[0]    row[2]        row[3]
        #1        Raveenndra     1998-06-12
        #2        sam            1990-12-11
        #it print in vertical
    cur.close()
except Exception as e:
    print(e)