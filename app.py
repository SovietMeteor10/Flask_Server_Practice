from flask import Flask, render_template, request
import re

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
    if "plus" in query_string:
        numbers = re.findall(r"\d+", query_string)
        return str(sum([int(num) for num in numbers]))
    if "multiplied" in query_string:
        numbers = re.findall(r"\d+", query_string)
        mul = 1
        return str([mul * int(num) for num in numbers])
    return "Query not recognised"
