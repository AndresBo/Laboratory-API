from main import db


class Request(db.Model):
    __tablename__= "requests"

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date())
    status = db.Column(db.String())
    analyst_email = db.Column(db.String, db.ForeignKey("analysts.email"), nullable=False)
    analyser_name = db.Column(db.String, db.ForeignKey("analysers.name"), nullable=False)
    # requests_tests = db.relationship(
    #     "Request_test",
    #     backref="request",
    #     cascade="all, delete"
    # )
