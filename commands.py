from main import db
from main import bcrypt
from flask import Blueprint

from models.analyser import Analyser
from models.analysts import Analyst
from models.tests import Test
from models.requests import Request
from models.requests_tests import Request_test


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

    analyser2 = Analyser(
        name = "ICP2",
        brand = "Thermo",
        model = "3000",
        year = "2013"
    )
    db.session.add(analyser2)
    
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

    test1 = Test(
        name = "zinc"
    )
    db.session.add(test1)

    test2 = Test(
        name = "copper"
    )
    db.session.add(test2)

    test3 = Test(
        name = "lead"
    )
    db.session.add(test3)

    test4 = Test(
        name = "mercury"
    )
    db.session.add(test4)

    db.session.commit()

    request1 = Request(
        date = "12/10/2020",
        status = "processing",
        analyst_email = analyst1.email,
        analyser_name = analyser1.name

    )
    db.session.add(request1)

    request2 = Request(
        date = "12/11/2020",
        status = "finalized",
        analyst_email = admin_user.email,
        analyser_name = analyser2.name
    )
    db.session.add(request2)


    request_test1 = Request_test(
        request_id = request1.id,
        test_name = test1.name
    )
    db.session.add(request_test1)

    request_test2 = Request_test(
        request_id = request1.id,
        test_name = test2.name
    )
    db.session.add(request_test2)

    request_test3 = Request_test(
        request_id = request1.id,
        test_name = test3.name
    )
    db.session.add(request_test3)

    request_test4 = Request_test(
        request_id = request2.id,
        test_name = test4.name
    )
    db.session.add(request_test4)


    db.session.commit()
    print("Table seeded")
