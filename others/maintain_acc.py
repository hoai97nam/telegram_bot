
from telethon import TelegramClient

# Remember to use your own values from my.telegram.org!
def account(phone,api_id,api_hash):
    print("ID of process running: {}".format(os.getpid()))
    client = TelegramClient(phone, api_id, api_hash)
    client.connect()
    client.loop.run_forever()


import threading 

if __name__ == "__main__": 
    # creating thread 
    t1 = threading.Thread(target=account, args=('+84132465895',123456, 'scfgghjhkjhlkjljlj;jlj')) ## args=(phone, api_id, api_hash)
    t2 = threading.Thread(target=account, args=()) 
    t3= threading.Thread(target=account, args=())

    t1.start() 
    t2.start() 
    t3.start()

    t1.join()  
    t2.join() 
    t3.join()

