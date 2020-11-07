## :bookmark_tabs: telegram automatic tools

#### :point_right: [Scrape](https://github.com/hoai97nam/telegram_bot/blob/master/scrape%20members/client_tele.py) members from customed group.

- 🌎 Change proxy when create new session help avoid banning from telegram, free proxies found [here](https://mtproto-proxy.fun/), code will be update later.

Change proxy with this command:

```
client = TelegramClient(
    phone,
    api_id,
    api_hash,
    connection=connection.ConnectionTcpMTProxyRandomizedIntermediate,
    proxy=('govir.imamatjome.me', 553, \
    'eecc84325ed8486dff37100a77777777776b65746161626f6e6c696e652e636f6d')
)
```

#### :point_right: [Add](https://github.com/hoai97nam/telegram_bot/tree/master/add_member) members after scraping from previous step to specify group.

- Also automate as possible processes in adding members

- For running simultaneously in addding member from group file with .BAT will help to do that.

#### :point_right: [Add](https://github.com/hoai97nam/telegram_bot/blob/master/add_member/add_mems_to_channel-public.py) members after scarping to channel.

#### :point_right: Check [follow](https://github.com/hoai97nam/telegram_bot/tree/master/check%20follow)

#### 📚📂 Packages/Libraries:
Install Python on your device (Window in my OS)

`pip install Telethon==<latest_version>`

`pip install pandas==1.0.x` 

`pip install instabot` (**note:** __scikit-learn__ version must be compatible to [profanity-check](https://github.com/hoai97nam/Instagagement/blob/master/NOTES.md) library)

`pip install InstagramAPI`
