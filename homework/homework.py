from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# In-memory storage
students = []


@app.route("/")
def home():
    return redirect(url_for("add_student"))


# ---------------------------------
# TODO: IMPLEMENT THIS ROUTE
# ---------------------------------
@app.route("/add", methods=["GET", "POST"])
def add_student():
    error = None

    if request.method == "POST":
        name = request.form.get("name")
        grade = request.form.get("grade")

        # TODO:
        # 1. Validate name
        # 2. Validate grade is number
        # 3. Validate grade range 0–100
        # 4. Add to students list as dictionary
        # 5. Redirect to /students

        pass

    return render_template("add.html", error=error)


# ---------------------------------
# TODO: IMPLEMENT DISPLAY
# ---------------------------------
@app.route("/students")
def display_students():
    return render_template("students.html", students=students)


# ---------------------------------
# TODO: IMPLEMENT SUMMARY
# ---------------------------------
@app.route("/summary")
def summary():
    # TODO:
    # Calculate:
    # - total students
    # - average grade
    # - highest grade
    # - lowest grade

    return render_template("summary.html")


if __name__ == "__main__":
    app.run(host="localhost", port=5001, debug=True)
