from flask import Flask, request, session, redirect, url_for, render_template
import json

app = Flask(__name__, template_folder="template")
app.secret_key = ""

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        print(username,password)

        with open("db.json") as db:
            data = json.load(db)
            if username in data and data[username]["password"] == password:
                session["logged_in"] = True
                session["username"] = username
                print("login successful")
                print("session is", session)
                return redirect(url_for("index"))
            else:
                return "Invalid username or password"
    return render_template("login.html")

@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        email = request.form["email"]
        username = request.form["username"]
        password = request.form["password"]

        with open("db.json", "r+") as db:
            data = json.load(db)
            if username not in data:
                data[username] = {
                    "email": email,
                    "username": username,
                    "password": password
                }
                db.seek(0)
                json.dump(data, db, indent=4)
                return redirect(url_for("login"))
            else:
                return "Username already exists. Please choose a different username."

    return render_template("signup.html")


@app.route("/logout")
def logout():
    session.pop("logged_in", None)
    session.pop("username", None)
    return redirect(url_for("login"))

    
if __name__ == "__main__":
    app.run(debug=True)



