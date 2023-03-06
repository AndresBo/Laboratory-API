from main import ma
from marshmallow.validate import Length
from models.analysts import Analyst


class AnalystSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Analyst
