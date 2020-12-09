from telethon.sync import TelegramClient
from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.types import InputPeerEmpty, InputPeerChannel, InputPeerUser
from telethon.errors.rpcerrorlist import PeerFloodError, UserPrivacyRestrictedError
from telethon.tl.functions.channels import InviteToChannelRequest
import sys
import csv
import traceback
import time

api_id = 1324758
api_hash = 'your-api'
phone = 'your-phone-number'
client = TelegramClient(phone, api_id, api_hash)

client.connect()
if not client.is_user_authorized():
    client.send_code_request(phone)
    client.sign_in(phone, input('Enter the code: '))

users = []

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
#print(chats[-1])
for chat in chats:
    try:
        if chat.megagroup== False:
            groups.append(chat)
            #print(chat)
    except:
        continue

print('Choose a channel to add members:')
i=0
for group in groups:
    print(str(i) + '- ' + group.title)
    i+=1

g_index = input("Enter a Number: ")
target_group=groups[int(g_index)]

target_group_entity = InputPeerChannel(target_group.id,target_group.access_hash)

mode = int(input("Enter 1 to add by username or 2 to add by ID: "))
i = 1 #testing numbering
for user in users:
    if mode == 1:
        client.edit_admin(target_group_entity,user,is_admin=True, add_admins=True)
    else:
        sys.exit("Invalid Mode Selected. Please Try Again.")
    client(InviteToChannelRequest(target_group_entity,[user_to_add]))
    print("Waiting 10 Seconds...")
    time.sleep(10) #sleep 900 instead 60
