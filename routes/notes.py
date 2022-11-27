from flask_login import login_required, current_user
from flask import request, redirect, flash
from app import app
from forms.note_form import NoteForm
from models import Session, Note


@app.route('/notes', methods=['GET'])
@login_required
def get_notes():
    with Session() as session:
        return session.query(Note).all()


@app.route('/notes', methods=['POST'])
@login_required
def add_note():
    form = NoteForm(request.form)

    if not form.validate():
        return form.errors

    with Session(expire_on_commit=False) as session:
        note = Note()
        note.title = form.title.data
        note.text = form.text.data
        note.private = form.is_private.data
        note.user_id = current_user.id
        session.add(note)
        session.commit()

    flash('Note created', 'success')
    return redirect('/home')
