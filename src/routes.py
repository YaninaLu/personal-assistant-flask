from flask import render_template, request, redirect, flash
from marshmallow import ValidationError
from sqlalchemy.exc import IntegrityError

from . import app
from src.repository import contacts_rp, notes_rp
from src.libs.validation import ContactSchema, NoteSchema


@app.route('/', strict_slashes=False)
def index():
    return render_template('index.html')


@app.route('/contacts', strict_slashes=False)
def contacts_page():
    contacts = contacts_rp.get_all()
    return render_template('contacts.html', contacts=contacts)


@app.route('/notes', strict_slashes=False)
def notes_page():
    notes = notes_rp.get_all()
    return render_template('notes.html', notes=notes)


@app.route('/contact_add', strict_slashes=False, methods=['GET', 'POST'])
def add_contact():
    if request.method == 'POST':
        try:
            ContactSchema().load(request.form)
        except ValidationError as err:
            return render_template('contact_add.html', messages=err.messages)

        name = request.form.get('name')
        phone = request.form.get('phone')
        birthday = request.form.get('birthday')
        email = request.form.get('email')
        address = request.form.get('address')

        try:
            contacts_rp.create_contact(name, phone, birthday, email, address)
            flash('Success!')
            return redirect('/contacts')
        except IntegrityError as err:
            print(err)
            return render_template('contact_add.html', messages={'error': f'Something went wrong: {err}!'})

    return render_template('contact_add.html')


@app.route('/contact_update/<cont_id>', strict_slashes=False, methods=['GET', 'POST'])
def update_contact(cont_id):
    if request.method == 'POST':
        try:
            ContactSchema().load(request.form)
        except ValidationError as err:
            return render_template('contact_update.html', messages=err.messages)

        name = request.form.get('name')
        phone = request.form.get('phone')
        birthday = request.form.get('birthday')
        email = request.form.get('email')
        address = request.form.get('address')

        try:
            contacts_rp.update_contact(cont_id, name, phone, birthday, email, address)
            flash('Success!')
            return redirect('/contacts')
        except IntegrityError as err:
            print(err)
            return render_template('contact_update.html', messages={'error': f'Something went wrong: {err}!'})

    return render_template('contact_update.html', contact=contacts_rp.get_contact_by_id(cont_id))


@app.route('/note_add', strict_slashes=False, methods=['GET', 'POST'])
def add_note():
    if request.method == 'POST':
        try:
            NoteSchema().load(request.form)
        except ValidationError as err:
            return render_template('note_add.html', messages=err.messages)

        title = request.form.get('title')
        text = request.form.get('text')
        tags = request.form.getlist('tags')

        try:
            notes_rp.create_note(title, text, tags)
            flash('Success!')
            return redirect('/notes')
        except IntegrityError as err:
            print(err)
            return render_template('note_add.html', messages={'error': f'Something went wrong: {err}!'})

    return render_template('note_add.html', tags=notes_rp.get_all_tags())


@app.route('/tag_add', strict_slashes=False, methods=['GET', 'POST'])
def add_tag():
    if request.method == "POST":
        name = request.form.get("name")
        notes_rp.add_tag(name)
        flash('Success!')
        return redirect('/notes')

    return render_template('tag_add.html')


@app.route('/note_update/<note_id>', methods=['GET', 'POST'], strict_slashes=False)
def update_note(note_id):
    if request.method == 'POST':
        try:
            NoteSchema().load(request.form)
        except ValidationError as err:
            return render_template('note_add.html', messages=err.messages)

        title = request.form.get('title')
        text = request.form.get('text')
        tags = request.form.getlist('tags')

        try:
            notes_rp.update_note(note_id, title, text, tags)
            flash('Success!')
            return redirect('/notes')
        except IntegrityError as err:
            print(err)
            return render_template('note_add.html', messages={'error': f'Something went wrong: {err}!'})

    return render_template('note_update.html', note=notes_rp.get_note_by_id(note_id), tags=notes_rp.get_all_tags())


@app.route('/delete_note/<note_id>', strict_slashes=False)
def delete_note(note_id):
    notes_rp.delete(note_id)
    flash('Deleted successfully!')
    return redirect('/notes')


@app.route('/delete_contact/<contact_id>', strict_slashes=False)
def delete_contact(contact_id):
    contacts_rp.delete(contact_id)
    flash('Deleted successfully!')
    return redirect('/contacts')
