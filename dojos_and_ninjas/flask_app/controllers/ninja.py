from flask import Flask, render_template, redirect, request
from flask_app.config.mysqlconnection import connectToMySQL

app = Flask(__name__)

# CREATE NINJA
@app.route('/ninjas/create', methods=['POST'])
def create_ninja():
    mysql = connectToMySQL('dojos_and_ninjas_original')
    query = 'INSERT INTO ninjas (first_name, last_name, age, dojo_id) VALUES (%(fn)s, %(ln)s, %(a)s, %(did)s);'
    data = {
        'fn': request.form['first_name'],
        'ln': request.form['last_name'],
        'a': request.form['age'],
        'did': request.form['dojo_id']
    }
    ninja_id = mysql.query_db(query, data)
    return redirect(f'/dojos/{request.form["dojo_id"]}')

# NEW NINJA FORM
@app.route('/ninjas/new')
def new_ninja():
    mysql = connectToMySQL('dojos_and_ninjas_original')
    dojos = mysql.query_db('SELECT * FROM dojos;')
    return render_template('new_ninja.html', dojos=dojos)
