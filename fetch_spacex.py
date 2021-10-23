import requests
from download_images import download_file

def fetch_spacex_last_launch(directory):
  space_x_API_url = 'https://api.spacexdata.com/v3/launches/67'
  response = requests.get(space_x_API_url)
  photo_links = response.json()["links"]["flickr_images"]
  for photo_number, url in enumerate(photo_links):
    download_files = download_file(directory, url, photo_number)

def main():
    directory = input('Введите название папки для скачивания фото')
    spacex_photos = fetch_spacex_last_launch(directory)


if __name__ == '__main__':
    main()
