import sqlite3
import time
conn = sqlite3.connect('notlar.db')
c = conn.cursor()
c.execute("CREATE TABLE notlar(id INTEGER PRIMARY KEY AUTOINCREMENT, note text, tarih text, saat text)")
c.execute("INSERT INTO notlar VALUES (null,'Lorem impsum sit dolor amet','"+ time.strftime("%d/%m/%Y") +"','"+ time.strftime("%H:%M") +"')")
c.execute("INSERT INTO notlar VALUES (null,'Test post with <b>HTML</b> !','"+ time.strftime("%d/%m/%Y") +"','"+ time.strftime("%H:%M") +"')")
conn.commit()
conn.close()
print "Veritabani olusturuldu !"

