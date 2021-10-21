import os
from urllib.parse import urlparse

import requests
from dotenv import load_dotenv

load_dotenv()


def define_ext(url):
  url_parsed = urlparse(url)
  file_ext = os.path.splitext(url_parsed.path)[1]
  return file_ext


def download_file(directory, url, quantity):
  if not os.path.exists(directory):
      try:
          os.makedirs(directory)
      except OSError as error:
          if error.errno != errno.EEXIST:
              raise
  file_ext = define_ext(url)
  filename = f"{directory}/spacex{quantity}{file_ext}"
  response = requests.get(url)
  response.raise_for_status()
  with open(filename, 'wb') as file:
      file.write(response.content)


def fetch_spacex_last_launch():
  space_x_API_url = 'https://api.spacexdata.com/v3/launches/67'
  response = requests.get(space_x_API_url)
  photo_links = response.json()["links"]["flickr_images"]
  for photo_number, url in enumerate(photo_links):
    download_files = download_file("images", url, photo_number)

def main():
    spacex_photos = fetch_spacex_last_launch()


if __name__ == '__main__':
    main()
