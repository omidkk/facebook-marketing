from facebook_business.exceptions import FacebookRequestError
from flask import request
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
        "objective": fields.String(required=True, description='The objective of objective"'),
    },
)

create_adset = facebook_marketing_ns.model(
    "CreateAdset",
    {
        "name": fields.String(required=True, description="The name"),
        "budget": fields.String(required=True, description='The daily budget"'),
        "campaign": fields.String(required=True, description='The campaign"'),
        "bid": fields.String(required=True, description='The bid"'),
        "audience": fields.String(required=True, description='The target audience"'),
    },
)
create_ad = facebook_marketing_ns.model(
    "CreateAd",
    {
        "link_message": fields.String(required=True, description="Creative link message"),
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
    def post(self):
        args = request.get_json()
        try:
            respone = FacebookMarketing.create_campaign(args["name"], args["objective"])
            return {"message": str(respone)}, 200, {"content-type": "application/json"}
        except FacebookRequestError:
            return (
                {"message": "Facebook Request Error!"},
                500,
                {"content-type": "application/json"},
            )


@facebook_marketing_ns.route("/create_adset")
class CreateAdset(Resource):
    @facebook_marketing_ns.doc("creates adset")
    @facebook_marketing_ns.expect(create_adset)
    def post(self):
        args = request.get_json()
        try:
            respone = FacebookMarketing.create_adset(
                args["name"],
                args["budget"],
                args["campaign"],
                args["bid"],
                args["audience"],
            )
            return {"message": str(respone)}, 200, {"content-type": "application/json"}
        except FacebookRequestError:
            return (
                {"message": "Facebook Request Error!"},
                500,
                {"content-type": "application/json"},
            )


@facebook_marketing_ns.route("/create_ad")
class CreateAd(Resource):
    @facebook_marketing_ns.doc("creates ad")
    @facebook_marketing_ns.expect(create_ad)
    def post(self):
        args = request.get_json()
        try:
            respone = FacebookMarketing.create_ad(
                args["link_message"],
                args["link"],
                args["page_id"],
                args["name"],
                args["image"],
            )
            return {"message": str(respone)}, 200, {"content-type": "application/json"}
        except FacebookRequestError:
            return (
                {"message": "Facebook Request Error!"},
                500,
                {"content-type": "application/json"},
            )


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
