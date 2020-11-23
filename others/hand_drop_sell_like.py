"""
This tool using recent library from this link : https://github.com/b31ngD3v/MyIGBot

"""
import time
from tqdm import tqdm
import random

from myigbot import MyIGBot

LINK_FILE = 'sample_file.txt'
USERNAME = 'username'
PASSWORD = 'password'
COMMENT = False

bot = MyIGBot(USERNAME, PASSWORD)

def read_links():
	with open(LINK_FILE) as f:
		a=f.readlines()
	links=[i.split(" ")[1] for i in a]
	return links

list_tmp=read_links()
for i in tqdm(list_tmp):
	bot.like(i[28:])
	if COMMENT:
    		bot.comment(i[28:],comment_text='Nice project !!!')
	# print(i[28:])


print('BACK to telegram group and DROP your link')
