from flask import Flask, render_template
import sqlite3, json, sys

app = Flask(__name__)
base_datos=sys.argv[1]

def get_cursor():
    conn = sqlite3.connect(base_datos)
    c=conn.cursor()
    return c

def get_tables():
    cur=get_cursor().execute("select name from sqlite_master where type = 'table';")
    res=cur.fetchall()
    cur.close()
    return res

@app.route('/tablas/')
def mostrar_tablas():
    return json.dumps(get_tables())

@app.route('/html/tablas/')
def mostrar_tablas_html():
    return render_template('config.html',title="Las tablas de la base de datos "+ base_datos +" son ", tables=(get_tables()))

@app.route("/tablas/<tabla>/")
def mostrar_tabla_registros(tabla):
    if (tabla,) in get_tables():
        cur=get_cursor().execute("select * from "+tabla+";")
        res=cur.fetchall()
        cur.close()
        return json.dumps(list(res))
    else:
        return "Tabla no encontrada"
        

@app.route("/html/tablas/<tabla>/")
def mostrar_tabla_registros_html(tabla):
    if (tabla,) in get_tables():
        cur=get_cursor().execute("select * from "+tabla+";")
        res=cur.fetchall()
        cur.close()
        return render_template('config.html',title="Registros en tabla "+tabla,tables=(res))
    else:
        return render_template('noTabla.html')
    
@app.route("/tablas/<tabla>/info/")
def mostrar_tabla_columnas(tabla):
    if (tabla,) in get_tables():
        cur=get_cursor().execute("select * from "+tabla+";")
        res=cur.fetchall()
        res_col=cur.description
        cur.close()
        filas=len(res)
        registros="El numero de registros de la tabla "+tabla+" es "+repr(filas)
        columnas=[]
        for element in res_col:
            columnas.append(element[0])
        columnas.append(registros)
        return json.dumps(columnas)
    else:
        return "Tabla no encontrada"
    
@app.route("/html/tablas/<tabla>/info/")
def mostrar_tabla_columnas_html(tabla):
    if (tabla,) in get_tables():
        cur=get_cursor().execute("select * from "+tabla+";")
        res=cur.fetchall()
        res_col=cur.description
        cur.close()
        filas=len(res)
        registros="El numero de registros de la tabla "+tabla+" es "+repr(filas)
        columnas=[]
        for element in res_col:
            columnas.append(element[0])
        columnas.append(registros)
        return render_template('config.html',title="Datos en tabla "+tabla,tables=list(columnas))
    else:
        return render_template('noTabla.html')

if __name__ == "__main__":
    app.run()
