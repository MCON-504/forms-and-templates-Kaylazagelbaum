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
    name_value = ""
    grade_value = ""

    if request.method == "POST":
        name = request.form.get("name", "").strip()
        grade = request.form.get("grade", "").strip()

        name_value = name
        grade_value = grade

        # TODO:
        # 1. Validate name
        # 2. Validate grade is number
        # 3. Validate grade range 0–100
        # 4. Add to students list as dictionary
        # 5. Redirect to /students

        if not name:
            error = "Name cannot be empty"
            return render_template("add.html", error=error, name=name_value, grade=grade_value)

        if not grade.isdigit():
            error = "Grade must be a number"
            return render_template("add.html", error=error, name=name_value, grade=grade_value)

        grade = int(grade)

        if grade < 0 or grade >100:
            error = "Grade must be between 0 and 100"
            return render_template("add.html", error=error, name=name_value, grade=grade_value)

        students.append({"name": name, "grade": grade})
        return redirect(url_for("display_students"))

    return render_template("add.html", error=error, name=name_value, grade=grade_value)


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

    if not students:
        return render_template("summary.html", empty=True)

    grades = [s["grade"] for s in students]

    total = len(grades)
    avg = sum(grades)/total
    highest = max(grades)
    lowest = min(grades)

    return render_template("summary.html", empty=False, total=total, avg=avg, highest=highest, lowest=lowest)



if __name__ == "__main__":
    app.run(host="localhost", port=5001, debug=True)
