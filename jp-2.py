from flask import Flask, request

app = Flask(__name__)


@app.route("/")
def index():
    name = request.args.get("name")
    return "<h1>Hello, {}!</h1>".format(name)


if __name__ == "__main__":
    app.run()
