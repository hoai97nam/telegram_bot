"""
1. This file is used for auto like many Instagram posts, work with text file
2. This file extract from Instabot repository or forked repo (https://github.com/hoai97nam/InstaBot/tree/instabot-custom)
3. instabot-custom is added like media function
"""
from instabot_functions import like_medias,log_in
import warnings 
warnings.filterwarnings("ignore") #f**k warnings
import instabot_data_api
from instabot_data_api import dataAPI
instabot_data_api.STORE_LOGS = True 

user='username
password='password'
email='username'

driver = log_in(email,password,user,for_aws=False,headless=True)
### If login failure, we cannot pursue the loop, we retry
if driver==0:
    print('LOG:',user,"MAIN","INFO","failed to log-in and get the driver")

# like_medias('https://www.instagram.com/p/CHi1b_iLTuv/',user,driver)

links=[]
with open('sample_file.txt') as f:
    a=f.readlines()
links=[i.split(" ")[1] for i in a]

for i in links:
    like_medias(i,user,driver)

print('FINISHED !!!')
