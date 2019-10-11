from flask import Flask, render_template
import sqlite3
import json

app = Flask(__name__)

@app.route('/tablas')
def mostrar_tablas():
    conn = sqlite3.connect("ejemplo.db")
    c=conn.cursor()
    c.execute("select name from sqlite_master where type = 'table';")
    return json.dumps(list(c.fetchall()))

if __name__ == "__main__":
	app.run()
