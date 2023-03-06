from flask import Blueprint, jsonify, request, abort
from main import db
from models.analysts import Analyst
from schemas.analyst_schema import analyst_schema, analysts_schema
from flask_jwt_extended import jwt_required, get_jwt_identity


analysts = Blueprint('analysts', __name__, url_prefix="/analysts")


@analysts.route("/", methods=["GET"])
def get_analysts():
    analysts_list = Analyst.query.all()

    result = analysts_schema.dump(analysts_list)

    return jsonify(result)
