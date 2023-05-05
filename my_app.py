from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:secret@192.168.31.10/delivery_service"
db.init_app(app)


class Tariff(db.Model):
    Id = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(64), nullable=False)
    Max_mass = db.Column(db.String(64), nullable=False)
    Time_of_delivery = db.Column(db.String(64), nullable=False)


class Delivery(db.Model):
    Id = db.Column(db.Integer, primary_key=True)
    Address = db.Column(db.String(64), nullable=False)
    Destination = db.Column(db.String(64), nullable=False)
    Number_of_destination = db.Column(db.String(64), nullable=False)
    Time_of_destination = db.Column(db.String(64), nullable=False)
    Number_of_car = db.Column(db.String(64), nullable=False)
    Courier = db.Column(db.String(64), nullable=False)


with app.app_context():
    db.create_all()
