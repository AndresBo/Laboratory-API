from flask import Blueprint, jsonify
from main import db
from models.tests import Test
from schemas.tests_schema import test_schema, tests_schema



tests = Blueprint("tests", __name__, url_prefix="/tests")


@tests.route("/", methods=["GET"])
def get_tests():
    tests_list = Test.query.all()
    result = tests_schema.dump(tests_list)
    return jsonify(result)
