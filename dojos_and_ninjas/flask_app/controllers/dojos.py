from flask import Flask, render_template, request, redirect, url_for
from flask_app.config.mysqlconnection import connectToMySQL

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', dojos=dojos)
    # return redirect(url_for('dojos'))

@app.route('/dojos')
def dojos():
    mysql = connectToMySQL('ninjas_and_dojos_original')
    dojos = mysql.query_db('SELECT * FROM dojos;')
    return render_template('dojos.html', dojos=dojos)

@app.route('/dojos/new', methods=['GET', 'POST'])
def new_dojo():
    if request.method == 'POST':
        mysql = connectToMySQL('ninjas_and_dojos_original')
        query = "INSERT INTO dojos (name, created_at, updated_at) VALUES (%(name)s, NOW(), NOW());"
        data = {
            'name': request.form['name']
        }
        mysql.query_db(query, data)
        return redirect(url_for('dojos'))
    else:
        return render_template('new_dojo.html')

@app.route('/dojos/<int:dojo_id>')
def show_dojo(dojo_id):
    mysql = connectToMySQL('ninjas_and_dojos_original')
    query = "SELECT * FROM dojos WHERE id = %(id)s;"
    data = {
        'id': dojo_id
    }
    dojo = mysql.query_db(query, data)
    mysql = connectToMySQL('ninjas_and_dojos_original')
    query = "SELECT * FROM ninjas WHERE dojo_id = %(id)s;"
    ninjas = mysql.query_db(query, data)
    return render_template('show_dojo.html', dojo=dojo[0], ninjas=ninjas)

@app.route('/ninjas/new', methods=['GET', 'POST'])
def new_ninja():
    if request.method == 'POST':
        mysql = connectToMySQL('ninjas_and_dojos_original')
        query = "INSERT INTO ninjas (first_name, last_name, age, dojo_id, created_at, updated_at) VALUES (%(first_name)s, %(last_name)s, %(age)s, %(dojo_id)s, NOW(), NOW());"
        data = {
            'first_name': request.form['first_name'],
            'last_name': request.form['last_name'],
            'age': request.form['age'],
            'dojo_id': request.form['dojo_id']
        }
        ninja_id = mysql.query_db(query, data)
        return redirect(url_for('show_dojo', dojo_id=request.form['dojo_id']))
    else:
        mysql = connectToMySQL('ninjas_and_dojos_original')
        query = "SELECT * FROM dojos;"
        dojos = mysql.query_db(query)
        return render_template('new_ninja.html', dojos=dojos)

if __name__ == '__main__':
    app.run(debug=True)
