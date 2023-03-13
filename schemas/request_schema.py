from main import ma 


class RequestSchema(ma.Schema):
    class Meta:
        fields = ("id", "date", "status", "analyst_email", "analyser_name")

request_schema = RequestSchema()

requests_schema = RequestSchema(many=True)
