import os

import requests
from dotenv import load_dotenv
from dowload_images import download_file


def fetch_APOD_last_days():
  url = "https://api.nasa.gov/planetary/apod/"
  payload = {"api_key": os.getenv('API_KEY_NASA'),
             "count": 50, }
  response = requests.get(url, params=payload)
  photo_links = response.json()
  urls = []
  for photo_link in photo_links:
    url = photo_link["url"]
    photo_urls = urls.append(url)
  for photo_number, url in enumerate(urls):
    download_files = download_file("images", url, photo_number)


def fetch_EPIC():
  url_original = "https://epic.gsfc.nasa.gov/api/natural"
  response = requests.get(url_original)
  photo_urls = []
  for parameter in response.json():
    image = parameter["image"]
    year = parameter["date"][:4]
    month = parameter["date"][5:7]
    day = parameter["date"][8:10]
    photo_url = f'https://api.nasa.gov/EPIC/archive/natural/{year}/{month}/{day}/png/{image}.png?api_key=DEMO_KEY'
    photo_urls.append(photo_url)
  for photo_number, url in enumerate(photo_urls):
      download_files = download_file("images", url, photo_number)


def main():
    load_dotenv()
    apod_photos = fetch_APOD_last_days()
    epic_photos = fetch_EPIC()


if __name__ == '__main__':
    main()
