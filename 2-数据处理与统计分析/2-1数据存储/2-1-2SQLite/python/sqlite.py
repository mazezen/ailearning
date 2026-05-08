#!/usr/bin/python3

import sqlite3

conn = sqlite3.connect("py-test.db")
print("数据库连接成功...")

c = conn.cursor()

c.execute('''
CREATE TABLE IF NOT EXISTS COMPANY(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    NAME TEXT NOT NULL,
    AGE INT NOT NULL,
    ADDRESS CAHR(50),
    SALARY REAL
);
''')
print("数据表创建成功...")


c.execute("INSERT INTO COMPANY (NAME, AGE, ADDRESS, SALARY) VALUES ('Paul', 32, 'California', 20000.00)")
c.execute("INSERT INTO COMPANY (NAME, AGE, ADDRESS, SALARY) VALUES ('Allen', 20, 'Texas', 15000.00)")
c.execute("INSERT INTO COMPANY (NAME, AGE, ADDRESS, SALARY) VALUES ('Teddy', 19, 'Norway', 18000.00)")
c.execute("INSERT INTO COMPANY (NAME, AGE, ADDRESS, SALARY) VALUES ('Mark', 25, 'Rich-Mond', 30000.00)")
conn.commit()
print("数据写入成功...")

cursor_row = c.execute("SELECT ID, NAME, ADDRESS, SALARY FROM COMPANY")
for row in cursor_row:
    print ("ID = ", row[0])
    print ("NAME = ", row[1])
    print ("ADDRESS = ", row[2])
    print ("SALARY = ", row[3])


c.execute("UPDATE COMPANY SET SALARY = 9999.00 WHERE ID = 1")
conn.commit()

c.execute("DELETE FROM COMPANY WHERE ID = 10");
conn.commit()


cursor_row = c.execute("SELECT ID, NAME, ADDRESS, SALARY FROM COMPANY")
for row in cursor_row:
    print ("ID = ", row[0])
    print ("NAME = ", row[1])
    print ("ADDRESS = ", row[2])
    print ("SALARY = ", row[3])

conn.close()

