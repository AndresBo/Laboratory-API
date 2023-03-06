from main import db
from flask import Blueprint
# bcyrpt
from models.analyser import Analyser


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

    db.session.commit()
    print("Table seeded")
