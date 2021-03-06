#!/usr/bin/env python
# -*- coding: utf-8 -*-
# This program is inherited from public repositories.

"""
Bot to reply to Telegram messages.
Manage follow engagement processes
Checking conditions from user before post on engagement group
Interact to telegram API to get latest link as requirement for comming up posts
"""
from telethon.tl.types import BotInlineMessageText
import logging
from telethon.tl.types import BotInlineResult

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram.bot import *
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
import telegram.message
import telegram.chat
import datetime
import time
from check_follow import check_follow_yet
# declare constant

TOKEN = '1098222229:AAE27CLsIN1xPwoDcjrBbz-z34lualgzbB4'
GROUP = '@follownetwork30'
FILE = 'user.txt'
GROUP_TYPE = 'Dx30'
SOURCE = 'https://www.instagram.com/'

def get_links_from_file(get_username=False):
    try:
        with open('user.txt','r') as f:
            lines=f.readlines() #include '\n' (newline)
    except:
        print('can not open links file')
    clean=[]
    for i in lines:
        if get_username == True:
            clean.append(i[i.find('com/')+4:-1])
        else:
            clean.append(i[:-1])      
    return clean

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)
# BotInlineMessageText("hello")
def get_list():  
    a=get_links_from_file()
    container=[]
    count=1
    for i in a:
        container.append('{}. [{}]({})'.format(count,i[i.find('com/')+4:],i))
        count+=1
    return container

ad='🔥 Get more likes & comments by joining our other groups👇 \n \
❤️Happy engaging❤️ \n \
🚀Viral Network🚀'

keyboard = [[InlineKeyboardButton("🔥   Rules   🔥", url='https://t.me/viralnetworkchannel', callback_data='1'),
                 InlineKeyboardButton("📄   List    📄", url='https://t.me/hoai97nambot',callback_data='2')],

                [InlineKeyboardButton("💎   Premium User    💎", url='https://t.me/johntendo', callback_data='3')]]

reply_markup = InlineKeyboardMarkup(keyboard)

list_markup = [[InlineKeyboardButton("🚀 Dx30 Follow Group 🚀", url='https://t.me/follownetwork30')]]
reply_markup1 = InlineKeyboardMarkup(list_markup)
# Define a few command handlers. These usually take the two arguments update and
# context. Error handlers also receive the raised TelegramError object in error.
def start(update, context):
    """Send a message when the command /start is issued."""
    m='📋 Profiles List 📋 \n Follow the following users to join the list\n'
    k=get_list()
    for i in k:
        m=m+ '\n'+i
    m=m+'\n\n ➖➖➖➖➖➖➖➖➖➖\nWhen you’re done, drop your instagram profile in this format:\n\
        Example: dx30 taylorswift or Dx30 taylorswift'
    send_to_destination(update.message.from_user.id, m)
    auto_delete_message(update.message.message_id)    
    return 0

def list_command(update, context):
    """Send a message when the command /start is issued."""
    m='📋 Profiles List 📋 \n Follow the following users to join the list\n'
    k=get_list()
    for i in k:
        m=m+ '\n'+i
    m=m+'\n\n ➖➖➖➖➖➖➖➖➖➖\nWhen you’re done, drop your instagram profile in this format:\n\
        Example: dx30 taylorswift or Dx30 taylorswift'
    send_to_destination(update.message.from_user.id, m)
    auto_delete_message(update.message.message_id)    
    return 0

def help_command(update, context):
    """Send a message when the command /help is issued."""   
    update.message.reply_text(str(update.message.message_id) +'-'+ \
        update.message.from_user.username+'-'\
        +str(update.message.from_user.id))
    time.sleep(3)
    auto_delete_message(update.message.message_id)

