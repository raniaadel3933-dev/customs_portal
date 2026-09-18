from flask import Blueprint, render_template, request, redirect, session
from werkzeug.security import check_password_hash
from app.db import get_db

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        username = request.form["username"]
        password = request.form["password"]

        conn = get_db()
        cur = conn.cursor(dictionary=True)

        cur.execute("""
            SELECT * FROM users
            WHERE username=%s AND status='active'
        """, (username,))

        user = cur.fetchone()

        cur.close()
        conn.close()

        if user and check_password_hash(user["password_hash"], password):
            session["user"] = user["username"]
            return redirect("/dashboard")

        return render_template("auth/login.html", error="بيانات غير صحيحة")

    return render_template("auth/login.html")