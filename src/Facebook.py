__author = "Pranav Raj"
__email = "pranav09032@hotmail.com"

import simplejson as json
import urllib


class Facebook ():

    def __init__(self, accessToken):

        self.accessToken = accessToken
        self.id = None
        self.name = None
        self.baseUrl = "https://graph.facebook.com/"

    def user_information(self, fbUser="me"):
        """
        returns User Information ; fbUser can be the facebook id of any user ;
        for the current user it is 'me'
        """

        profile = json.load(
            urllib.urlopen(
                self.baseUrl
                + fbUser + "?"
                + urllib.urlencode(
                    dict(accessToken=
                         self.accessToken))))
        self.id = str(profile["id"])
        self.name = str(profile["name"])
        user = dict(key_name=str(profile["id"]),
                id=str(profile["id"]),
                name=profile["name"],
                accessToken=self.accessToken,
                profile_url=profile["link"]
        return user

    def get_friends(self, maxPage=4, fbUser="me"):
        """
        Gets the list of friends , maxPage : Pages need to be accessed ;
        4 can cober most of the friendlist ; will ensure that data is
        returned within 60 secs
        """
        friends = json.load(urllib.urlopen(self.baseUrl + fbUser + "/friends?"
            + urllib.urlencode(dict(accessToken=self.accessToken))))
        Friends = []
        while "next" in friends["paging"]:
            if maxPage == 0:
                break
            maxPage = maxPage - 1
            Friends = Friends + friends["data"]
            friends = json.load(urllib.urlopen(friends["paging"]["next"]))
        return Friends

    def get_user_wall(self, max_pages=2, fbUser="me"):
        """
        gets User Wall
        """

        user_feeds = json.load(urllib.urlopen(self.baseUrl + fbUser + "/feed?"
            + urllib.urlencode(dict(accessToken=self.accessToken))))
        Data = []
        while True:
            try:
                Data = Data + user_feeds["data"]
                user_feeds = json.load(
                    urllib.urlopen(user_feeds["paging"]["next"]))
                max_pages = max_pages - 1
                if max_pages < 1:
                    break
            except:
                break
        return Data

    def get_user_comments_story(self, fbUser="me"):
        """
        gets User Comments
        """

        UserWall = self.get_user_wall(fbUser=fbUser)
        returnData = []

        for feed in UserWall:
            if "story" in feed:
                returnData.append(feed["story"])

        return returnData

    def get_user_comments_picture(self, fbUser="me"):

        UserWall = self.get_user_wall(fbUser=fbUser)
        returnData = []

        for feed in UserWall:
            if "picture" in feed:
                returnData.append(feed["picture"])

        return returnData

    def get_user_comments_from(self, fbUser="me"):

        UserWall = self.get_user_wall(fbUser=fbUser)
        returnData = []

        for feed in UserWall:
            if "from" in feed:
                returnData.append(feed["from"])

        return returnData

    def get_user_comments_name(self, fbUser="me"):

        UserWall = self.get_user_wall(fbUser=fbUser)
        returnData = []

        for feed in UserWall:
            if "name" in feed:
                returnData.append(feed["name"])

        return returnData

    def get_user_comments_caption(self, fbUser="me"):

        UserWall = self.get_user_wall(fbUser=fbUser)
        returnData = []

        for feed in UserWall:
            if "caption" in feed:
                returnData.append(feed["caption"])

        return returnData

    def get_user_comments_description(self, fbUser="me"):

        UserWall = self.get_user_wall(fbUser=fbUser)
        returnData = []

        for feed in UserWall:
            if "description" in feed:
                returnData.append(feed["description"])

        return returnData

    def get_user_comments_comments(self, fbUser="me"):

        UserWall = self.get_user_wall(fbUser=fbUser)
        returnData = []

        for feed in UserWall:
            if "comments" in feed:
                returnData.append(feed["comments"])

        return returnData

    def get_user_comments_updated_time(self, fbUser="me"):

        UserWall = self.get_user_wall(fbUser=fbUser)
        returnData = []

        for feed in UserWall:
            if "updated_time" in feed:
                returnData.append(feed["updated_time"])

        return returnData

    def get_user_comments_type(self, fbUser="me"):

        UserWall = self.get_user_wall(fbUser=fbUser)
        returnData = []

        for feed in UserWall:
            if "type" in feed:
                returnData.append(feed["type"])

        return returnData

    def get_user_comments_id(self, fbUser="me"):

        UserWall = self.get_user_wall(fbUser=fbUser)
        returnData = []

        for feed in UserWall:
            if "id" in feed:
                returnData.append(feed["id"])

        return returnData

    def get_user_comments_likes(self, fbUser="me"):

        UserWall = self.get_user_wall(fbUser=fbUser)
        returnData = []

        for feed in UserWall:
            if "likes" in feed:
                returnData.append(feed["likes"])

        return returnData

    def get_user_likes(self, fbUser="me"):

        user_likes = json.load(
                                urllib.urlopen(
                                                self.baseUrl
                                              + fbUser + "/likes?"
                                              + urllib.urlencode(
                                                dict(accessToken
                                                =self.accessToken))))
        returnData = []

        while True:
            try:
                returnData = returnData + \
                    [x["name"] for x in user_likes["data"]]
                user_likes = json.load(
                    urllib.urlopen(user_likes["paging"]["next"]))
            except:
                break

        return returnData

    def get_user_movies(self, fbUser="me"):

        user_movies = json.load(
            urllib.urlopen(self.baseUrl + fbUser + "/movies?"
                + urllib.urlencode(dict(accessToken=self.accessToken))))
        returnData = []

        while True:

            try:
                returnData = returnData + \
                    [x["name"] for x in user_movies["data"]]
                user_movies = json.load(
                    urllib.urlopen(user_movies["paging"]["next"]))
            except:
                break

        return returnData

    def get_user_music(self, fbUser="me"):

        user_music = json.load(
            urllib.urlopen(self.baseUrl + fbUser + "/music?"
                + urllib.urlencode(dict(accessToken=self.accessToken))))
        returnData = []

        while True:

            try:
                returnData = returnData + \
                    [x["name"] for x in user_music["data"]]
                user_music = json.load(
                    urllib.urlopen(user_music["paging"]["next"]))
            except:
                break

        return returnData

    def get_user_books(self, fbUser="me"):

        user_book = json.load(
            urllib.urlopen(self.baseUrl + fbUser + "/books?"
                + urllib.urlencode(dict(accessToken=self.accessToken))))
        returnData = []

        while True:

            try:
                returnData = returnData + \
                    [x["name"] for x in user_book["data"]]
                user_book = json.load(
                    urllib.urlopen(user_book["paging"]["next"]))
            except:
                break

        return returnData

    def get_user_notes(self, fbUser="me"):

        user_notes = json.load(
            urllib.urlopen(self.baseUrl + fbUser + "/notes?"
                + urllib.urlencode(dict(accessToken=self.accessToken))))
        returnData = []

        while True:

            try:
                returnData = returnData + \
                    [x["name"] for x in user_notes["data"]]
                user_notes = json.load(
                    urllib.urlopen(user_notes["paging"]["next"]))
            except:
                break

        return returnData

    def get_user_photos(self, fbUser="me"):

        user_photos = json.load(
            urllib.urlopen(self.baseUrl + fbUser + "/photos?"
                + urllib.urlencode(dict(accessToken=self.accessToken))))
        returnData = []

        while True:

            try:
                returnData = returnData + \
                    [x["name"] for x in user_photos["data"]]
                user_photos = json.load(
                    urllib.urlopen(user_photos["paging"]["next"]))
            except:
                break

        return returnData

    def get_user_events(self, fbUser="me"):

        user_notes = json.load(
            urllib.urlopen(self.baseUrl + fbUser + "/events?"
                + urllib.urlencode(dict(accessToken=self.accessToken))))
        returnData = []

        while True:

            try:
                returnData = returnData + [x for x in user_notes["data"]]
                user_notes = json.load(
                    urllib.urlopen(user_notes["paging"]["next"]))
            except:
                break

        return returnData

    def get_user_groups(self, fbUser="me"):

        user_notes = json.load(
            urllib.urlopen(self.baseUrl + fbUser + "/groups?"
                + urllib.urlencode(dict(accessToken=self.accessToken))))
        returnData = []

        while True:

            try:
                returnData = returnData + \
                    [x["name"] for x in user_notes["data"]]
                user_notes = json.load(
                    urllib.urlopen(user_notes["paging"]["next"]))
            except:
                break

        return returnData

    def get_user_places(self, fbUser="me"):

        user_places = json.load(
            urllib.urlopen(self.baseUrl + fbUser + "/locations?"
                + urllib.urlencode(dict(accessToken=self.accessToken))))
        returnData = {}

        while True:

            try:
                tempData = [x["place"]["name"] for x in user_places["data"]]
                for place in tempData:
                    if place in returnData:
                        returnData[place] = returnData[place] + 1
                    else:
                        returnData[place] = 0
                user_places = json.load(
                    urllib.urlopen(user_places["paging"]["next"]))
            except:
                break

        return returnData

if __name__ == "__main__" :
    fb = Facebook("")
