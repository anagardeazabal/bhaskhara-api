from flask_restplus import fields
from service.restplus import api

INPUT_MAIN_SERVICE = api.model(
  'input_main_service', {
    'a': fields.List(fields.Integer(), required=True), 
    'b': fields.List(fields.Integer(), required=True),
    'c': fields.List(fields.Integer(), required=True)})
