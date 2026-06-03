from flask import Flask, redirect, request, render_template, session, url_for
import os
from dotenv import load_dotenv
from functools import wraps

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY')

def db_config_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if not session.get('db_config'):
            return redirect(url_for('index'))
        return f(*args, **kwargs)
    return decorated

def login_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if not session.get('utente'):
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        session['db_config'] = {
            'HOST'    : request.form.get('HOST'),
            'PORT'    : request.form.get('PORT'),
            'DB'      : request.form.get('DB'),
            'USERNAME': request.form.get('USERNAME'),
            'PASSWORD': request.form.get('PASSWORD')
        }
        return redirect(url_for('login'))
    else:
        return render_template('index.html')

@app.route("/login", methods=['GET', 'POST'])
@db_config_required
def login():

@app.route("/lista")
@db_config_required
@login_required
def lista():
    from rubrica import Rubrica
    r = Rubrica(session.get('db_config'))
    contatti = r.get_all()
    return render_template('lista.html', contatti=contatti)