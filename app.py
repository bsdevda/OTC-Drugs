from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///example.db'
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    password = db.Column(db.String(80), nullable=False)
    address = db.Column(db.String(120), nullable=False)

with app.app_context():
    db.create_all()

@app.route('/')
def index():
    users = User.query.all()
    return render_template('index.html', users=users)

@app.route('/add_user', methods=['POST'])
def add_user():
    name = request.form['name']
    password = request.form['password']
    address = request.form['address']

    new_user = User(name=name, password=password, address=address)
    db.session.add(new_user)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        name = request.form['name']
        password = request.form['password']
        user = User.query.filter_by(name=name, password=password).first()

        if user:
            return f"Login successful for user: {name}"
        else:
            return "Login failed. Invalid credentials."

    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        password = request.form['password']
        address = request.form['address']

        new_user = User(name=name, password=password, address=address)
        db.session.add(new_user)
        db.session.commit()

        return f"Registration successful for user: {name}"

    return render_template('register.html')

if __name__ == '__main__':
    app.run(debug=True)
