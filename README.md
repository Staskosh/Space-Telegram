# Space Telegram

This script allows downloading photos from SpaceX, NASA, and posting such kind of files on your own Telegram channel.

### How to install

- Download the code.
- Python3 should be already installed. 
- Install virtual enviriment
- Get API Key for [NASA](https://api.nasa.gov). Write it in the file '.ENV' as
  ```python
  API_KEY_NASA='here is your api key'
  ```
- Create a chat bot in [Telegram](https://way23.ru/регистрация-бота-в-telegram.html). Now you have the token. Write it in the file '.ENV' as
  ```python
  TG_TOKEN='here is your token'
  ```
- Create a [new channel in Telegram](https://smmplanner.com/blog/otlozhennyj-posting-v-telegram/) and get a chat id. Now you have the chat id. Write it in the file '.ENV' as
  ```python
  TG_CHAT_ID='here is your chat id'
  ```
- Then use `pip` (or `pip3`, if there is a conflict with Python2) to install dependencies:
```python
pip install -r requirements.txt
```
## How to use

- For downloading photos from SpaceX use the command:
```python
python3 fetch_spacex.py
```
- For downloading photos from NASA use the command:
```python
python3 fetch_nasa.py
```
- Publish one of the downloaded photos once a day on your Telegram channel:
```python
python3 publish_images.py
```

### Project Goals

The code is written for educational purposes on online-course for web-developers [dvmn.org](https://dvmn.org/).