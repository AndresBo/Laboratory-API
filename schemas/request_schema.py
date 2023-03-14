from main import ma 
from marshmallow import fields


class RequestSchema(ma.Schema):
    class Meta:
        fields = ("id", "date", "status", "analyst_email", "analyser_name", "test")
    # nested schema to show tests that belong to request
    test = fields.List(fields.Nested("RequestTestSchema", only=("test_name",)))

request_schema = RequestSchema()

requests_schema = RequestSchema(many=True)
