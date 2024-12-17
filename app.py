from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Change this to a random secret key

# Configure SQLite Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Initialize Flask-Login
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'  # Redirect to login page if not logged in

# User Model
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)

# Task Model
class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(200))
    due_date = db.Column(db.Date, nullable=True)
    priority = db.Column(db.String(10), default="Medium")
    completed = db.Column(db.Boolean, default=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))  # Link to User

    def __repr__(self):
        return f"<Task {self.id} - {self.title}>"

# Load user
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Route 1: Home Page - Display Tasks
@app.route('/')
@login_required
def home():
    tasks = Task.query.filter_by(user_id=current_user.id).order_by(Task.due_date).all()
    return render_template('index.html', tasks=tasks)

# Route 2: Render Add Task Page
@app.route('/add', methods=['GET'])
@login_required
def add_task_page():
    return render_template('add_task.html')

# Route 3: Add a Task (POST)
@app.route('/add', methods=['POST'])
@login_required
def add_task():
    title = request.form['title']
    description = request.form.get('description', '')
    due_date = request.form.get('due_date', None)
    priority = request.form.get('priority', 'Medium')

    if due_date:
        due_date = datetime.strptime(due_date, "%Y-%m-%d")

    new_task = Task(title=title, description=description, due_date=due_date, priority=priority, user_id=current_user.id)
    db.session.add(new_task)
    db.session.commit()

    return redirect(url_for('home'))

# Route 4: Render Login Page
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if user and check_password_hash(user.password, password):
            login_user(user)
            return redirect(url_for('home'))
        else:
            flash('Invalid username or password')
    return render_template('login.html')

# Route 5: Logout
@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

# Route 6: Render Registration Page
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        hashed_password = generate_password_hash(password)  # Use the default method

        new_user = User(username=username, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        flash('Registration successful! You can now log in.')
        return redirect(url_for('login'))
    return render_template('register.html')

# Route 7: Render Edit Task Page
@app.route('/edit/<int:task_id>', methods=['GET', 'POST'])
@login_required
def edit_task(task_id):
    task = Task.query.get_or_404(task_id)
    if request.method == 'POST':
        task.title = request.form['title']
        task.description = request.form.get('description', '')
        due_date = request.form.get('due_date', None)
        priority = request.form.get('priority', 'Medium')

        if due_date:
            task.due_date = datetime.strptime(due_date, "%Y-%m-%d")
        task.priority = priority

        db.session.commit()
        return redirect(url_for('home'))
    return render_template('edit_task.html', task=task)

# Route 8: Delete Task
@app.route('/delete/<int:task_id>', methods=['POST'])
@login_required
def delete_task(task_id):
    task = Task.query.get_or_404(task_id)
    db.session.delete(task)
    db.session.commit()
    return redirect(url_for('home'))

# Route 9: Complete Task
@app.route('/complete/<int:task_id>', methods=['POST'])
@login_required
def complete_task(task_id):
    task = Task.query.get_or_404(task_id)
    task.completed = True
    db.session.commit()
    return redirect(url_for('home'))

# Initialize Database
with app.app_context():
    db.create_all()  # Create database tables

if __name__ == '__main__':
    app.run(debug=True)