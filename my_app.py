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


@app.route("/", methods=["POST", "GET"])
def index():
    return render_template("index.html")


@app.route("/tarif_data", methods=["POST"])
def tarif():
    bd = Tariff.query.order_by(Tariff.Id).all()
    return render_template("tarif_data.html", bd=bd)


@app.route("/delivery_form", methods=["POST"])
def delivery_form():
    return render_template("/delivery_form.html")


@app.route("/delivery_data", methods=["POST"])
def delivery_data():
    id = request.form.get("id")
    phone = request.form.get("phone")
    print("До первого ")
    print(Delivery.query.filter_by(Id=int(id)).first())
    print(Delivery.query.filter_by(Number_of_destination=phone).first())
    if ((Delivery.query.filter_by(Id=int(id)).first()) and (Delivery.query.filter_by(Number_of_destination=phone).first())):#Если данные существуют
        print("после вервого")
        if (Delivery.query.filter_by(Id=int(id)).first()) == (Delivery.query.filter_by(Number_of_destination=phone).first()): #Если равны
            print("В основном")
            item = Delivery.query.filter_by(Id=int(id)).first()
            name = item.Number_of_destination
            time = item.Time_of_destination
            car = item.Number_of_car
            return render_template("/delivery_data.html", name=name, time=time, car=car)
        else:
            return render_template("/fall.html")
    else:
        return render_template("/fall.html")


app.run(host="0.0.0.0")