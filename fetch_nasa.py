import os

import requests
from dotenv import load_dotenv
from download_images import download_file
from datetime import datetime


def fetch_APOD_last_days(directory, API_KEY_NASA):
  url = 'https://api.nasa.gov/planetary/apod/'
  payload = {'api_key': API_KEY_NASA,
             'count': 50, }
  response = requests.get(url, params=payload)
  response.raise_for_status()
  for photo_number, photo_link in enumerate(response.json()):
      url = photo_link['url']
      download_files = download_file(directory, url, photo_number, payload)


def fetch_EPIC(directory, API_KEY_NASA):
  url_original = 'https://epic.gsfc.nasa.gov/api/natural'
  response = requests.get(url_original)
  response.raise_for_status()
  for photo_number, parameter in enumerate(response.json()):
    date_of_photo = parameter['date']
    #date2 = date_of_photo.strftime('%d/%m/%y')
    image = parameter['image']
    date_parameters = datetime.strptime(parameter['date'], '%Y-%m-%d %H:%M:%S')
    payload = {'api_key': API_KEY_NASA }
    photo_url = f'https://api.nasa.gov/EPIC/archive/natural/{date_parameters.year}/{date_parameters.month}/{date_parameters.day}/png/{image}.png'
    download_files = download_file(directory, photo_url, photo_number, payload)


def main():
    load_dotenv()
    API_KEY_NASA = os.getenv('API_KEY_NASA')
    directory = os.getenv('PHOTO_FOLDER')
    #fetch_APOD_last_days(directory, API_KEY_NASA)
    fetch_EPIC(directory, API_KEY_NASA)


if __name__ == '__main__':
    main()
