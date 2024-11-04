from flask import Flask, render_template, request
import re
import math

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


def submit_gitname():
    input_name = request.form.get("name")
    return render_template("git_hello.html", username=input_name)


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
    if "minus" in query_string:
        numbers = re.findall(r"\d+", query_string)
        vals = [int(num) for num in numbers]
        return str((vals[0] - vals[1]))

    if "multiplied" in query_string:
        numbers = re.findall(r"\d+", query_string)
        mul_vals = [int(num) for num in numbers]
        return str(math.prod(mul_vals))

    if "is the largest:" in query_string:
        numbers = re.findall(r"\d+", query_string)
        return str(max([int(num) for num in numbers]))

    if "is both a square and a cube:" in query_string:

        numbers = re.findall(r"\d+", query_string)
        mul_vals = [int(num) for num in numbers]
        val = [
            i
            for i in mul_vals
            if (pow(i, 1 / 2).is_integer() and pow(i, 1 / 3).is_integer())
        ]
        return ", ".join(map(str, val))

    if "are primes" in query_string:
        numbers = re.findall(r"\d+", query_string)
        vals = [int(num) for num in numbers]
        primes = []
        for i in vals:
            if i < 2:
                continue
            is_prime = True
            for j in range(2, math.isqrt(i) + 1):
                if i % j == 0:
                    is_prime = False
                    break
            if is_prime:
                primes.append(i)

        return ", ".join(map(str, primes))

    if "power" in query_string:
        numbers = re.findall(r"\d+", query_string)
        vals = [int(num) for num in numbers]
        return str(vals[0] ** vals[1])

    return "Query not recognised"
