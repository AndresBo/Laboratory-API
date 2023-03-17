from flask import Blueprint, jsonify, request, abort
from main import db
from models.requests import Request
from models.analysts import Analyst
from models.analyser import Analyser
from models.tests import Test
from models.requests_tests import Request_test
from schemas.request_schema import request_schema, requests_schema
from schemas.request_test_schema import request_test_schema
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


@requests.route("/addtest/<int:id>/", methods=["POST"])
@jwt_required()
def add_test(id):
    test_fields = request_test_schema.load(request.json)

    #verify analyser_id exists:
    analyser = Analyser.query.filter_by(id=id).first()

    if not analyser:
        return abort(400, description="There is no Analyser by that ID number, please enter a valid Analyser ID")
    
    #verify test is a valid test:
    input_test = test_fields["test_name"]
    test = Test.query.filter_by(name=input_test).first()

    if not test:
        return abort(400, description="There is no test by that name, enter a valid test")

    

    new_test = Request_test()
    new_test.request_id = id
    new_test.test_name = test_fields["test_name"]

    db.session.add(new_test)
    db.session.commit()

    return jsonify(request_test_schema.dump(new_test))

    


    

    
