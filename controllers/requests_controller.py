from flask import Blueprint, jsonify, request, abort
from main import db
from models.requests import Request
from schemas.request_schema import request_schema, requests_schema

requests = Blueprint('requests', __name__, url_prefix="/requests")


@requests.route("/", methods=["GET"])
def get_requests():
    requests_list = Request.query.all()
    result = requests_schema.dump(requests_list)
    return jsonify(result)
