from main import ma
from marshmallow.validate import Length
from models.analysts import Analyst
#from marshmallow.exceptions import ValidationError
#from pprint import pprint


class AnalystSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Analyst

    password = ma.String(validate=Length(min=6))
    
  
analyst_schema = AnalystSchema()
analysts_schema = AnalystSchema(many=True)
