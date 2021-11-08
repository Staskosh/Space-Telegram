import os
import time
from os import listdir

import telegram
from dotenv import load_dotenv


def publish_images(directory, bot, chat_id, photos):
    while True:
        for photo in photos:
            time.sleep(86400)
            with open(f'{directory}/{photo}', 'rb') as photo:
                bot.send_photo(chat_id=chat_id, photo=photo, timeout=100)


def main():
    load_dotenv()
    directory = os.getenv('PHOTO_FOLDER')
    bot = telegram.Bot(token=os.getenv('TG_TOKEN'))
    chat_id = os.getenv('TG_CHAT_ID')
    photos = listdir(directory)
    publish_images(directory, bot, chat_id, photos)


if __name__ == '__main__':
    main()
