import sqlite3

database=sqlite3.connect("candidates.db")
cursor=database.cursor()
cursor.execute("DROP TABLE CANDIDATES")
cursor.execute('''CREATE TABLE CANDIDATES (
               NAME TEXT NOT NULL,
               VOTE INT NOT NULL
)''')
cursor.execute("INSERT INTO CANDIDATES (NAME,VOTE) VALUES  ('G',5),('L',4),('F',6)")
cursor.execute("SELECT * FROM CANDIDATES")
list=cursor.fetchall()
print(list)
