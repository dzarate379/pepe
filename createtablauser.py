import sqlite3
conn=sqlite3.connect("user.db")
c=conn.cursor()
c.execute("CREATE TABLE user2 (name text,age integer)")
c.execute("INSERT INTO user2 VALUES ('user pepe',27)")
conn.commit()
c.execute("SELECT * FROM user2")
print(c.fetchall())
conn.close()