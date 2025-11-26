from flask import Flask, render_template, request, redirect, url_for 
import sqlite3
app = Flask(__name__)

def init_db():
    sql=sqlite3.connect('alunos.db')
    cursor=sql.cursor()
    cursor.execute('''
                    CREATE TABLE IF NOT EXISTS aluno(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT NOT NULL,
                    idade INTEGER NOT NULL,
                    peso REAL NOT NULL,
                    horario TEXT NOT NULL
                   )
                   
                   
                   ''')
    sql.commit()
    sql.close()
init_db()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/agendar',methods=['POST'])
def agendar():
    nome=request.form['nome']
    idade=request.form['idade']
    peso=request.form['peso']
    horario=request.form['horario']

    sql=sqlite3.connect('alunos.db')
    cursor=sql.cursor()
    cursor.execute('INSERT INTO aluno(nome,idade,peso,horario)VALUES(?,?,?,?)',(nome,idade,peso,horario))
    sql.commit()
    sql.close()

    return redirect(url_for('index'))

app.run(debug=True)







