from flask import Blueprint, jsonify, request
from main import db
from models.analyser import Analyser
from schemas.analyser_schema import analyser_schema, analysers_schema


analysers = Blueprint('analysers', __name__, url_prefix="/analysers")

@analysers.route("/", methods=["GET"])
def get_analysers():
    analysers_list = Analyser.query.all()
    result = analysers_schema.dump(analysers_list)
    return jsonify(result)


@analysers.route("/", methods=["POST"])
def create_analyser():
    analyser_fields = analyser_schema.load(request.json)
    
    new_analyser = Analyser()
    new_analyser.name = analyser_fields["name"]
    new_analyser.brand = analyser_fields["brand"]
    new_analyser.model = analyser_fields["model"]
    new_analyser.year = analyser_fields["year"]

    db.session.add(new_analyser)
    db.session.commit()
    
    return jsonify(analyser_schema.dump(new_analyser))


@analysers.route("/<int:id>/", methods=["DELETE"])
def delete_analyser():
    return "Analyser deleted"

# !!!
# @analysers.route("/<int:id>/", methods=["PUT"])
# def modify_analyser():
#     return "analyser modified"
