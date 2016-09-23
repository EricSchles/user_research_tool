from app import app
from app import db
from app.models import Notes
from flask import render_template,request
from .tools import process_todos

@app.route("/create_note",methods=["GET","POST"])
def create_note():
    if request.method=='POST':
        note = request.form.get("note")
        db_note_obj = Notes(note,"eric")
        db.session.add(db_note_obj)
        db.session.commit()
    return render_template("create_note.html")

@app.route("/show_notes",methods=["GET","POST"])
def show_notes():
    notes = Notes.query.filter_by(username="eric").all()
    notes = [note.note.replace("\r","\n") for note in notes]
    return render_template("show_notes.html",notes=notes)

@app.route("/todo_list",methods=["GET","POST"])
def todo_list():
    notes = Notes.query.filter_by(username="eric").all()
    todos = process_todos(notes) #returns a list of lists
    return render_template("todo_list.html",todos=todos)
