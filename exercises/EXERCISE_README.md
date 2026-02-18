# Jinja2 and Forms practice

In this project you will practice using Jinja2 templates and handling forms in a web application. 
The exercises will involve creating a simple web application that allows users to submit a form 
and display the submitted data on a new page.

## Exercise: Basic Jinja2 Template

Repo structure:
```arduino
forms_and_templates/
│
├── app.py - solutions to the flask_intro exercises
└── test_app.py - tests for the flask_intro exercises
└── demo.py - demo code for working  with Ninja templates
└── templates/
├── base.html
├── home.html
├── students.html
├── grades.html
└── form.html
└── ninja_exercise.py - exercise for working with Ninja templates

```
## Ninja Templates Exercise
### Part 1 – Variable Interpolation

Open home.html.

Modify the template so that it displays:

```arduino
Welcome, <name>!
Today is <current date>
```
You must:

 - Use {{ }} for variables
 - Pass variables from Flask to the template

### Part 2 – Conditionals

In grades.html:

Display a message depending on score:
```arduino
90+ → "Excellent"
70–89 → "Good Job"
Below 70 → "Needs Improvement"
```
You must:

- Use {% if %}
- Use {% elif %}
- Use {% else %}
 
### Part 3 – Loops

In students.html:

Display a list of students dynamically.

Requirements:

 - Use {% for %}
 - Display index number using loop.index
 - Show total number of students using |length

### Part 4 – Filters

In home.html:

Display:

 - Name in uppercase
 - Name in title case
 - A number rounded to 2 decimal places

Use following filters:

 - |upper
 - |title
 - |round

### Part 5 – Template Inheritance

You must:

 - Create a base.html
 - Add a navigation bar
 - Use {% block content %}
 - Make all other templates extend base.html

### Part 6 – Working with Forms

In form.html:

- Create a form that:
- Displays an error in red is error is present
- Accepts a username
- Uses POST method
- Displays an error if empty
- Displays a welcome message if valid

In ninja_exercise.py:

- Handle GET and POST
- Use request.form
- Validate input

