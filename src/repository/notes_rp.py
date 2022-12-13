from src import db
from src.entity import models


def get_all():
    return db.session.query(models.Note).all()


def get_all_tags():
    return db.session.query(models.Tag).all()


def get_note_by_id(note_id):
    return db.session.query(models.Note).filter(models.Note.id == note_id).first()


def create_note(title, text, tags):
    tags_obj = []
    for tag in tags:
        tags_obj.append(db.session.query(models.Tag).filter(models.Tag.name == tag).first())
    note = models.Note(title=title, text=text, tags=tags_obj)
    db.session.add(note)
    db.session.commit()


def update_note(note_id, title, text, tags):
    tags_obj = []
    for tag in tags:
        tags_obj.append(db.session.query(models.Tag).filter(models.Tag.name == tag).first())
    db.session.query(models.Note).filter(models.Note.id == note_id).update(
        {"title": title, "text": text, "tags": tags_obj}
    )
    db.session.commit()


def delete(note_id):
    db.session.query(models.Note).filter(models.Note.id == note_id).delete()
    db.session.commit()


def add_tag(name):
    tag = models.Tag(name=name)
    db.session.add(tag)
    db.session.commit()

