from telethon.sync import TelegramClient
from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.types import InputPeerEmpty, InputPeerChannel, InputPeerUser
from telethon.errors.rpcerrorlist import PeerFloodError, UserPrivacyRestrictedError
from telethon.tl.functions.channels import InviteToChannelRequest
import sys
import csv
import traceback
import time
start = time.time() # begin time
# sim viettel
api_id = <api_id>
api_hash = '<api_hash>'
phone = '<your_phone_number>'
client = TelegramClient(phone, api_id, api_hash)

client.connect()
if not client.is_user_authorized():
    client.send_code_request(phone)
    client.sign_in(phone, input('Enter the code: '))

input_file = sys.argv[1]
users = []
with open(input_file, encoding='UTF-8') as f:
    rows = csv.reader(f,delimiter=",",lineterminator="\n")
    next(rows, None)
    for row in rows:
        user = {}
        user['username'] = row[0]
        user['id'] = int(row[1])
        user['access_hash'] = int(float(row[2])) # changing something in data type
        user['name'] = row[3]
        users.append(user)

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

"""
Automatically add in target group by using unique group id

"""
k = 0
print(len(groups))
for i in range(len(groups)):
    if groups[i].id == 1211589948: # group id for target group
        k = i
        break
    
print("You are adding in ",groups[k].title)
print("Group ID: ",groups[k].id)
#print("",groups[k].access_hash)
target_group_entity = InputPeerChannel(groups[k].id,groups[k].access_hash)

i = 1 #testing numbering

for user in users:
    try:
        """
        Numbering member for adding
        """
        print ("{}. Adding {}".format(i, user['id'])) # this location "i"
        """
        Auto add member by username
        """
        if user['username'] == "":
            continue
        user_to_add = client.get_input_entity(user['username'])
        client(InviteToChannelRequest(target_group_entity,[user_to_add]))
        
        print("Waiting 60 Seconds...")
        time.sleep(60) #sleep 60 instead 60
        
        i = i + 1   # this location increases counting unit
    except PeerFloodError:
        print("Getting Flood Error from telegram. Script is stopping now. Please try again after some time.")
    except UserPrivacyRestrictedError:
        print("The user's privacy settings do not allow you to do this. Skipping.")
    except:
        traceback.print_exc()
        print("Unexpected Error")
        continue

end = time.time()
print("spending time:",(end-start))

