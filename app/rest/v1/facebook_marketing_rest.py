from flask_restx import Namespace, Resource, cors
from app.services.facebook_marketing_services import FacebookMarketing

facebook_marketing_ns = Namespace(
    "facebook marketing",
    description="facebook marketing related operations",
    decorators=[cors.crossdomain(origin="*")],
)


@facebook_marketing_ns.route("/create_campaign")
class HealthCheck(Resource):
    @facebook_marketing_ns.doc("creates campaign")
    def post(self):
        pass


@facebook_marketing_ns.route("/create_adset")
class HealthCheck(Resource):
    @facebook_marketing_ns.doc("creates adset")
    def post(self):
        pass


@facebook_marketing_ns.route("/create_ad")
class HealthCheck(Resource):
    @facebook_marketing_ns.doc("creates ad")
    def post(self):
        pass


@facebook_marketing_ns.route("/get_adset_insigth")
class HealthCheck(Resource):
    @facebook_marketing_ns.doc("returns a adset insigth")
    def get(self):
        pass


@facebook_marketing_ns.route("/get_preview")
class HealthCheck(Resource):
    @facebook_marketing_ns.doc("returns preview")
    def get(self):
        pass
