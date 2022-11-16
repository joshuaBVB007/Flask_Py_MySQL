from flask import Flask,render_template,redirect,url_for,request
from flask_mysqldb import MySQL

app = Flask(__name__)
 
my = MySQL(app)

@app.route('/')
def hello():
    return "<p>Hello!</p>"

@app.route('/mysql')
def mysql():
    cursor_BD=my.connection.cursor()
    #Executing SQL Statements
    cursor_BD.execute(''' INSERT INTO profile VALUES(%s,%s)''',(0,"maria"))
    my.connection.commit()
    #Closing the cursor
    cursor_BD.close()
    return "<p>Mysql lives in our server!</p>"    

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
