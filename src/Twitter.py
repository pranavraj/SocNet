__author = "Pranav Raj"
__email = "pranav09032@hotmail.com"

import tweepy
import TwitterConfig as config_twitter


class Twitter:

    def __init__(self):
        self.CONSUMER_KEY = config_twitter.get_consumer_key()
        self.CONSUMER_SECRET = config_twitter.get_consumer_secret()
        self.oauth_token = None
        self.oauth_verifier = None
        self.api = None

    def get_auth_url(self):
        self.auth = tweepy.OAuthHandler(
            self.CONSUMER_KEY,
            self.CONSUMER_SECRET)
        return self.auth.get_authorization_url()

    def get_request_token(self):
        return (self.auth.request_token.key, self.auth.request_token.secret)

    def set_token(self, token):
        self.oauth_token = token

    def set_verifier(self, verifier):
        self.oauth_verifier = verifier

    def set_request_token(self, ReqToken):
        self.request_token = ReqToken

    def get_access_token(self):
        self.auth = tweepy.OAuthHandler(
            self.CONSUMER_KEY, self.CONSUMER_SECRET)
        token = self.request_token
        # session.delete('request_token')
        self.auth.set_request_token(token[0], token[1])
        self.auth.get_access_token(self.oauth_verifier)

    def authorize(self):
        key = self.auth.access_token.key
        secret = self.auth.access_token.secret
        self.auth = tweepy.OAuthHandler(
            self.CONSUMER_KEY, self.CONSUMER_SECRET)
        self.auth.set_access_token(key, secret)
        self.api = tweepy.API(self.auth)

    def checkVerification(self):
        condition = self.oauth_token and self.oauth_verifier and self.api
        if condition:
            raise Exception("Twitter verification problem")

    def update_status(self, status):
        self.checkVerification()
        self.api.update_status(status)
        return "Done"

    def user_information(self):
        # returns information of the authenticate user
        self.checkVerification()
        return self.api.me()

    def get_friends(self):
        self.checkVerification()
        return self.api.GetFriends(self.user_information().name)

    def get_followers(self):
        self.checkVerification()
        return self.api.GetFollowers()

    def get_followers_id(self):
        self.checkVerification()
        return self.api.followers_ids()

    def get_friends_ids(self):
        self.checkVerification()
        return self.api.friends_ids()

    def get_rate_limit_status(self):
        # returns the rate limit status of the authenticated user
        return self.api.rate_limit_status()

    def get_tweets(self):
        self.checkVerification()
        me = self.user_information()
        statuses = self.api.GetUseerTimeline(me.name)
        return statuses

    def get_messages(self):
        self.checkVerification()
        return self.api.GetDirectMessages()
