from flask import Blueprint, jsonify, request, abort
from main import db
from models.tests import Test
from models.analysts import Analyst
from schemas.tests_schema import test_schema, tests_schema
from flask_jwt_extended import jwt_required, get_jwt_identity



tests = Blueprint("tests", __name__, url_prefix="/tests")


@tests.route("/", methods=["GET"])
def get_tests():
    tests_list = Test.query.all()
    result = tests_schema.dump(tests_list)
    return jsonify(result)


@tests.route("/", methods=["POST"])
@jwt_required()
def create_test():
    analyst_id = get_jwt_identity()

    analyst = Analyst.query.get(analyst_id)

    if not analyst:
        return abort(401, description="Invalid user")
    # only admins can create a new analyser
    if not analyst.admin:
        return abort(401, description="Unauthorized user, contact Admin")
    
    test_fields = test_schema.load(request.json)

    new_test = Test()
    new_test.name = test_fields["name"]

    db.session.add(new_test)
    db.session.commit()

    return jsonify(test_schema.dump(new_test))
