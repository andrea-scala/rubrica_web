from flask import Flask, redirect, request, render_template, session, url_for
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY')

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
        return redirect(url_for('lista'))
    else:
        return render_template('index.html')
    