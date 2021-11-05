import os
import time
from os import listdir

import telegram
from dotenv import load_dotenv


def publish_images(directory, bot, all_photos):
  while True:
    for photo in all_photos:
      time.sleep(86400)
      with open(f'{directory}/{photo}', 'rb') as photo:
          bot.send_photo(chat_id=os.getenv('TG_CHAT_ID'), photo=photo, timeout=100)


def main():
    load_dotenv()
    directory = os.getenv('PHOTO_FOLDER')
    bot = telegram.Bot(token=os.getenv('TG_TOKEN'))
    all_photos = listdir(directory)
    publish_images(directory, bot, all_photos)


if __name__ == '__main__':
    main()
