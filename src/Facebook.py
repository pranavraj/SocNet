import simplejson as json
import urllib

class SocnetshopFacebook ():

    def __init__ (self, access_token):

        self.access_token = access_token
        self.id = None
        self.name = None

    def user_information (self, fbuser = "me"):

        """ 
        returns User Information ; fbuser can be the facebook id of any user ; for the current user it is 'me'

        """
        profile = json.load(urllib.urlopen("https://graph.facebook.com/" + fbuser + "?" + urllib.urlencode(dict(access_token=self.access_token))))
        self.id = str(profile["id"])
        self.name = str(profile["name"])
        user = dict(key_name=str(profile["id"]), id=str(profile["id"]),  name=profile["name"], access_token=self.access_token, profile_url=profile["link"])
        return user

    def get_friends (self, maxPage = 4, fbuser = "me"):

        """
        Gets the list of friends , maxPage : Pages need to be accessed ; 4 can cober most of the friendlist ; will ensure that data is returned within 60 secs
        """
        friends = json.load(urllib.urlopen("https://graph.facebook.com/" + fbuser + "/friends?" + urllib.urlencode(dict(access_token=self.access_token))))
        Friends = []
        while "next" in friends["paging"]:
            if maxPage == 0:
                break
            maxPage = maxPage - 1
            Friends = Friends + friends["data"]
            friends = json.load(urllib.urlopen(friends["paging"]["next"]))
        return Friends

    def get_user_wall (self, max_pages = 2, fbuser = "me"):
        """
        gets User Wall 
        """

        user_feeds = json.load(urllib.urlopen("https://graph.facebook.com/" + fbuser + "/feed?" + urllib.urlencode(dict(access_token=self.access_token))))
        Data = []
        while True :
            try:
                Data = Data + user_feeds["data"]
                user_feeds = json.load(urllib.urlopen(user_feeds["paging"]["next"]))
                max_pages = max_pages-1
                if max_pages < 1 :
                    break
            except:
                break
        return Data

    def get_user_comments_story (self, fbuser = "me"):
        """
        gets User Comments 
        """

        UserWall = self.get_user_wall(fbuser = fbuser)
        returnData = []

        for feed in UserWall :
            if "story" in feed:
                returnData.append(feed["story"])

        return returnData 

    def get_user_comments_picture(self, fbuser = "me"):

        UserWall = self.get_user_wall(fbuser = fbuser)
        returnData = []

        for feed in UserWall :
            if "picture" in feed:
                returnData.append(feed["picture"])

        return returnData 

    def get_user_comments_from(self, fbuser = "me"):

        UserWall = self.get_user_wall(fbuser = fbuser)
        returnData = []

        for feed in UserWall :
            if "from" in feed:
                returnData.append(feed["from"])

        return returnData 
            
    def get_user_comments_name(self, fbuser = "me"):

        UserWall = self.get_user_wall(fbuser = fbuser)
        returnData = []

        for feed in UserWall :
            if "name" in feed:
                returnData.append(feed["name"])

        return returnData 

    def get_user_comments_caption(self, fbuser = "me"):

        UserWall = self.get_user_wall(fbuser = fbuser)
        returnData = []

        for feed in UserWall :
            if "caption" in feed:
                returnData.append(feed["caption"])

        return returnData 

    def get_user_comments_description(self, fbuser = "me"):

        UserWall = self.get_user_wall(fbuser = fbuser)
        returnData = []

        for feed in UserWall :
            if "description" in feed:
                returnData.append(feed["description"])

        return returnData 

    def get_user_comments_comments(self, fbuser = "me"):

        UserWall = self.get_user_wall(fbuser = fbuser)
        returnData = []

        for feed in UserWall :
            if "comments" in feed:
                returnData.append(feed["comments"])

        return returnData 

    def get_user_comments_updated_time(self, fbuser = "me"):

        UserWall = self.get_user_wall(fbuser = fbuser)
        returnData = []

        for feed in UserWall :
            if "updated_time" in feed:
                returnData.append(feed["updated_time"])

        return returnData 

    def get_user_comments_type(self, fbuser = "me"):

        UserWall = self.get_user_wall(fbuser = fbuser)
        returnData = []

        for feed in UserWall :
            if "type" in feed:
                returnData.append(feed["type"])

        return returnData 

    def get_user_comments_id(self, fbuser = "me"):

        UserWall = self.get_user_wall(fbuser = fbuser)
        returnData = []

        for feed in UserWall :
            if "id" in feed:
                returnData.append(feed["id"])

        return returnData 

    def get_user_comments_likes(self, fbuser = "me"):

        UserWall = self.get_user_wall(fbuser = fbuser)
        returnData = []

        for feed in UserWall :
            if "likes" in feed:
                returnData.append(feed["likes"])

        return returnData 
    
    def get_user_likes (self, fbuser = "me"):

        user_likes = json.load(urllib.urlopen("https://graph.facebook.com/" + fbuser + "/likes?" + urllib.urlencode(dict(access_token=self.access_token))))
        returnData = []
        
        while True:
            try:
                returnData = returnData + [x["name"] for x in user_likes["data"]]
                user_likes = json.load(urllib.urlopen(user_likes["paging"]["next"]))
            except:
                break

        return returnData
    
    def get_user_movies (self, fbuser = "me"):
        
        user_movies = json.load(urllib.urlopen("https://graph.facebook.com/" + fbuser + "/movies?" + urllib.urlencode(dict(access_token=self.access_token))))
        returnData = []

        while True:

            try:
                returnData = returnData + [ x["name"] for x in user_movies["data"]]
                user_movies = json.load(urllib.urlopen(user_movies["paging"]["next"]))
            except:
                break

        
        return returnData
        
    def get_user_music (self, fbuser = "me"):
        
         user_music = json.load(urllib.urlopen("https://graph.facebook.com/" + fbuser + "/music?" + urllib.urlencode(dict(access_token=self.access_token))))
         returnData = []

         while True:

             try:
                 returnData = returnData + [ x["name"] for x in user_music["data"]]
                 user_music = json.load(urllib.urlopen(user_music["paging"]["next"]))
             except:
                break

         return returnData

    def get_user_books (self, fbuser = "me"):
        
         user_book = json.load(urllib.urlopen("https://graph.facebook.com/" + fbuser + "/books?" + urllib.urlencode(dict(access_token=self.access_token))))
         returnData = []

         while True:

             try:
                 returnData = returnData + [ x["name"] for x in user_book["data"]]
                 user_book = json.load(urllib.urlopen(user_book["paging"]["next"]))
             except:
                break

         return returnData

    def get_user_notes (self, fbuser = "me"):

         user_notes = json.load(urllib.urlopen("https://graph.facebook.com/" + fbuser + "/notes?" + urllib.urlencode(dict(access_token=self.access_token))))
         returnData = []

         while True:

             try:
                 returnData = returnData + [ x["name"] for x in user_notes["data"]]
                 user_notes = json.load(urllib.urlopen(user_notes["paging"]["next"]))
             except:
                break

         return returnData

    def get_user_photos (self, fbuser = "me"):
        
         user_photos = json.load(urllib.urlopen("https://graph.facebook.com/" + fbuser + "/photos?" + urllib.urlencode(dict(access_token=self.access_token))))
         returnData = []

         while True:

             try:
                 returnData = returnData + [ x["name"] for x in user_photos["data"]]
                 user_photos = json.load(urllib.urlopen(user_photos["paging"]["next"]))
             except:
                break

         return returnData
    
    def get_user_events(self, fbuser = "me"):

         user_notes = json.load(urllib.urlopen("https://graph.facebook.com/" + fbuser + "/events?" + urllib.urlencode(dict(access_token=self.access_token))))
         returnData = []

         while True:

             try:
                 returnData = returnData + [ x for x in user_notes["data"]]
                 user_notes = json.load(urllib.urlopen(user_notes["paging"]["next"]))
             except:
                break

         return returnData

    def get_user_groups (self, fbuser = "me"):

         user_notes = json.load(urllib.urlopen("https://graph.facebook.com/" + fbuser + "/groups?" + urllib.urlencode(dict(access_token=self.access_token))))
         returnData = []

         while True:

             try:
                 returnData = returnData + [ x["name"] for x in user_notes["data"]]
                 user_notes = json.load(urllib.urlopen(user_notes["paging"]["next"]))
             except:
                break

         return returnData

    def get_user_places (self, fbuser = "me"):

         user_places = json.load(urllib.urlopen("https://graph.facebook.com/" + fbuser + "/locations?" + urllib.urlencode(dict(access_token=self.access_token))))
         returnData = {}

         while True:

             try:
                 tempData = [ x["place"]["name"] for x in user_places["data"]]
                 for place in tempData:
                     if place in returnData:
                         returnData[place] = returnData[place]+1
                     else:
                         returnData[place] = 0
                 user_places = json.load(urllib.urlopen(user_places["paging"]["next"]))
             except:
                break

         return returnData

    def all_user_data (self):

        String = ""
        
        String = String + "\n USer Information \n"
        String = String + "________________________________________\n\n\n"
        String = String + str(self.user_information('502291155'))
        """
        String = String + "_____________________________________________________________________________________\n\n\n"
        String = String + "\n Friends \n"
        String = String + "________________________________________\n\n\n"
        String = String + str(self.get_friends())


        String = String + "_____________________________________________________________________________________\n\n\n"
        String = String + "\n user_books \n"
        String = String + "________________________________________\n\n\n"
        String = String + str(self.get_user_books())
        """

        return String
        """
        String = String + "_____________________________________________________________________________________\n\n\n"
        String = String + "\n user_comments_caption \n"
        String = String + "________________________________________\n\n\n"
        String = String + str(self.get_user_comments_caption())

        return String
        String = String + "_____________________________________________________________________________________\n\n\n"
        String = String + "\n user_comments_comments \n"
        String = String + "________________________________________\n\n\n"
        String = String + str(self.get_user_comments_comments())

        String = String + "_____________________________________________________________________________________\n\n\n"
        String = String + "\n user_comments_description \n"
        String = String + "________________________________________\n\n\n"
        String = String + str(self.get_user_comments_description())

        String = String + "_____________________________________________________________________________________\n\n\n"
        String = String + "\n user_comments_from \n"
        String = String + "________________________________________\n\n\n"
        String = String + str(self.get_user_comments_from())

        String = String + "_____________________________________________________________________________________\n\n\n"
        String = String + "\n user_comments_id \n"
        String = String + "________________________________________\n\n\n"
        String = String + str(self.get_user_comments_id())

        String = String + "_____________________________________________________________________________________\n\n\n"
        String = String + "\n user_comments_likes \n"
        String = String + "________________________________________\n\n\n"
        String = String + str(self.get_user_comments_likes())

        return String """

    def all_user_data1 (self):

        String = ""

        String = String + "_____________________________________________________________________________________\n\n\n"
        String = String + "\n user_comments_name \n"
        String = String + "________________________________________\n\n\n"
        String = String + str(self.get_user_comments_name())

        String = String + "_____________________________________________________________________________________\n\n\n"
        String = String + "\n user_comments_picture \n"
        String = String + "________________________________________\n\n\n"
        String = String + str(self.get_user_comments_picture())

        String = String + "_____________________________________________________________________________________\n\n\n"
        String = String + "\n user_comments_story \n"
        String = String + "________________________________________\n\n\n"
        String = String + str(self.get_user_comments_story())

        String = String + "_____________________________________________________________________________________\n\n\n"
        String = String + "\n user_comments_type \n"
        String = String + "________________________________________\n\n\n"
        String = String + str(self.get_user_comments_type())

        

        String = String + "_____________________________________________________________________________________\n\n\n"
        String = String + "\n user_comments_updated_time \n"
        String = String + "________________________________________\n\n\n"
        String = String + str(self.get_user_comments_updated_time())

        String = String + "_____________________________________________________________________________________\n\n\n"
        String = String + "\n user_events \n"
        String = String + "________________________________________\n\n\n"
        String = String + str(self.get_user_events())

        String = String + "_____________________________________________________________________________________\n\n\n"
        String = String + "\n user_groups \n"
        String = String + "________________________________________\n\n\n"
        String = String + str(self.get_user_groups())

        String = String + "_____________________________________________________________________________________\n\n\n"
        String = String + "\n user_likes \n"
        String = String + "________________________________________\n\n\n"
        String = String + str(self.get_user_likes())

        String = String + "_____________________________________________________________________________________\n\n\n"
        String = String + "\n user_movies \n"
        String = String + "________________________________________\n\n\n"
        String = String + str(self.get_user_movies())

        String = String + "_____________________________________________________________________________________\n\n\n"
        String = String + "\n user_music \n"
        String = String + "________________________________________\n\n\n"
        String = String + str(self.get_user_music())

        String = String + "_____________________________________________________________________________________\n\n\n"
        String = String + "\n user_notes \n"
        String = String + "________________________________________\n\n\n"
        String = String + str(self.get_user_notes())

        String = String + "_____________________________________________________________________________________\n\n\n"
        String = String + "\n user_photos \n"
        String = String + "________________________________________\n\n\n"
        String = String + str(self.get_user_photos())

       

        String = String + "_____________________________________________________________________________________\n\n\n"
        String = String + "\n user_places \n"
        String = String + "________________________________________\n\n\n"
        String = String + str(self.get_user_places())

        String = String + "_____________________________________________________________________________________\n\n\n"
        String = String + "\n user_wall \n"
        String = String + "________________________________________\n\n\n"
        String = String + str(self.get_user_wall())

        return String





        