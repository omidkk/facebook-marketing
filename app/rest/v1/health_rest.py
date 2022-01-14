from flask_restx import Namespace, Resource, cors

health_ns = Namespace(
    "health",
    description="health related operations",
    decorators=[cors.crossdomain(origin="*")],
)


@health_ns.route("/")
class HealthCheck(Resource):
    @health_ns.doc("return a health check")
    def get(self):
        return (
            {"message": "Welcome to OUNASS facebook marketing app"},
            200,
            {"content-type": "application/json"},
        )
