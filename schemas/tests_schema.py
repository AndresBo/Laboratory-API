from main import ma 


class TestSchema(ma.Schema):
    class Meta:
        fields = ("id", "name")


test_schema = TestSchema()
tests_schema = TestSchema(many=True)
