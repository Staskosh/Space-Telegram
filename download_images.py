import os
from urllib.parse import urlparse

import requests


def define_photo_name(url, source_name, photo_number):
    parsed_url = urlparse(url)
    file_ext = os.path.splitext(parsed_url.path)[1]
    filename = f'{source_name}{photo_number}.{file_ext}'
    return filename


def download_file(directory, url, source_name, photo_number, payload):
    filename = define_photo_name(url, source_name, photo_number)
    file_path = f'{directory}/{filename}'
    response = requests.get(url, params=payload)
    response.raise_for_status()
    with open(file_path, 'wb') as file:
        file.write(response.content)
