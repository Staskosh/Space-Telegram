import os
import time
from os import listdir

import telegram
from dotenv import load_dotenv


def public_images(directory, bot):
  all_photos = listdir(directory)
  while True:
    for number in range(len(all_photos)):
      time.sleep(3)
      with open(f'{directory}/{all_photos[number]}', "rb") as g:
          bot.send_photo(chat_id=os.getenv('TG_CHAT_ID'), photo=g, timeout=100)


def main():
    load_dotenv()
    directory = input('Введите название папки из которой необходимо опубликовать фото')
    bot = telegram.Bot(token=os.getenv('TG_TOKEN'))
    updates = bot.get_updates()
    photo_post = public_images(directory, bot)


if __name__ == '__main__':
    main()
