from flask import Blueprint, jsonify, request, abort
from main import db
from models.requests import Request
from models.analysts import Analyst
from schemas.request_schema import request_schema, requests_schema
from flask_jwt_extended import jwt_required, get_jwt_identity

requests = Blueprint('requests', __name__, url_prefix="/requests")


@requests.route("/", methods=["GET"])
def get_requests():
    requests_list = Request.query.all()
    result = requests_schema.dump(requests_list)
    return jsonify(result)


@requests.route("/", methods=['POST'])
@jwt_required()
def create_request():
    analyst_id = get_jwt_identity()

    analyst = Analyst.query.get(analyst_id)

    if not analyst:
        return abort(401, description="Invalid user")

    
    request_fields = request_schema.load(request.json)

    new_request = Request()
    new_request.date = request_fields["date"]
    new_request.status = request_fields["status"]
    new_request.analyst_email = analyst.email
    new_request.analyser_name = request_fields["analyser_name"]
    #new_request.test = request_fields

    db.session.add(new_request)
    db.session.commit()

    return jsonify(request_schema.dump(new_request))


@requests.route("/<int:id>/", methods=["DELETE"])
@jwt_required()
def delete_request(id):
    analyst_id = get_jwt_identity()

    analyst = Analyst.query.get(analyst_id)

    if not analyst:
        return abort(401, description="Invalid user")
    
    request = Request.query.filter_by(id=id).first()

    if not request:
        return abort(400, description="Request does not exists")
    
    db.session.delete(request)
    db.session.commit()

    return jsonify(request_schema.dump(request))


@requests.route("/<int:id>/", methods=["PUT"])
@jwt_required()
def update_request(id):
    request_fields = request_schema.load(request.json)


    analyst_id = get_jwt_identity()

    analyst = Analyst.query.get(analyst_id)

    if not analyst:
        return abort(401, description="Invalid user")
    
       
    to_update_request = Request.query.filter_by(id=id).first()

    if not to_update_request:
        return abort(400, description="Request does not exists")
    
    #update request
    to_update_request.status = request_fields["status"]

    db.session.commit()

    return jsonify(request_schema.dump(to_update_request))
    


    

    
