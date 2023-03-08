from flask import Blueprint, jsonify, request, abort
from main import db
from models.analyser import Analyser
from models.analysts import Analyst
from schemas.analyser_schema import analyser_schema, analysers_schema
from flask_jwt_extended import jwt_required, get_jwt_identity


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
@jwt_required()
def delete_analyser(id):
    analyst_id = get_jwt_identity()

    analyst = Analyst.query.get(analyst_id)

    if not analyst:
        return abort(401, description="Invalid user")
    
    if not analyst.admin:
        return abort(401, description="Unauthorized user, contact Admin")
    
    analyser = Analyser.query.filter_by(id=id).first()
    
    if not Analyser:
        return abort(401, description="Analyser does not exists")
    
    db.session.delete(analyser)
    db.session.commit()
    return jsonify(analyser_schema.dump(analyser))

# !!!
# @analysers.route("/<int:id>/", methods=["PUT"])
# def modify_analyser():
#     return "analyser modified"
