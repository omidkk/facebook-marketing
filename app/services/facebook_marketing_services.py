import os
import uuid
from datetime import datetime
from datetime import timedelta

import requests
from facebook_business.adobjects.adaccount import AdAccount

from facebook_business.api import FacebookAdsApi

from app.config import Config


class FacebookMarketing:

    @classmethod
    def create_image_hash(cls, path):
        FacebookAdsApi.init(access_token=Config.ACCESS_TOKEN)
        id = Config.AD_ACCOUNT_ID

        img_data = requests.get(path).content
        file_name = uuid.uuid4()
        with open(f'temp/{file_name}.jpg', 'wb') as handler:
            handler.write(img_data)

        params = {
            "filename": f'temp/{file_name}.jpg'
        }
        # Output image Hash
        result = AdAccount(id).create_ad_image(fields=[], params=params)
        os.remove(f'temp/{file_name}.jpg')
        return result

    @classmethod
    def create_campaign(cls, name, objective):
        FacebookAdsApi.init(access_token=Config.ACCESS_TOKEN)
        id = Config.AD_ACCOUNT_ID
        params = {
            "name": name,
            "objective": objective,
            "status": "PAUSED",
            "special_ad_categories": [],
        }
        return AdAccount(id).create_campaign(fields=[], params=params)

    @classmethod
    def create_adset(cls, name, budget, optimization_goal, campaign_id, bid, audience_age, locations):
        today = datetime.today()
        expire = datetime.now() + timedelta(days=10)

        today = today.strftime("%Y-%m-%d")
        expire = expire.strftime("%Y-%m-%d")

        FacebookAdsApi.init(access_token=Config.ACCESS_TOKEN)
        id = Config.AD_ACCOUNT_ID
        params = {
            'name': name,
            'daily_budget': budget,
            'bid_amount': bid,
            'billing_event': 'IMPRESSIONS',
            'optimization_goal': optimization_goal,
            'campaign_id': campaign_id,
            'promoted_object': {'page_id': Config.PAGE_ID},
            'date_preset': {'since': today, 'until': expire},
            'targeting': {'geo_locations': {'countries': locations},
                          'age_max': audience_age['max_age'], 'age_min': audience_age['min_age']},
            'status': 'PAUSED',
        }
        return AdAccount(id).create_ad_set(
            fields=[],
            params=params,
        )

    @classmethod
    def create_ad_creatice(cls, link_message, link, name, image):
        image_hash = FacebookMarketing.create_image_hash(image)
        FacebookAdsApi.init(access_token=Config.ACCESS_TOKEN)
        id = Config.AD_ACCOUNT_ID
        params = {
            "name": name,
            'status': 'PAUSED',
            "object_story_spec": {
                "page_id": Config.PAGE_ID,
                "link_data": {
                    "image_hash": image_hash['hash'],
                    "link": link,
                    "message": link_message,
                },
            },
        }
        return AdAccount(id).create_ad_creative(fields=[], params=params)

    @classmethod
    def create_ad(cls, name, creative_id, adset_id):
        FacebookAdsApi.init(access_token=Config.ACCESS_TOKEN)
        id = Config.AD_ACCOUNT_ID
        fields = [
        ]
        params = {
            'name': name,
            'adset_id': adset_id,
            'creative': {'creative_id': creative_id},
            'status': 'PAUSED',
            "bid_info": {"CLICKS": 150}

        }
        AdAccount(id).create_ad(
            fields=fields,
            params=params,
        )

        return AdAccount(id).create_ad(
            fields=[],
            params=params,
        )

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
