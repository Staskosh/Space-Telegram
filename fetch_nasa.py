import os
from datetime import datetime

import requests
from dotenv import load_dotenv
from download_images import download_file, make_directory


def fetch_apod_last_days(directory, api_key_nasa):
    url = 'https://api.nasa.gov/planetary/apod/'
    source_name = 'nasa_apod'
    payload = {'api_key': api_key_nasa,
               'count': 50, }
    response = requests.get(url, params=payload)
    response.raise_for_status()
    for photo_number, photo_link in enumerate(response.json()):
        url = photo_link['url']
        download_file(directory, url, source_name, photo_number, payload)


def fetch_epic(directory, api_key_nasa):
    original_url = 'https://epic.gsfc.nasa.gov/api/natural'
    source_name = 'nasa_epic'
    response = requests.get(original_url)
    response.raise_for_status()
    for photo_number, photo_data in enumerate(response.json()):
        image = photo_data['image']
        date = datetime.strptime(photo_data['date'], '%Y-%m-%d %H:%M:%S')
        formatted_date = date.strftime('%Y/%m/%d')
        payload = {'api_key': api_key_nasa}
        photo_url = 'https://api.nasa.gov/EPIC/archive/' \
                    f'natural/{date_parameters_formatted}/png/{image}.png'
        download_file(directory, photo_url, source_name, photo_number, payload)


def main():
    load_dotenv()
    api_key_nasa = os.getenv('API_KEY_NASA')
    directory = os.getenv('PHOTO_FOLDER')
    os.makedirs(directory, exist_ok=True)
    fetch_apod_last_days(directory, api_key_nasa)
    fetch_epic(directory, api_key_nasa)


if __name__ == '__main__':
    main()
