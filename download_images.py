import os
from urllib.parse import urlparse

import requests


def define_ext(url):
  url_parsed = urlparse(url)
  file_ext = os.path.splitext(url_parsed.path)[1]
  return file_ext


def download_file(directory, url, quantity, payload):
  if not os.path.exists(directory):
      try:
          os.makedirs(directory)
      except OSError as error:
          if error.errno != errno.EEXIST:
              raise
  file_ext = define_ext(url)
  filename = f'{directory}/spacex{quantity}{file_ext}'
  response = requests.get(url, params=payload)
  response.raise_for_status()
  with open(filename, 'wb') as file:
      file.write(response.content)