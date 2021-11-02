import os

import requests
from dotenv import load_dotenv
from download_images import download_file

def fetch_spacex_given_launch(directory, launch_number):
  space_x_API_url = f'https://api.spacexdata.com/v3/launches/{launch_number}'
  response = requests.get(space_x_API_url)
  response.raise_for_status()
  photo_links = response.json()['links']['flickr_images']
  for photo_number, url in enumerate(photo_links):
    payload = None
    download_files = download_file(directory, url, photo_number, payload)

def main():
    load_dotenv()
    launch_number = 67
    directory = os.getenv('PHOTO_FOLDER')
    fetch_spacex_given_launch(directory, launch_number)


if __name__ == '__main__':
    main()
