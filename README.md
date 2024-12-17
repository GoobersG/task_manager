
# CS50x Final Project
# Task Manager

#### Video Demo:  <https://youtu.be/plANxbFGhEk>
#
#
## **DESCRIPTION**
A simple task management application built with Flask, allowing users to create, edit, delete, and complete tasks. This application uses Flask-SQLAlchemy for database management and Flask-Login for user authentication.

### **How the Program Works?**
The Task Manager application is a web-based tool built with Flask that allows users to manage their tasks efficiently. Users can register and log in to their accounts, where they can create, view, edit, and delete tasks. Each task can include details such as a title, description, due date, and priority level. The application uses a SQLite database to store user and task information securely. When a user interacts with the application, the Flask framework processes the requests, updates the database as needed, and renders the appropriate HTML pages for the user to see. This seamless interaction between the front end and back end allows users to manage their tasks easily and effectively.


## **Installing Libraries**
There is a requirements.txt file that has all the libraries used.

and simply can be installed by this pip command:

```pip install -r requirements.txt```

## Screenshots

![Register](https://i.ibb.co/nsykmkY/Screenshot-2024-12-17-at-22-42-43-Register.png)

![Login](https://i.ibb.co/NLJ0QQc/Screenshot-2024-12-17-at-22-42-59-Login.png)

![Dashboard](https://i.ibb.co/TK2Sd8x/Screenshot-2024-12-17-at-22-43-16-Task-Manager.png)

![Add Task](https://i.ibb.co/5F9BqRF/Screenshot-2024-12-17-at-22-43-29-Add-Task.png)

![Dashboard With Tasks](https://i.ibb.co/MCCSgMd/Screenshot-2024-12-17-at-22-45-07-Task-Manager.png)

![Edit Task](https://i.ibb.co/5cmy4Hg/Screenshot-2024-12-17-at-22-45-45-Edit-Task.png)

## Usage
Start the Application: Run the Flask application by executing Flask run in your terminal.

Register: Click on the "Register" link to create a new account. Fill in the required information and submit the form.

Log In: After registering, click on the "Login" link. Enter your username and password to access your account.

Create a Task: Once logged in, click on the "Add Task" button. Fill in the task details (title, description, due date, and priority) and submit the form.

View Tasks: Your tasks will be displayed on the dashboard. You can filter tasks by their status (all, completed, or pending).

Edit or Delete Tasks: To edit a task, click the "Edit" button next to the task. To delete a task, click the "Delete" button and confirm the action.

Log Out: When finished, click the "Logout" link to exit your account.

#
#
## __Libraries__

The Task Manager application utilizes the following libraries:

__Flask:__ A lightweight WSGI web application framework in Python that provides the tools and libraries needed to build web applications quickly and easily.

__Flask-SQLAlchemy:__ An extension for Flask that adds support for SQLAlchemy, allowing for easy database management and ORM (Object-Relational Mapping) capabilities.

__Flask-Login:__ A Flask extension that provides user session management, making it easy to handle user authentication and authorization.

__Flask-WTF:__ An extension that integrates Flask with WTForms, providing form handling and validation capabilities.

__Bootstrap:__ A front-end framework for developing responsive and mobile-first websites. It is used in this application for styling the user interface.

__Werkzeug:__ A comprehensive WSGI web application library that Flask is built on. It provides utilities for handling requests, responses, and more.

__Jinja2:__ A templating engine for Python that is used by Flask to render HTML templates dynamically.


## Authors

- [@GoobersG](https://github.com/GoobersG)

