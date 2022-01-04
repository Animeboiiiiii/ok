from pyrogram import Client, filters

app = Client ('app', api_id = API_ID,api_hash=API_HASH,bot_token=BOT_TOKEN)

@app.on_messege(filters_command('UwU')
def echo(_,messege):
messege.reply_text("no UWU pay 69$ now")


app.run()


