import os
import sys
from tweepy import API
from tweepy import OAuthHandler

def get_twitter_auth():

    try:
        consumer_key=''
        consumer_secret=''
        access_token_key=''
        access_token_secret=''

    except KeyError:
        sys.stderr.write("Twitter Enviroment Variable not set \n")

    auth = OAuthHandler(consumer_key,consumer_secret)
    auth.set_access_token(access_token_key,access_token_secret)

    return auth

def get_twitter_client():

    auth = get_twitter_auth()
    client = API(auth)
    return client
