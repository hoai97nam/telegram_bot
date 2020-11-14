from InstagramAPI import InstagramAPI
import time
from datetime import datetime
import requests
import pprint
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
# sign in 

#get user id

# usrname='tnt12dck'
# API.searchUsername(usrname)
# usr_id=API.LastJson['user']['pk']
# #get user followings
# API.getUserFollowers(usr_id)
# fl=API.LastJson['users']
# print(API.LastJson['users'][0]['username'])
#----------------------------------------------------- testing block
#put result in list
'''
k=1
list_following=set()
list_following_full=[]
for i in fl:
    print('{}. '.format(k) + i['username'])
    list_following.add(i['username'])
    list_following_full.append(str(i))
    k+=1
print(type(fl))    
print(fl[0]['username'])
#--------------------------------------------------------
'''
def get_latest_follower(list_1):
    latest_follower_list=[]
    for i in list_1:
        API.searchUsername(i)
        # print(API.LastJson['user']['pk'])
        uid=API.LastJson['user']['pk']
        #get user followings
        API.getUserFollowers(uid)
        latest_follower_list.append(API.LastJson['users'][0]['username'])
    return latest_follower_list

def check_follower_step2(profile,list_1):
    check_in=[]
    check_in2 = []
    prf=False
    for i in list_1:
        API.searchUsername(i)
        # print(API.LastJson['user']['pk'])
        uid=API.LastJson['user']['pk']
        #get user followings
        API.getUserFollowers(uid)
        k = API.LastJson['users']
        check_in.append(str(k).find(i))
        check_in2.append(k[0]['username'])
    if API.searchUsername(profile):
        prf = True
    return check_in, check_in2, prf
# list 1 is target user given to user who call '/list' command
def check_follow_yet(profile, list1): 
    API = InstagramAPI("nokia51plus", "nguyenhnam")
    API.login()

    tmp, tmp2, prf = check_follower_step2(profile, list1)
    print(tmp)
    tmp=set(tmp)
    if len(tmp) == 1 and prf:
        print('acceptable')
        return 1
    else:   
        print('inacceptable !!! check step-2')
        tmp2=set(tmp2)
        if len(tmp2) == 1 and prf:
            print('acceptable')
            return 1
    return 0

def check_profile(profile):
    API = InstagramAPI("nokia51plus", "nguyenhnam")
    API.login()
    if API.searchUsername(profile):
        return 1
    else:
        return 0
