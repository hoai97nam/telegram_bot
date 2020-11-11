from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep, strftime
from random import randint
import pandas as pd

def read_links():
	with open('sample_file.txt') as f:
		a=f.readlines()
	links=[i.split(" ")[1] for i in a]
	return links

chromedriver_path = 'D:/Data/bots/tools/chromedriver.exe' # Change this to your own chromedriver path!
webdriver = webdriver.Chrome(executable_path=chromedriver_path)
sleep(2)
webdriver.get('https://www.instagram.com/accounts/login/?source=auth_switcher')
sleep(3)

username = webdriver.find_element_by_name('username')
username.send_keys('usrname')
password = webdriver.find_element_by_name('password')
password.send_keys('passwd')


button_login = webdriver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button/div')
button_login.click()
sleep(2)

# notnow = webdriver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div/button')
# notnow.click() #comment these last 2 lines out, if you don't get a pop up asking about notifications
def like(link):
	webdriver.switch_to.window(webdriver.window_handles[0])
	webdriver.get(link)
	sleep(2)
	like = webdriver.find_element_by_class_name('fr66n')
	print(like)
	like.click()
	sleep(2)

ass=read_links()
for i in ass:
	like(i)
	sleep(randint(5,8))

webdriver.close()
print('BACK to telegram group and DROP your link')
