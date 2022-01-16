from facebook_business.adobjects.adaccount import AdAccount

# from facebookads.adobjects.adset import AdSet
# from facebookads.adobjects.adimage import AdImage
# from facebookads.adobjects.targeting import Targeting
# from facebook_business.adobjects.adcreative import AdCreative
from facebook_business.api import FacebookAdsApi

from app.config import Config


class FacebookMarketing:
    access_token = Config.ACCESS_TOKEN
    app_secret = Config.APP_SECRET
    app_id = Config.APP_ID
    id = Config.AD_ACCOUNT_ID
    FacebookAdsApi.init(access_token=access_token)

    # @classmethod
    # def create_image_hash(cls, path):
    #     image = AdImage(parent_id=Config.AD_ACCOUNT_ID)
    #     image[AdImage.Field.filename] = path
    #     image.remote_create()
    #
    #     # Output image Hash
    #     return image[AdImage.Field.hash]

    @classmethod
    def create_campaign(cls, name, objective):
        params = {
            "name": name,
            "objective": objective,
            "status": "PAUSED",
            "special_ad_categories": [],
        }
        return AdAccount(id).create_campaign(fields=[], params=params)

    @classmethod
    def create_adset(cls, name, budget, campaign, bid, audience):
        pass
        # adset = AdSet(parent_id=Config.AD_ACCOUNT_ID)
        # adset.update(
        #     {
        #         AdSet.Field.name: name,
        #         AdSet.Field.campaign_id: campaign,
        #         AdSet.Field.daily_budget: budget,
        #         AdSet.Field.billing_event: AdSet.BillingEvent.impressions,
        #         AdSet.Field.optimization_goal: AdSet.OptimizationGoal.reach,
        #         AdSet.Field.bid_amount: bid,
        #         AdSet.Field.targeting: {
        #             Targeting.Field.geo_locations: {"countries": [audience],},
        #         },
        #     }
        # )
        # return adset.remote_create(params={"status": AdSet.Status.paused,})

    @classmethod
    def create_ad(cls, link_message, link, page_id, name, image):
        pass
        # image_hash = FacebookMarketing.create_image_hash(image)
        # params = {
        #     "name": name,
        #     "object_story_spec": {
        #         "page_id": page_id,
        #         "link_data": {
        #             "image_hash": image_hash,
        #             "link": link,
        #             "message": link_message,
        #         },
        #     },
        # }
        # return AdAccount(id).create_ad(fields=[], params=params)

    @classmethod
    def get_adset_insigth(cls):
        pass

    @classmethod
    def get_preview(cls):
        pass
        # params = {
        #     "ad_format": "DESKTOP_FEED_STANDARD",
        # }
        # return AdCreative(id).get_previews(fields=[], params=params,)
