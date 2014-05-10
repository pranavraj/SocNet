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
                        profile_url=profile["link"])
            return user

        raise Exception("Profile id or name is None")

    def getFriends(self, maxParsedPages=4, fbUser="me"):

        friends_info = self.readTag(fbUser, "friends")
        friends = []
        while "next" in friends_info["paging"]:
            if not maxParsedPages:
                break
            maxParsedPages -= 1
            friends += friends_info["data"]
            friends_info = json.load(
                self.urlRead(
                    friends_info["paging"]["next"]))
        return friends

    def getUserWall(self, max_pages=2, fbUser="me"):

        user_feeds = self.readTag(fbUser, "feed")
        Data = []
        while True:
            try:
                Data = Data + user_feeds["data"]
                user_feeds = json.load(
                    self.urlRead(user_feeds["paging"]["next"]))
                max_pages = max_pages - 1
                if max_pages < 1:
                    break
            except:
                break
        return Data

    def __getUserComment(self, fbUser, tag):

        UserWall = self.getUserWall(fbUser=fbUser)
        return [feed[tag] for feed in UserWall if tag in feed]

    def getUserCommentsStory(self, fbUser="me"):
        """
        gets User Comments
        """
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

    def getUserLikes(self, fbUser="me"):

        user_likes = self.readTag(fbUser, "likes")
        returnData = []

        while True:
            try:
                returnData += [x["name"] for x in user_likes["data"]]
                user_likes = json.load(
                    self.urlRead(
                        user_likes["paging"]["next"]))
            except:
                break

        return returnData

    def getUserMovies(self, fbUser="me"):

        user_movies = self.readTag(fbUser, "movies")
        returnData = []

        while True:

            try:
                returnData += [x["name"] for x in user_movies["data"]]
                user_movies = json.load(
                    self.urlRead(
                        user_movies["paging"]["next"]))
            except:
                break

        return returnData

    def getUserMusic(self, fbUser="me"):

        user_music = self.readTag(fbUser, "music")
        returnData = []

        while True:

            try:
                returnData += [x["name"] for x in user_music["data"]]
                user_music = json.load(
                    self.urlRead(
                        user_music["paging"]["next"]))
            except:
                break

        return returnData

    def getUserBooks(self, fbUser="me"):

        user_book = self.readTag(fbUser, "books")
        returnData = []

        while True:

            try:
                returnData += [x["name"] for x in user_book["data"]]
                user_book = json.load(
                    self.urlRead(
                        user_book["paging"]["next"]))
            except:
                break

        return returnData

    def getUserNotes(self, fbUser="me"):

        user_notes = self.readTag(fbUser, "notes")
        returnData = []

        while True:

            try:
                returnData += [x["name"] for x in user_notes["data"]]
                user_notes = json.load(
                    self.urlRead(
                        user_notes["paging"]["next"]))
            except:
                break

        return returnData

    def getUserPhotos(self, fbUser="me"):

        user_photos = self.readTag(fbUser, "photos")
        returnData = []

        while True:

            try:
                returnData += [x["name"] for x in user_photos["data"]]
                user_photos = json.load(
                    self.urlRead(
                        user_photos["paging"]["next"]))
            except:
                break

        return returnData

    def getUserEvents(self, fbUser="me"):

        user_notes = self.readTag(fbUser, "events")
        returnData = []

        while True:

            try:
                returnData += [x for x in user_notes["data"]]
                user_notes = json.load(
                    self.urlRead(
                        user_notes["paging"]["next"]))
            except:
                break

        return returnData

    def get_user_groups(self, fbUser="me"):

        user_notes = self.readTag(fbUser, "groups")
        returnData = []

        while True:

            try:
                returnData += [x["name"] for x in user_notes["data"]]
                user_notes = json.load(
                    self.urlRead(
                        user_notes["paging"]["next"]))
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
                    self.urlRead(
                        user_places["paging"]["next"]))
            except:
                break

        return returnData

if __name__ == "__main__":
    fb = Facebook("")
