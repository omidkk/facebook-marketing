from flask_restx import Namespace, Resource, cors, fields
from app.services.facebook_marketing_services import FacebookMarketing

facebook_marketing_ns = Namespace(
    "facebook_marketing",
    description="facebook marketing related operations",
    decorators=[cors.crossdomain(origin="*")],
)
create_campaign = facebook_marketing_ns.model(
    "CreateCampaign",
    {
        "name": fields.String(required=True, description="The name of campaign"),
        "objective": fields.String(
            required=True, description='The objective of objective"'
        ),
    },
)

create_adset = facebook_marketing_ns.model(
    "CreateAdset",
    {
        "name": fields.String(required=True, description="The name"),
        "budget": fields.String(required=True, description='The daily budget"'),
        "campaign": fields.String(required=True, description='The campaign"'),
        "bid": fields.String(required=True, description='The bid"'),
        "billing_event": fields.String(
            required=True, description='Chose the suitable billing event"'
        ),
        "optimization_goal": fields.String(
            required=True, description='Chose the right optimization goal"'
        ),
        "audience": fields.String(required=True, description='The target audience"'),
    },
)
create_ad = facebook_marketing_ns.model(
    "CreateAd",
    {
        "link_message": fields.String(
            required=True, description="Creative link message"
        ),
        "link": fields.String(required=True, description='Creative link"'),
        "page_id": fields.String(required=True, description='Page id"'),
        "name": fields.String(required=True, description='Creative name"'),
        "image": fields.String(required=True, description='Creative image"'),
    },
)


@facebook_marketing_ns.route("/create_campaign")
class CreatesCampaign(Resource):
    @facebook_marketing_ns.doc("creates campaign")
    @facebook_marketing_ns.expect(create_campaign)
    def post(self, name, objective):
        pass


@facebook_marketing_ns.route("/create_adset")
class CreateAdset(Resource):
    @facebook_marketing_ns.doc("creates adset")
    @facebook_marketing_ns.expect(create_adset)
    def post(
        self, name, budget, campaign, bid, billing_event, optimization_goal, audience
    ):
        pass


@facebook_marketing_ns.route("/create_ad")
class CreateAd(Resource):
    @facebook_marketing_ns.doc("creates ad")
    @facebook_marketing_ns.expect(create_ad)
    def post(self, link_message, link, page_id, name, image):
        pass


@facebook_marketing_ns.route("/get_adset_insigth")
class GetAdsetInsigth(Resource):
    @facebook_marketing_ns.doc("returns a adset insigth")
    def get(self):
        pass


@facebook_marketing_ns.route("/get_preview")
class HealthCheck(Resource):
    @facebook_marketing_ns.doc("returns preview")
    def get(self):
        pass
