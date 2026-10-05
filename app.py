from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)


# ==============================
# LOGIN
# ==============================

@app.route("/")
def home():
    return redirect(url_for("login"))


@app.route("/login")
def login():
    return render_template("login.html")


# ==============================
# USER
# ==============================

@app.route("/user")
def user():
    return render_template("index.html")


# ==============================
# DRIVER
# ==============================

@app.route("/driver")
def driver():
    return render_template("driver.html")


# ==============================
# ADMIN
# ==============================

@app.route("/admin")
def admin():
    return render_template("admin.html")


# ==============================
# HEALTH CHECK
# ==============================

@app.route("/health")
def health():
    return "RouteLive is running"


# ==============================
# START SERVER
# ==============================

if __name__ == "__main__":

    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )