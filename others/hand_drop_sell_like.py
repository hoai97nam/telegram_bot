import time
from instabot import API
from tqdm import tqdm
import random

LINK_FILE = 'sample_file.txt'
USERNAME = 'username'
PASSWORD = 'passwd'

def read_links():
	with open(LINK_FILE) as f:
		a=f.readlines()
	links=[i.split(" ")[1] for i in a]
	return links


instabot = API()
instabot.login(	username = USERNAME, password = PASSWORD)

for i in tqdm(qread_links()):
	instabot.like(i[28:])
	time.sleep(random.randint(5,8))
print('BACK to telegram group and DROP your link')
