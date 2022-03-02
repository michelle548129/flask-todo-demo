from flask import redirect, url_for
from application import app, db
from application.models import Todo, Project
from datetime import date, timedelta

@app.route('/')
def home():
    return f"{Todo.query.count()} todos: " + '<br>'.join(str(t) + " "+ str(t.project) for t in Todo.query.all())

@app.route('/search=<keyword>')
def search(keyword):
    data = db.session.execute(f"SELECT * FROM todo WHERE desc LIKE '%{keyword}%'")
    return '<br>'.join([str(res) for res in data])


@app.route('/done')
def done():
    return '<br>'.join(str(t) for t in Todo.query.filter_by(status='done').order_by(Todo.title.desc()).all())

@app.route('/create/<int:pnum>/<title>/<desc>')
def create(pnum, title, desc):
    todo = Todo(title=title, desc=desc, status='todo', proj_id = pnum)
    db.session.add(todo)
    db.session.commit()
    return redirect(url_for('home'))

@app.route('/create-proj/<name>')
def create_project(name):
    new_proj = Project(project_name = name, due_date = date.today() + timedelta(30))
    db.session.add(new_proj)
    db.session.commit()
    return redirect(url_for('home'))

@app.route('/update/<int:i>/<newstatus>')
@app.route('/update/<int:i>/<newtask>/<newstatus>')
def update(i, newstatus, newtask = None): #defining multiple routes and setting default
    todo = Todo.query.get(i)
    if newtask:
        todos.title = newtask
    todo.status = newstatus
    db.session.commit()
    return redirect(url_for('home'))

@app.route('/delete/<int:i>')
def delete(i):
    todo = Todo.query.get(i)
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for('home'))

