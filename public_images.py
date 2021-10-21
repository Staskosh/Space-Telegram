import os
import time
from os import listdir

import telegram
from dotenv import load_dotenv

load_dotenv()
bot = telegram.Bot(token=os.getenv('TOKEN'))
updates = bot.get_updates()


def public_images():
  all_photos = listdir("images")
  while True:
    for number in range(len(all_photos)):
      time.sleep(86400)
      bot.send_photo(chat_id=os.getenv('CHAT_ID'), photo=open(f'images/{all_photos[number]}', "rb"), timeout=100)


def main():
    photo_post = public_images()


if __name__ == '__main__':
    main()
