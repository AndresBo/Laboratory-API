from main import db


class Analyser(db.Model):
    __tablename__= "analysers"

    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(), nullable=False, unique=True)
    brand = db.Column(db.String(), nullable=False)
    model = db.Column(db.String(), nullable=False)
    year = db.Column(db.String(), nullable=False)
    requests = db.relationship(
        "Request",
        backref="analyser",
        cascade="all, delete"
    )
