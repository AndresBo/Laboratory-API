from main import db


class Analyst(db.Model):
    __tablename__= "analysts"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(), nullable=False, unique=True)
    password = db.Column(db.String(), nullable=False)
    # requests = db.relationship(
    #     "Request",
    #     backref="analyst",
    #     cascade="all, delete"
    # )
    admin = db.Column(db.Boolean(), default=False)
    
