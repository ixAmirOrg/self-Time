###################################
# Coded By ===> ixAmirCom
# Telegram ID ===> T.me/ixAmirCom
###################################

from telethon import TelegramClient, events, sync, errors,utils
from telethon.tl.functions.account import UpdateProfileRequest
import aiocron
import asyncio
import pytz
import datetime
import logging
import time
import os
import random

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',level=logging.INFO)

logger = logging.getLogger(__name__)


api_id = 000000 #api id

api_hash = "000000" #api hash

admin = 000000 # id admin ba @


client = TelegramClient("data", api_id, api_hash)


ik = 0

@client.on(events.NewMessage(from_users=admin, pattern="add:")) 
async def wait_hours(event):
	global ik
	tsxt = event.raw_text
	tsxt = tsxt.replace("add:","")
	ik = int(tsxt)

@client.on(events.NewMessage(from_users=admin, pattern="help")) #id admin
async def wait_hours(event):
	client.send_message(event.chat_id, """☾︎ Coded By @ixAmirCom   ☽︎
☾︎									 ☽︎
☾︎ add:							  ☽︎
☾︎ ba in dastorige saat	   ☽︎
☾︎ agab oftad bebaridesh   ☽︎
☾︎ jolo mesal :				   ☽︎
☾︎ add:1							☽︎""")

@aiocron.crontab('*/1 * * * *')
async def clock():
	global ik
	fonts = [
	{"0":"⁰","1":"¹","2":"²","3":"³","4":"⁴","5":"⁵","6":"⁶","7":"⁷","8":"⁸","9":"⁹"},
	{"0":"𝟘","1":"𝟙","2":"𝟚","3":"𝟛","4":"𝟜","5":"𝟝","6":"𝟞","7":"𝟟","8":"𝟠","9":"𝟡"},
	{"0":"⓪","1":"①","2":"②","3":"③","4":"④","5":"⑤","6":"⑥","7":"⑦","8":"⑧","9":"⑨"},
	{"0":"𝟎","1":"𝟏","2":"𝟐","3":"𝟑","4":"𝟒","5":"𝟓","6":"𝟔","7":"𝟕","8":"𝟖","9":"𝟗"},
	{"0":"⊘","1":"𝟏","2":"ϩ","3":"Ӡ","4":"५","5":"Ƽ","6":"Ϭ","7":"7","8":"𝟖","9":"९"},
	{"0":"ʘ","1":"➀","2":"➁","3":"❸","4":"❹","5":"❺","6":"６","7":"❼","8":"❽","9":"９"},
	{"1":"♳","2":"♴","3":"♵","4":"♶","5":"♷","6":"♸","7":"♹"},
	{"1":"⓵","2":"⓶","3":"⓷","4":"⓸","5":"⓹","6":"⓺","7":"⓻","8":"⓼","9":"⓽","0":"¤"},
	{"1":"1̴̴","2":"ᆯ","3":"Յ","4":"Վ","5":"Ƽ","6":"Դ","7":"ᆨ","8":"Ց","9":"ะ9ะ","0":"ᅙ"},
	{"1":"【1】","2":"【2】","3":"【3】","4":"【4】","5":"【5】","6":"【6】","7":"【7】","8":"【8】","9":"【9】","0":"【0】"}
	]
	d = datetime.now(pytz.timezone("Asia/Tehran"))
	h = d.strftime("%M")
	h1 = int(h)
	h2 = h1 + ik
	if len(str(h2)) == 1:
		h2 = "0" + str(h2)
	await client(UpdateProfileRequest(first_name = 'AᴍɪʀAʟɪ ' + d.strftime("%H : ").translate(str.maketrans(random.choice(fonts))) + str(h2).translate(str.maketrans(random.choice(fonts)))))   
			
			
clock.start()	
client.start()
client.run_until_disconnected()
