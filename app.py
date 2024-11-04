from flask import Flask, render_template, request
import re
import math
import requests

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


@app.route("/submit_gitname", methods=["POST"])
def submit_gitname():
    input_name = request.form.get("username")

    response = requests.get(f"https://api.github.com/users/{input_name}/repos")

    repo_data_list = []

    if response.status_code == 200:
        repos = response.json()

        for repo in repos:

            commits_response = requests.get(\
            repo["commits_url"].replace("{/sha}", ""))

            if commits_response.status_code == 200:
                commits = commits_response.json()

                if commits:

                    latest_commit = commits[0]
                    author_name = latest_commit["commit"]["author"]["name"]
                    commit_sha = latest_commit["sha"]
                    commit_message = latest_commit["commit"]["message"]

                    repo_data_list.append(
                        [
                            repo["full_name"],
                            repo["pushed_at"],
                            author_name,
                            commit_sha,
                            commit_message,
                        ]
                    )
            else:
                repo_data_list.append(
                    [
                        repo["full_name"],
                        repo["pushed_at"],
                        "No Author Listed",
                        "No Commit Hash Listed",
                        "No Commit Message Listed",
                    ]
                )

    return render_template(
        "git_hello.html", username=input_name, repo_data_list=repo_data_list
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
