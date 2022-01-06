from pyrogram import Client, filters
import os

TOKEN = os.environ.get('TOKEN')
API_ID = os.environ.get('API_ID')
API_HASH = os.environ.get('API_HASH')

app = Client ('app', api_id = API_ID,api_hash=API_HASH,bot_token=TOKEN)

@app.on_messege(filters_command('UwU'))
def echo(_,messege):
    messege.reply_text("no UWU pay 69$ now")


app.run()


