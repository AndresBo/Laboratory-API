from main import db
from main import bcrypt
from flask import Blueprint

from models.analyser import Analyser
from models.analysts import Analyst


db_commands = Blueprint("db", __name__)


@db_commands.cli.command("create")
def create_db():
    db.create_all()
    print("Tables created")


@db_commands.cli.command("drop")
def drop_db():
    db.drop_all()
    print("Tables dropped")


@db_commands.cli.command("seed")
def seed_db():
    analyser1 = Analyser(
        name = "ICP1",
        brand = "Thermo",
        model = "2000",
        year = "2012",
    )
    db.session.add(analyser1)

    admin_user = Analyst(
        email = "admin@email.com",
        password = bcrypt.generate_password_hash("password123").decode("utf-8"),
        admin = True
    )
    db.session.add(admin_user)

    analyst1 = Analyst(
        email = "analyst1@email.com",
        password = bcrypt.generate_password_hash("123456").decode("utf-8"),
    )
    db.session.add(analyst1)

    db.session.commit()
    print("Table seeded")
