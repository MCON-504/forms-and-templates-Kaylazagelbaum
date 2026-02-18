# Homework: Student Grade Tracker (Flask + Jinja2)

## Objective

In this assignment, you will build a small Flask application that:

- Accepts student name and grade through a form
- Validates input
- Stores submissions in memory
- Displays students and grades in a table
- Adds comments based on grade
- Creates an additional endpoint to display summary statistics

This homework reinforces:

- Working with HTML forms
- GET vs POST
- request.form
- Validation
- Jinja conditionals
- Jinja loops
- Template inheritance
- Multiple routes

---

#  Project Requirements

You must implement:

## 1 Endpoint: `/add`

A form that allows the user to:

- Enter student name
- Enter numeric grade (0–100)
- Submit via POST

Validation rules:

- Name cannot be empty
- Grade must be a number
- Grade must be between 0 and 100

If invalid:
- Display error message
- Preserve user input

If valid:
- Add student to in-memory list
- Redirect to `/students`

---

## 2. Endpoint: `/students`

Display all students in a table:

| Name | Grade | Comment |

Comment rules:

- 90–100 → Excellent
- 70–89 → Good
- 60–69 → Passing
- Below 60 → Needs Improvement

You must:
- Use `{% for %}` loop
- Use conditionals in Jinja
- Use template inheritance

---

## 3. Endpoint: `/summary`

Create a new route that displays:

- Total number of students
- Average grade
- Highest grade
- Lowest grade

If no students exist:
- Display a friendly message

---

## Rules
---
- Must use POST for form submission
- Must validate input in Flask (not in template)
- Must use Jinja conditionals
- Must use Jinja loops
- Must use template inheritance
- Do NOT use a database (store in a Python list)

---

# 💡 Example Behavior

User submits:

Name: Alice  
Grade: 95

→ Redirect to `/students`

Table shows:

Alice | 95 | Excellent

---

# Bonus (Optional)

- Add flash messages
- Add delete student button
- Add sorting by grade
- Add styling

---

# Submission

Push your completed project to GitHub Classroom.
Application must run without errors.



