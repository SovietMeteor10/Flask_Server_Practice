from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def hello_world():
    return render_template("index.html")


@app.route("/submit", methods=["POST"])
def submit():
    input_name = request.form.get("name")
    input_age = request.form.get("age")
    input_degree = request.form.get("degree")
    return render_template(
        "hello.html", name=input_name, age=input_age, degree=input_degree
    )


@app.route("/query")
def get_query():
    q = request.args.get("q")
    return process_query(q)


def process_query(query_string):
    if query_string == "dinosaurs":
        return "Dinosaurs ruled the Earth 200 million years ago"
    if query_string == "asteroids":
        return "Unknown"
    if query_string == "What is your name?":
        return "Team_Wun"
    return "Query not recognised"
