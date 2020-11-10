import time
from instabot import API


LINK_FILE = 'sample_file.txt'
USERNAME = 'nhnam97'
PASSWORD = 'nguyennam'

def read_links():
	with open(LINK_FILE) as f:
		a=f.readlines()
	links=[i.split(" ")[1] for i in a]
	return links


instabot = API()
instabot.login(	username = USERNAME, password = PASSWORD)

for i in read_links():
	instabot.like_medias(i[28:],1)
	# print(i[28])


