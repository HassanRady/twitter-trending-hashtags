import os
from os.path import join, dirname
from dotenv import load_dotenv
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

from tweepy import OAuthHandler
from tweepy import API

consumer_key = os.environ['CONSUMER_KEY']
consumer_secret = os.environ['CONSUMER_SECRET']
access_token = os.environ['ACCESS_TOKEN']
access_secret = os.environ['ACCESS_SECRET']

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

class Tweets(object):
    """Tweets class"""
    def __init__(self, ):
        self.api = API(auth, wait_on_rate_limit=True,)

    def get_trending_hashtags(self, WOEID=1):
        """getting the trending hashtags"""

        tags = self.api.trends_place(WOEID)
        return tags