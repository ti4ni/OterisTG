from pyrogram import Client, filters  # телеграм клиент

# Создать можно на my.telegram.org
API_ID =   # API_ID с сайта
API_HASH = ''  # API_HASH с сайта

PUBLIC_PUBLIC = ''  # паблик, куда будет репоститься
SOURCE_PUBLICS = [
    # паблики, откуда будут браться посты
    '',

]
PHONE_NUMBER = ''  # номер, на который зарегистрирован тг

# создаем клиент телеграм
app = Client("", api_id=API_ID, api_hash=API_HASH,
             phone_number=PHONE_NUMBER)

@app.on_message(filters.chat(SOURCE_PUBLICS))
def new_channel_post(client, message):

    # пересылаем пост
    message.copy(PUBLIC_PUBLIC)



app.run()  # запускает скрипт