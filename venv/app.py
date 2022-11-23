from flask import Flask,render_template,redirect,url_for,request
from flask_mysqldb import MySQL

app = Flask(__name__) 
my = MySQL(app)

@app.route('/')
def hello():
    return "<p>Hello!</p>"

# doing mysql CRUD
@app.route('/select')
def select():
    cursor_BD=my.connection.cursor()
    cursor_BD.execute(''' SELECT * from profile ''')
    article = cursor_BD.fetchall()
    #Closing the cursor
    cursor_BD.close()
    return f"<p>{article}</p>"    

@app.route('/insert')
def insert():
    cursor_BD=my.connection.cursor()
    #Executing SQL Statements
    cursor_BD.execute(''' INSERT INTO profile VALUES(%s,%s)''',(0,"fifa23"))
    my.connection.commit()
    #Closing the cursor
    cursor_BD.close()
    return f"<p>data has been inserted correctly</p>"

@app.route('/update')
def update():
    cursor_BD=my.connection.cursor()
    #Executing SQL Statements
    cursor_BD.execute(''' update profile set bio=%s where bio=%s ''',("Ignacio","maria"))
    my.connection.commit()
    #Closing the cursor
    cursor_BD.close()
    return f"<p>update has been done correctly</p>"

@app.route('/delete')
def delete():
    cursor_BD=my.connection.cursor()
    #Executing SQL Statements
    cursor_BD.execute(''' delete from profile where id=%s''',("6"))
    my.connection.commit()
    #Closing the cursor
    cursor_BD.close()
    return f"<p>delete has been done correctly</p>"

# Re-directing
@app.route("/")
def redirect():
    return redirect(url_for('jona'))

# example using a variable rule(<username>)
@app.route('/world/<username>')
def world(username):
    return f"<p>Hello, {username}</p>"

# render templates
@app.route('/jona/<person>')
def jona(person=None):
    return render_template('jona.html',person=person);
