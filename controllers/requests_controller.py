from flask import Blueprint, jsonify, request, abort
from main import db
from models.requests import Request

requests = Blueprint('requests', __name__, url_prefix="/requests")


@request.route("/", methods=["GET"])
def get_requests():
    requests_list = Request.query.all()
    result = 
