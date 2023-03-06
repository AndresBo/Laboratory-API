from flask import Blueprint, jsonify, request, abort
from main import db
from main import bcrypt
from datetime import timedelta
from models.analysts import Analyst
from schemas.analyst_schema import analyst_schema, analysts_schema
from flask_jwt_extended import create_access_token


analysts = Blueprint('analysts', __name__, url_prefix="/analysts")


@analysts.route("/", methods=["GET"])
def get_analysts():
    analysts_list = Analyst.query.all()

    result = analysts_schema.dump(analysts_list)

    return jsonify(result)


@analysts.route("/register/", methods=["POST"])
def auth_register():
    analyst_fields = analyst_schema.load(request.json)

    analyst = Analyst.query.filter_by(email=analyst_fields["email"]).first()

    if analyst:
        return abort(400, description="Email already registered")
    
    analyst = Analyst()
    analyst.email = analyst_fields["email"]
    analyst.password = bcrypt.generate_password_hash(analyst_fields["password"]).decode("utf-8") 
    analyst.admin = False

    db.session.add(analyst)
    db.session.commit()

    expiry = timedelta(days=1)

    access_token = create_access_token(identity=str(analyst.id), expires_delta=expiry)

    return jsonify({"analyst":analyst.email, "token": access_token})
