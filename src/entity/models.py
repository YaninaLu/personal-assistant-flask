from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime

from src import db


notes_tags_conn = db.Table(
    "notes_to_tags",
    db.Column("id", db.Integer, primary_key=True),
    db.Column("note", db.Integer, ForeignKey("notes.id", ondelete="CASCADE")),
    db.Column("tag", db.Integer, ForeignKey("tags.id", ondelete="CASCADE")),
)


class Contact(db.Model):
    __tablename__ = "contacts"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False, unique=True)
    birthday = db.Column(db.DateTime)
    email = db.Column(db.String(50), unique=True)
    phone = db.Column(db.String(20), unique=True)
    address = db.Column(db.String(70))


class Note(db.Model):
    __tablename__ = "notes"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(20), nullable=False, unique=True)
    created_on = db.Column(db.DateTime, default=datetime.now())
    text = db.Column(db.String(500), nullable=False)
    tags = relationship("Tag", secondary=notes_tags_conn, backref="notes")


class Tag(db.Model):
    __tablename__ = "tags"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(25), nullable=False)
