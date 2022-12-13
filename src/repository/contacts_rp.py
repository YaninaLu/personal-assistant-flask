from src import db
from src.entity import models
import datetime


def get_all():
    return db.session.query(models.Contact).all()


def get_contact_by_id(cont_id):
    return db.session.query(models.Contact).filter(models.Contact.id == cont_id).first()


def create_contact(name, phone, birthday, email, address):
    birthday_dt = datetime.datetime.strptime(birthday, "%Y-%m-%d")
    contact = models.Contact(name=name, phone=phone, birthday=birthday_dt, email=email, address=address)
    db.session.add(contact)
    db.session.commit()


def update_contact(cont_id, name, phone, birthday, email, address):
    birthday_dt = datetime.datetime.strptime(birthday, "%Y-%m-%d")
    db.session.query(models.Contact).filter(models.Contact.id == cont_id).update(
        {"name": name, "phone": phone, "birthday": birthday_dt, "email": email, "address": address})
    db.session.commit()


def delete(contact_id):
    db.session.query(models.Contact).filter(models.Contact.id == contact_id).delete()
    db.session.commit()


