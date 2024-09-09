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

@app.route('/edit/<string:id>')
def get_contact(id):
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM usuarios WHERE id = {0}'.format(id))
    data = cur.fetchall()
    return render_template('edit-contact.html', usuario = data[0])

@app.route('/update/<id>', methods=['POST'])
def update_contact(id):
    if (request.method == 'POST'):
        nombre = request.form['nombre']
        matricula = request.form['matricula']
        correo = request.form['correo']
        cur = mysql.connection.cursor()
        cur.execute("""UPDATE usuarios SET nombre = %s, matricula = %s, correo = %s WHERE id = %s""", [nombre, matricula, correo, id])
        mysql.connection.commit()
        flash('Usuario Updated Succesfully')
        return redirect(url_for('Index'))

@app.route('/delete/<string:id>')
def delete_contact(id):
    cur = mysql.connection.cursor()
    cur.execute('DELETE FROM usuarios WHERE id = {0}'.format(id))
    mysql.connection.commit()
    flash('Usuario Removed Succesfully')
    return redirect(url_for('Index'))

if __name__ == '__main__':
    app.run(port = 3000, debug = True)