from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.types import InputPeerEmpty
from telethon.sync import TelegramClient
from telethon.tl.types import InputMessagesFilterUrl
import time
api_id = <>
api_hash = <>
phone = <>
client = TelegramClient(phone, api_id, api_hash)
client.connect()
if not client.is_user_authorized():
    client.send_code_request(phone)
    client.sign_in(phone, input('Enter the code: '))
for dialog in client.iter_dialogs():
    pass
##    print(dialog.name, 'has ID', dialog.id)
# get message and extract from other groups

GROUP = 'follownetwork30'
FORMAT = 'drop dx30 '
COUNT = 0
def read_file(file_name):
    with open(file_name, 'r') as f:
        a=f.readlines()
    return a

'''
thoi gian giua 2 lan drop = 12h /so luong acc vip
'''

while True:
    if COUNT != 2:
        file = read_file('auto_drop.txt')
        for i in file:
            client.send_message(GROUP, FORMAT+i)
            print('between list - ', i)
            time.sleep(15*60)
        COUNT = COUNT + 1
    if COUNT == 2:
        time.sleep(60*60*12)
        COUNT = 0
