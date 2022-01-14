import logging
from flask_restx import Api

from flask import jsonify, Blueprint

_log = logging.getLogger(__name__)

api_v1 = Blueprint("api_v1", __name__, url_prefix="/v1")
api = Api(api_v1, doc="/docs", version="1.0", title="Pocket Strata API Version 1")

from app.rest.v1.health import health_ns

api.add_namespace(health_ns)
