from main import ma


class RequestTestSchema(ma.Schema):
    class Meta:
        fields = ("id","request_id", "test_name")

request_test_schema = RequestTestSchema()

requests_tests_schema = RequestTestSchema(many=True)
