import os
from jinja2 import StrictUndefined
from flask import Flask, render_template, redirect, flash, session, request
from flask_debugtoolbar import DebugToolbarExtension
import json
import bcrypt
from werkzeug import secure_filename

from model import User

app = Flask(__name__)
app.secret_key = os.environ.get('FLASK_SECRET_KEY')

app.config['UPLOAD_FOLDER'] = 'static/uploads'
app.config['ALLOWED_EXTENSIONS'] = set(['png', 'jpg', 'jpeg'])
app.config['MAX_CONTENT_LENGTH'] = 1 * 1024 * 1024

app.jinja_env.undefined = StrictUndefined
app.jinja_env.auto_reload = True

##############################################################################


@app.route('/')
def index():
    """Homepage."""

    return render_template('index.html')


@app.route('/register', methods=['POST', 'GET'])
def register():
    """Show register form and complete registration."""

    if not session.get('user_id'):
        if methods == 'GET':
            return render_template('register.html')
        else:
            username = request.form.get('username')
            email = request.form.get('email')
            password = bcrypt.hashpw(request.form.get('password').encode('utf-8'), bcrypt.gensalt())

            if User.query.filter_by(username=username).all():
                flash('Unavailable username')
                return redirect('/register')

            if User.query.filter_by(email=email).all():
                flash('This email is already registered')
                return redirect('/register')

            new_user = User(username=username,
                            email=email,
                            password=password)

            db.session.add(new_user)
            db.session.commit()

            return redirect('/login')

#############################################################################

if __name__ == "__main__":
    app.debug = True
    DebugToolbarExtension(app)
    # connect_to_db(app)
    app.run()

