from flask import Blueprint, jsonify, request
from main import db
from models.analyser import Analyser


analysers = Blueprint('analysers', __name__, url_prefix="/analysers")

@analysers.route("/", methods=["GET"])
def get_analysers():
    #analysers_list = Analyser.query.all()
    return "List of analysers retrieved"


@analysers.route("/", methods=["POST"])
def new_analyser():
    return "added new analyser"


@analysers.route("/<int:id>/", methods=["DELETE"])
def delete_analyser():
    return "Analyser deleted"

# !!!
# @analysers.route("/<int:id>/", methods=["PUT"])
# def modify_analyser():
#     return "analyser modified"
