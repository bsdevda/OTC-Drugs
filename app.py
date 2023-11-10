from flask import Flask, redirect, url_for, request, render_template


app = Flask(__name__)

@app.route('/')
def index():
    user = ""
    if request.args:
        user = request.args['user']
    return render_template('index.html', user = user)

@app.route('/login', methods = ['POST', 'GET'])
def login():
    error = ""
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["passw"]
        fetchedUser = Users.query.filter_by(email = email, password = password).first()
        print(fetchedUser)
        if fetchedUser:
            user = fetchedUser.fullname
            userid = fetchedUser.id
            return redirect(url_for('index', user = user, **request.args))
        else:
            error = "Invalid credentials!"
    return render_template('login.html', error = error)



if __name__ == '__main__':
    app.run(debug = True)