#==========================================================================================
def echo(update, context): # important info in this function
    """Echo the user message."""
    aa=update.message.text # get typed link ⚠️
   
    if aa[:4] == 'dx30' or aa[:4] == 'Dx30':
        # check bunch of of conditions
        if check_repost(aa[5:]) and get_and_extract(aa[5:]):
            tele_usr='@'+ update.message.from_user.username
            bot_push_message(aa,tele_usr)
            # tidy user's message
            time.sleep(5)
            auto_delete_message(update.message.message_id)
        else:
            update.message.reply_text('Please check following reasons:\n \
                ❗️ No enough follow \n \
                ❗️ Input link with non-exist profile \n \
                ❗️ Wrong syntax',reply_markup=reply_markup1)
            auto_delete_message(update.message.message_id)
            time.sleep(5)
            auto_delete_message(update.message.message_id+1)
    # auto drop functions
    elif aa[:4]=='drop' and check_repost(aa[5:]):
        bot_push_message(aa,'@'+update.message.from_user.username,auto_drop=True)   
        auto_delete_message(update.message.message_id)     
    else:
        update.message.reply_text('Wrong syntax ❗️❗️❗️ \n Please check again or read our rules',reply_markup=reply_markup1) 
        auto_delete_message(update.message.message_id)
        time.sleep(3)
        auto_delete_message(update.message.message_id+1)

def send_to_destination(des,mess):
    # destination = chat name with @:format
    # use to send toward user 
    obj=Bot(token=TOKEN)
    obj.send_message(des,mess,parse_mode='Markdown',disable_web_page_preview=True,reply_markup=reply_markup1)

def auto_send_message(st):
    obj=Bot(token=TOKEN)
    obj.send_message(GROUP,st,parse_mode='Markdown',disable_web_page_preview=True,reply_markup=reply_markup)

def bot_push_message(link, user,auto_drop=False):
    #trim input link
    obj=Bot(token=TOKEN)
    sub_link = link[5:]
    link = 'https://www.instagram.com/' + sub_link
    if auto_drop == True:
        # auto drop
        me='🌟 '+user+ ' ✅ '+' Dx30 [{}]({})'.format(sub_link,link)
    else: 
        me='👤 '+user+ ' ✅ '+' Dx30 [{}]({})'.format(sub_link,link)
    print(me)
    obj.send_message(GROUP,me, parse_mode='Markdown',disable_web_page_preview=True,reply_markup=reply_markup)
# this scripts used for testing 👤entrepreneurs_club01 ✅

def auto_delete_message(mess_id):
    obj=Bot(token=TOKEN)
    try:
        obj.delete_message(GROUP,mess_id)
    except:
        print('message haven\'t been deleted yet')

def extract_usr(a):
    # get username from instagram url
    lit=[]
    for i in a:
        c=i[1]
        lit.append(c[c.find('com/')+4:])
    return lit

def get_and_extract(prf):
    lit=get_links_from_file(get_username=True)
    r=check_follow_yet(prf,lit)
    return r

def check_repost(usrname_in_repost_link):
    # check if a link  is able to repost
    sample = get_links_from_file(get_username=True)
    if usrname_in_repost_link in sample:
        return 0
    return 1

def send_notify(content,mess_id):
    obj=Bot(token=TOKEN)
    try:
        obj.send_message(GROUP,content)
        time.sleep(5)
        obj.delete_message(GROUP,mess_id)
    except:
        print('message haven\'t been sent/deleted yet')
        
def main():
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    updater = Updater(TOKEN, use_context=True)
    # obj=Bot(token='1098222229:AAE27CLsIN1xPwoDcjrBbz-z34lualgzbB4')
    # st='📸 '+ a[-1]
    # obj.send_message('@innertest',st, reply_markup=reply_markup)
   
    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("list", list_command))
    # on noncommand i.e message - echo the message on Telegram
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))
    #dp.add_handler(MessageHandler(Filters.regex('^1$'),start))
    #conv_handler=ConversationHandler(entry_points=[CommandHandler('start',start)],\
    #    states={0:[CallbackQueryHandler(start,pattern='^1$')]},fallbacks=[CommandHandler('start',start)])
    #dp.add_handler(conv_handler)
    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()
    

if __name__ == '__main__':
    main()
