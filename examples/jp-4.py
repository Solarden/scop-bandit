from flask import Flask, request
import sqlite3
from decouple import config

app = Flask(__name__)
app.config["SECRET_KEY"] = config("SECRET_KEY")


@app.route("/users")
def get_users():
    name = request.args.get("name", None)
    conn = sqlite3.connect("users.db")
    c = conn.cursor()
    if name:
        c.execute("SELECT * FROM users WHERE name = ?", (name,))
    else:
        c.execute("SELECT * FROM users")
    results = c.fetchall()
    conn.close()
    return str(results)


if __name__ == "__main__":
    app.run(debug=False)
