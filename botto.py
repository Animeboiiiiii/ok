from pyrogram import Client, filters
import os

TOKEN = os.environ.get('TOKEN')
API_ID = os.environ.get('API_ID')
API_HASH = os.environ.get('API_HASH')

app = Client ('app', api_id = API_ID,api_hash=API_HASH,bot_token=TOKEN)

@app.on_message(filters.command('UwU'))
def echo(_,messege):
    messege.reply_text("no UWU pay 69$ now")

@app.on_message(filters.command('info'))
def info(_, message):
    usr = message.from_user
    caption = f"<b>User ID:</b> {usr.id}\n"
    caption += f"<b>Username:</b> {usr.username}\n"
    caption += f"<b>Is A Bot?:</b> {usr.is_bot}\n"
    caption += f"<b>Status:</b> {usr.status}\n"
    caption += f"<b>DC id:</b> {usr.dc_id}\n"
    message.reply_text(caption)

@app.on_message(filters.command('ginfo'))
def ginfo(_,message):
cht = message.chat
Chat profile:{cht.photo}
caption += f"<b>Chat ID:<\b>{cht.id}
caption += f"<b>Chat  Type:<\b>{cht.type}
caption += f"<b>Chat name:<\b>{cht.title}
caption += f"<b>Chat username:<\b>{cht.username}
caption += f"<b>Bio:<\b>{cht.discription}

app.run()

