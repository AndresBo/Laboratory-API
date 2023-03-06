from main import ma 


class AnalyserSchema(ma.Schema):
    class Meta:
        fields = ("id", "name", "brand", "model", "year")

analyser_schema = AnalyserSchema()

analysers_schema = AnalyserSchema(many=True)
