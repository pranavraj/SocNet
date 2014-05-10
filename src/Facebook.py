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

    def urlRead(self, url):

        try:
            response = self.urlRead(url)
            return response
        except ConnectionError:
            raise Exception("Connection Exception")

    def readTag(self, user, tag=""):

        return json.load(
            self.urlRead(
                self.baseUrl
                + "/" + tag + "?"
                + urllib.urlencode(
                    dict(accessToken=
                         self.accessToken))))

    def userInformation(self, fbUser="me"):

        profile = self.readTag(fbUser, "")
        self.id = profile.get("id", None)
        self.name = profile.get("name", None)
        if self.id and self.name:
            user = dict(key_name=str(profile["id"]),
                        id=str(profile["id"]),
                        name=profile["name"],
                        accessToken=self.accessToken,
                        profile_url=profile.get("link", None))
            return user
        raise Exception("Profile id or name is None")

    def getFriends(self, maxParsedPages=4, fbUser="me"):

        friendsInfo = self.readTag(fbUser, "friends")
        friends = []
        for pages in range(maxParsedPages):
            paging = friendsInfo.get("paging", None)
            if not paging:
                raise Exception("Paging Error")
            if "next" in paging:
                friends += friendsInfo.get("userWall", [])
                friendsInfo = json.load(self.urlRead(paging["next"]))
            else:
                break
        return friends

    def getUserWall(self, maxParsedPages=2, fbUser="me"):

        userFeeds = self.readTag(fbUser, "feed")
        userWall = []
        for pages in range(maxParsedPages):
            feed = userFeeds.get("userWall", None)
            if not feed:
                break
            userWall += feed
            paging = userFeeds.get("paging", None)
            if not paging:
                break
            nextUrl = paging.get("next", None)
            if not nextUrl:
                break
            userFeeds = json.load(
                self.urlRead(
                    nextUrl))
        return userWall

    def __getUserComment(self, fbUser, tag):

        UserWall = self.getUserWall(fbUser=fbUser)
        return [feed[tag] for feed in UserWall if tag in feed]

    def getUserCommentsStory(self, fbUser="me"):

        return self.__getUserComment(fbUser, "story")

    def getUserCommentsPicture(self, fbUser="me"):

        return self.__getUserComment(fbUser, "picture")

    def getUserCommentsFrom(self, fbUser="me"):

        return self.__getUserComment(fbUser, "from")

    def getUserCommentsName(self, fbUser="me"):

        return self.__getUserComment(fbUser, "name")

    def getUserCommentsCaption(self, fbUser="me"):

        return self.__getUserComment(fbUser, "caption")

    def getUserCommentsDescription(self, fbUser="me"):

        return self.__getUserComment(fbUser, "description")

    def getUserCommentsComments(self, fbUser="me"):

        return self.__getUserComment(fbUser, "comments")

    def getUserCommentsUpdatedTime(self, fbUser="me"):

        return self.__getUserComment(fbUser, "updated_time")

    def getUserCommentsType(self, fbUser="me"):

        return self.__getUserComment(fbUser, "type")

    def getUserCommentsId(self, fbUser="me"):

        return self.__getUserComment(fbUser, "id")

    def getUserCommentsLikes(self, fbUser="me"):

        return self.__getUserComment(fbUser, "likes")

    def __getUserInfo(self, fbUser, fbProperty, maxParsedPages=4):

        userRawProperty = self.readTag(fbUser, fbProperty)
        userProperty = []
        for pages in range(maxParsedPages):
            userProperty += [obj["name"] for obj in userRawProperty["data"]]
            paging = userRawProperty.get("paging", None)
            if not paging:
                break
            nextUrl = paging.get("next", None)
            if not nextUrl:
                break
            userRawProperty = json.load(
                self.urlRead(
                    nextUrl))
        return userProperty

    def getUserLikes(self, fbUser="me"):

        return self.__getUserInfo(
            fbUser,
            "likes")

    def getUserMovies(self, fbUser="me"):

        return self.__getUserInfo(
            fbUser,
            "movies")

    def getUserMusic(self, fbUser="me"):

        return self.__getUserInfo(
            fbUser,
            "music")

    def getUserBooks(self, fbUser="me"):

        return self.__getUserInfo(
            fbUser,
            "books")

    def getUserNotes(self, fbUser="me"):

        return self.__getUserInfo(
            fbUser,
            "notes")

    def getUserPhotos(self, fbUser="me"):

        return self.__getUserInfo(
            fbUser,
            "photos")

    def getUserEvents(self, fbUser="me"):

        return self.__getUserInfo(
            fbUser,
            "events")

    def get_user_groups(self, fbUser="me"):

        return self.__getUserInfo(
            fbUser,
            "groups")

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
                    self.urlRead(
                        user_places["paging"]["next"]))
            except:
                break

        return returnData

if __name__ == "__main__":
    fb = Facebook("")
