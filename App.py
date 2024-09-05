from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_DB'] = 'flaskproyect'
mysql = MySQL(app)

app.secret_key = 'mysecretkey'

@app.route('/')
def Index():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM usuarios')
    data = cur.fetchall()
    return render_template('index.html', usuarios = data)

@app.route('/add_contact', methods=['POST'])
def add_contact():
    if (request.method == 'POST'):
        nombre = request.form['nombre']
        matricula = request.form['matricula']
        correo = request.form['correo']
        cur = mysql.connection.cursor()
        cur.execute('INSERT INTO usuarios (nombre, matricula, correo) VALUES (%s, %s, %s)', [nombre, matricula, correo])
        mysql.connection.commit()
        return redirect(url_for('Index'))

@app.route('/edit')
def edit_contact():
    return 'edit'

@app.route('/delete')
def delete_contact():
    return 'delete'

if __name__ == '__main__':
    app.run(port = 3000, debug = True)