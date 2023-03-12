from main import ma 


class RequestSchema(ma.Schema):
    class Meta:
        fields = ("id", "date", "status")

request_schema = RequestSchema()

requests_schema = RequestSchema(many=True)
