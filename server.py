#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask
from flask import Response
from flask import render_template
from flask import request
from flask import flash
from functools import wraps
import sqlite3
import time 

db = sqlite3.connect('notlar.db',check_same_thread=False)
c = db.cursor()

def check_auth(username, password):

    return username == 'admin' and password == 'password'

def authenticate():
	
    return Response(
    'Kullanıcı girişi yapmadan not ekleyip silemezsiniz !', 401,
    {'WWW-Authenticate': 'Basic realm="Yetkili Kullanici Girisi"'})

def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if not auth or not check_auth(auth.username, auth.password):
            return authenticate()
        return f(*args, **kwargs)
    return decorated


app = Flask(__name__)

@app.route("/not/")
def show_index():
	c.execute("SELECT * FROM notlar")
	data = c.fetchall()
	print data
	return render_template("show.htm",data=data[::-1])

@app.route("/not/<int:id>")
def show_id(id):
	c.execute("SELECT * FROM notlar WHERE id=?", (id,))
	data = c.fetchall()
	return render_template("show.htm",data=data[::-1])

@app.route("/not/ekle")
@requires_auth
def show_textbox():
	c.execute("SELECT * FROM notlar")
	data = c.fetchall()
	return render_template("add.htm",data=data[::-1])
	
@app.route("/not/sil/<id>/", methods=['GET'])
@requires_auth
def delete_post(id):
	c.execute("DELETE FROM notlar WHERE  id=?", (id,))
	c.execute("SELECT COUNT(*) FROM notlar;")
	count = c.fetchall()[0][0]
	c.execute("UPDATE sqlite_sequence SET seq=? WHERE name='notlar'", (count,))	
	db.commit()
	return "Gonderi silindi !"	

@app.route("/not/ekle/gonder", methods=['POST'])
@requires_auth
def add_post():
	mesaj=request.form['not']
	tarih = time.strftime("%d/%m/%Y")
	saat = time.strftime("%H:%M")
	c.execute("INSERT INTO notlar VALUES (null,?,?,?)",(mesaj,tarih,saat))
	db.commit()
	return "<script>document.location ='/not/ekle'</script>"
	
if __name__ == "__main__":
	app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
	app.run(port=8080,debug=True)

