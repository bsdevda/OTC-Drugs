from flask import Flask, render_template, request, redirect, url_for, session

from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///example.db'
app.config['SECRET_KEY'] = 'your_secret_key'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    password = db.Column(db.String(80), nullable=False)
    address = db.Column(db.String(120), nullable=False)

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    price = db.Column(db.Float, nullable=False)

with app.app_context():
    db.create_all()

# Function to check if a password meets the minimum length requirement
def is_valid_password(password):
    return len(password) >= 6  # Adjust the minimum length as needed

# Function to check if the input is empty or exceeds a certain length
def is_valid_input(input_value, max_length):
    return input_value and len(input_value) <= max_length

@app.route('/')
def index():
    user = User.query.get(session.get('user_id'))
    items = Item.query.all()
    cart = session.get('cart', [])
    return render_template('index.html', user=user, items=items, cart=cart)

@app.route('/add_user', methods=['POST'])
def add_user():
    name = request.form['name']
    password = request.form['password']
    address = request.form['address']

    new_user = User(name=name, password=password, address=address)
    db.session.add(new_user)
    db.session.commit()
    session['user_id'] = new_user.id
    return redirect(url_for('index'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        name = request.form['name']
        password = request.form['password']
        user = User.query.filter_by(name=name, password=password).first()

        if user:
            session['user_id'] = user.id
            return redirect(url_for('index'))
        else:
            return "Login failed. Invalid credentials."

    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('user_id', None)
    session.pop('cart', None)  # Clear the cart when logging out
    return redirect(url_for('index'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        password = request.form['password']
        address = request.form['address']

        # Check input validity
        if not is_valid_input(name, 80):
            return "Invalid name. Please provide a valid name."
        if not is_valid_password(password):
            return "Invalid password. Password must be at least 6 characters long."
        if not is_valid_input(address, 120):
            return "Invalid address. Please provide a valid address."

        # Check if the username already exists
        if User.query.filter_by(name=name).first():
            return "Username already exists. Please choose a different username."

        new_user = User(name=name, password=password, address=address)
        db.session.add(new_user)
        db.session.commit()

        session['user_id'] = new_user.id
        return redirect(url_for('index'))

    return render_template('register.html')

@app.route('/add_to_cart', methods=['POST'])
def add_to_cart():
    if 'user_id' not in session:
        return redirect(url_for('login'))

    user_id = session['user_id']
    item_name = request.form['item_name']

    cart = session.get('cart', [])
    if item_name not in cart:
        cart.append(item_name)
        session['cart'] = cart

    return redirect(url_for('index'))

@app.route('/cart')
def view_cart():
    if 'user_id' not in session:
        return redirect(url_for('login'))

    user = User.query.get(session['user_id'])
    cart = session.get('cart', [])

    return render_template('cart.html', user=user, cart=cart)

@app.route('/checkout')
def checkout():
    if 'user_id' not in session:
        return redirect(url_for('login'))

    user = User.query.get(session['user_id'])
    cart = session.get('cart', [])

    # Fetch item prices from the database
    items = Item.query.filter(Item.name.in_(cart)).all()

    # Calculate total cost
    total_cost = sum(item.price for item in items)

    return render_template('checkout.html', user=user, cart=cart, items = items, total_cost=total_cost)

if __name__ == '__main__':
    app.run(debug=True)
