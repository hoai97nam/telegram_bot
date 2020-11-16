from telethon.sync import TelegramClient
import csv
from telethon.tl.types import InputMessagesFilterUrl
from telethon import types
import time
from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.types import InputPeerEmpty

api_id = '<api_id>'
api_hash = '<api_hash>'
phone = '<phone_number>'
client = TelegramClient(phone, api_id, api_hash)

client.connect()
if not client.is_user_authorized():
    client.send_code_request(phone)
    client.sign_in(phone, input('Enter the code: '))

from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.types import InputPeerEmpty
chats = []
last_date = None
chunk_size = 200
groups=[]

result = client(GetDialogsRequest(
             offset_date=last_date,
             offset_id=0,
             offset_peer=InputPeerEmpty(),
             limit=chunk_size,
             hash = 0
         ))
chats.extend(result.chats)

for chat in chats:
    try:
        if chat.megagroup== True:
            groups.append(chat)
    except:
        continue

print('Choose a group to scrape members from:')
i=0
for g in groups:
    print(str(i) + '- ' + g.title)
    i+=1

g_index = input("Enter a Number: ")
target_group=groups[int(g_index)]

print('Fetching Members...')
all_participants = []
all_participants = client.get_participants(target_group, aggressive=True)

#print(all_participants) # log type all_participants 

print('Saving In file...')
with open("members.csv","w",encoding='UTF-8') as f:
    writer = csv.writer(f,delimiter=",",lineterminator="\n")
    writer.writerow(['username','status'])
    for user in all_participants:
        if user.username: # UserStatusRecently() for active account filter
            username= user.username
        else:
            #username= ""
            continue
        # if user.first_name:
        #     first_name= user.first_name
        # else:
        #     first_name= ""
        # if user.last_name:
        #     last_name= user.last_name
        # else:
        #     last_name= ""
        # name= (first_name + ' ' + last_name).strip()

        # t=user.stringify()
        
        if isinstance(user.status, types.UserStatusOffline):
            #print((user.status.was_online))           
            #if time.time()-(user.status.was_online).timestamp() <=3600 
        
            writer.writerow([username, 1 if time.time()-(user.status.was_online).timestamp() <=3600 else 0])      
print('Members scraped successfully.')
