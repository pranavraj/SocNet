from github import Github
from user import GithubUser

class SocNetGithub():

	self.access_token = None
	self.username = None
	self.password = None
	self.user = None
	self.pointer = None
	def __init__(self, access_token):
		self.access_token = access_token
		self.pointer = Github(self.access_token)
		self.user = self.pointer.get_user()
	def __init__(self, username, password):
		self.username = username
		self.password = password
		self.pointer = Github(self.username, self.password)
		self.user = self.pointer.get_user()
	
		

	
