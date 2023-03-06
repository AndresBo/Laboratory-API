# from main import db


# class Request(db.Model):
#     __tablename__= "requests"

#     id = db.Column(db.Integer, primary_key=True)
#     date = db.Column(db.Date())
#     status = db.Column(db.String())
#     # analyst_id = db.Column(db.Integer, db.ForeignKey("analysts.id"), nullable=False)
#     # analyser_id = db.Column(db.Integer, db.ForeignKey("analysers.id"), nullable=False)
#     # requests_tests = db.relationship(
#     #     "Request_test",
#     #     backref="request",
#     #     cascade="all, delete"
#     # )
