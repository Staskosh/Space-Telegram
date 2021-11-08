import os

import requests
from dotenv import load_dotenv
from download_images import download_file, make_directory


def fetch_spacex_launch(directory, launch_number):
    api_url = f'https://api.spacexdata.com/v3/launches/{launch_number}'
    source_name = 'spacex'
    response = requests.get(api_url)
    response.raise_for_status()
    photo_links = response.json()['links']['flickr_images']
    for photo_number, url in enumerate(photo_links):
        download_file(directory, url, source_name, photo_number)


def main():
    load_dotenv()
    launch_number = 67
    directory = os.getenv('PHOTO_FOLDER')
    os.makedirs(directory, exist_ok=True)
    fetch_spacex_launch(directory, launch_number)


if __name__ == '__main__':
    main()
