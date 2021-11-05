import os
from urllib.parse import urlparse

import requests


def define_photo_name(url, source_name, quantity):
    url_parsed = urlparse(url)
    file_ext = os.path.splitext(url_parsed.path)[1]
    filename = f'{source_name}{quantity}.{file_ext}'
    return filename


def make_directory(directory):
    os.makedirs(directory, exist_ok=True)


def download_file(directory, url, source_name, quantity, payload):
    filename = define_photo_name(url, source_name, quantity)
    file_path = f'{directory}/{filename}'
    response = requests.get(url, params=payload)
    response.raise_for_status()
    with open(file_path, 'wb') as file:
        file.write(response.content)
