from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy
import json

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///ejemplo.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db=SQLAlchemy(app)
db.Model.metadata.reflect(db.engine)

x = "/tablas";
@app.route(x)
def mostrar():
    return json.dumps(list(db.Model.metadata.tables.keys()))


@app.route("/tablas/html")
def mostrar_html():
    return render_template('hello.html',tables=list(db.Model.metadata.tables.keys()))

@app.route("/tablas/<tabla>/")
def mostrar_tabla(tabla):
    
    if tabla in list(db.Model.metadata.tables.keys()):
        return json.dumps(db.session.query(db.Model.metadata.tables[tabla]).all())
    else:
        return "Tabla no encontrada"

@app.route("/tablas/html/<tabla>/")
def mostrar_tabla_html(tabla):
    
    if tabla in list(db.Model.metadata.tables.keys()):
        return render_template('hello_tabla.html',datos=list(db.session.query(db.Model.metadata.tables[tabla]).all()))
    else:
        return "Tabla no encontrada"

if __name__=="__main__":
    app.run()
