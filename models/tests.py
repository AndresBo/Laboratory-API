from main import db


class Test(db.Model):
    __tablename__= "tests"

    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(), nullable=False, unique=True)
#     # requests_tests = db.relationship(
#     #     "Request_test",
#     #     backref="test",
#     #     cascade="all, delete"
#     # )
