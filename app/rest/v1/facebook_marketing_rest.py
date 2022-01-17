from facebook_business.exceptions import FacebookRequestError
from flask import request
from flask_restx import Namespace, Resource, cors, fields

from app.services.facebook_marketing_services import FacebookMarketing

facebook_marketing_ns = Namespace(
    "facebook_marketing",
    description="facebook marketing related operations",
    decorators=[cors.crossdomain(origin="*")],
)

audience_age_model = facebook_marketing_ns.model(
    "AudienceAge",
    {
        "min_age": fields.String(required=True, description="Creative link message"),
        "max_age": fields.String(required=True, description='Creative link"'),
    },
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
        "campaign_id": fields.String(required=True, description='The campaign id"'),
        "optimization_goal": fields.String(required=True, description='The optimization goal"'),
        "bid": fields.String(required=True, description='The bid"'),
        "audience_age": fields.Nested(model=audience_age_model, required=True, description='The target audience"'),
        "locations": fields.List(fields.String, required=True, description='The bid"'),
    },
)
create_ad_creative = facebook_marketing_ns.model(
    "CreateAdCreative",
    {
        "link_message": fields.String(required=True, description="Creative link message"),
        "link": fields.String(required=True, description='Creative link"'),
        "name": fields.String(required=True, description='Creative name"'),
        "image": fields.String(required=True, description='Creative image"'),
    },
)

create_ad = facebook_marketing_ns.model(
    "CreateAd",
    {
        "name": fields.String(required=True, description='Creative name"'),
        "creative_id": fields.String(required=True, description='Creative id"'),
        "adset_id": fields.String(required=True, description='Adset id"'),
    },
)


@facebook_marketing_ns.route("/create_campaign")
class CreatesCampaign(Resource):
    @facebook_marketing_ns.doc("creates campaign")
    @facebook_marketing_ns.expect(create_campaign)
    def post(self):
        args = request.get_json()
        # try:
        respone = FacebookMarketing.create_campaign(args["name"], args["objective"])
        return {"message": str(respone)}, 200, {"content-type": "application/json"}
        # except FacebookRequestError:
        #     return (
        #         {"message": "Facebook Request Error!"},
        #         500,
        #         {"content-type": "application/json"},
        #     )


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
                args["optimization_goal"],
                args["campaign_id"],
                args["bid"],
                args["audience_age"],
                args["locations"],
            )
            return {"message": str(respone)}, 200, {"content-type": "application/json"}
        except FacebookRequestError:
            return (
                {"message": "Facebook Request Error!"},
                500,
                {"content-type": "application/json"},
            )


@facebook_marketing_ns.route("/create_ad_creative")
class CreateAdCreatice(Resource):
    @facebook_marketing_ns.doc("creates ad creative")
    @facebook_marketing_ns.expect(create_ad_creative)
    def post(self):
        args = request.get_json()
        try:
            respone = FacebookMarketing.create_ad_creative(
                args["link_message"],
                args["link"],
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


@facebook_marketing_ns.route("/create_ad")
class CreateAdCreatice(Resource):
    @facebook_marketing_ns.doc("creates ad")
    @facebook_marketing_ns.expect(create_ad)
    def post(self):
        args = request.get_json()
        try:
            respone = FacebookMarketing.create_ad(args["name"], args["creative_id"], args["adset_id"])
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
        try:
            respone = FacebookMarketing.get_adset_insigth()
            return {"message": str(respone)}, 200, {"content-type": "application/json"}
        except FacebookRequestError:
            return (
                {"message": "Facebook Request Error!"},
                500,
                {"content-type": "application/json"},
            )


@facebook_marketing_ns.route("/get_preview")
class HealthCheck(Resource):
    @facebook_marketing_ns.doc("returns preview")
    def get(self):
        try:
            respone = FacebookMarketing.get_preview()
            return {"message": str(respone)}, 200, {"content-type": "application/json"}
        except FacebookRequestError:
            return (
                {"message": "Facebook Request Error!"},
                500,
                {"content-type": "application/json"},
            )
