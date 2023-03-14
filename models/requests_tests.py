from main import db


class Request_test(db.Model):
    __tablename__= "requests_tests"

    id = db.Column(db.Integer, primary_key=True)
    # two foreing keys for many-to-many relationship: one request can have many tests,
    # one test can belong to many requests.
    request_id = db.Column(db.Integer, db.ForeignKey("requests.id"), nullable=False)
    test_name = db.Column(db.String, db.ForeignKey("tests.name"), nullable=False)
