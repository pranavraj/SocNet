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

    def readTag(self, user, tag=""):
        return json.load(
            urllib.urlopen(
                self.baseUrl
                + "/" + tag + "?"
                + urllib.urlencode(
                    dict(accessToken=
                         self.accessToken))))

    def userInformation(self, fbUser="me"):
        """
        returns User Information ; fbUser can be the facebook id of any user ;
        for the current user it is 'me'
        """

        profile = self.readTag(fbUser, "")
        self.id = str(profile["id"])
        self.name = str(profile["name"])
        user = dict(key_name=str(profile["id"]),
                    id=str(profile["id"]),
                    name=profile["name"],
                    accessToken=self.accessToken,
                    profile_url=profile["link"])
        return user

    def getFriends(self, maxPage=4, fbUser="me"):
        """
        Gets the list of friends , maxPage : Pages need to be accessed ;
        4 can cober most of the friendlist ; will ensure that data is
        returned within 60 secs
        """
        friends = self.readTag(fbUser, "friends")
        Friends = []
        while "next" in friends["paging"]:
            if maxPage == 0:
                break
            maxPage = maxPage - 1
            Friends = Friends + friends["data"]
            friends = json.load(urllib.urlopen(friends["paging"]["next"]))
        return Friends

    def getUserWall(self, max_pages=2, fbUser="me"):
        """
        gets User Wall
        """

        user_feeds = self.readTag(fbUser, "feed")
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

    def getUserCommentsStory(self, fbUser="me"):
        """
        gets User Comments
        """

        UserWall = self.getUserWall(fbUser=fbUser)
        returnData = [feed["story"] for feed in UserWall if "story" in feed]
        return returnData

    def getUserCommentsPicture(self, fbUser="me"):

        UserWall = self.getUserWall(fbUser=fbUser)
        returnData = []

        for feed in UserWall:
            if "picture" in feed:
                returnData.append(feed["picture"])

        return returnData

    def getUserCommentsFrom(self, fbUser="me"):

        UserWall = self.getUserWall(fbUser=fbUser)
        returnData = []

        for feed in UserWall:
            if "from" in feed:
                returnData.append(feed["from"])

        return returnData

    def getUserCommentsName(self, fbUser="me"):

        UserWall = self.getUserWall(fbUser=fbUser)
        returnData = []

        for feed in UserWall:
            if "name" in feed:
                returnData.append(feed["name"])

        return returnData

    def getUserCommentsCaption(self, fbUser="me"):

        UserWall = self.getUserWall(fbUser=fbUser)
        returnData = []

        for feed in UserWall:
            if "caption" in feed:
                returnData.append(feed["caption"])

        return returnData

    def getUserCommentsDescription(self, fbUser="me"):

        UserWall = self.getUserWall(fbUser=fbUser)
        returnData = []

        for feed in UserWall:
            if "description" in feed:
                returnData.append(feed["description"])

        return returnData

    def getUserCommentsComments(self, fbUser="me"):

        UserWall = self.getUserWall(fbUser=fbUser)
        returnData = []

        for feed in UserWall:
            if "comments" in feed:
                returnData.append(feed["comments"])

        return returnData

    def getUserCommentsUpdatedTime(self, fbUser="me"):

        UserWall = self.getUserWall(fbUser=fbUser)
        returnData = []

        for feed in UserWall:
            if "updated_time" in feed:
                returnData.append(feed["updated_time"])

        return returnData

    def getUserCommentsType(self, fbUser="me"):

        UserWall = self.getUserWall(fbUser=fbUser)
        returnData = []

        for feed in UserWall:
            if "type" in feed:
                returnData.append(feed["type"])

        return returnData

    def getUserCommentsId(self, fbUser="me"):

        UserWall = self.getUserWall(fbUser=fbUser)
        returnData = []

        for feed in UserWall:
            if "id" in feed:
                returnData.append(feed["id"])

        return returnData

    def getUserCommentsLikes(self, fbUser="me"):

        UserWall = self.getUserWall(fbUser=fbUser)
        returnData = []

        for feed in UserWall:
            if "likes" in feed:
                returnData.append(feed["likes"])

        return returnData

    def getUserLikes(self, fbUser="me"):

        user_likes = self.readTag(fbUser, "likes")
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

    def getUserMovies(self, fbUser="me"):

        user_movies = self.readTag(fbUser, "movies")
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

    def getUserMusic(self, fbUser="me"):

        user_music = self.readTag(fbUser, "music")
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

    def getUserBooks(self, fbUser="me"):

        user_book = self.readTag(fbUser, "books")
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

    def getUserNotes(self, fbUser="me"):

        user_notes = self.readTag(fbUser, "notes")
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

    def getUserPhotos(self, fbUser="me"):

        user_photos = self.readTag(fbUser, "photos")
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

    def getUserEvents(self, fbUser="me"):

        user_notes = self.readTag(fbUser, "events")
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

        user_notes = self.readTag(fbUser, "groups")
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

    def getUserPlaces(self, fbUser="me"):

        user_places = self.readTag(fbUser, "locations")
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

if __name__ == "__main__":
    fb = Facebook("")
