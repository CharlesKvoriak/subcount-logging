from bs4 import BeautifulSoup
import requests

r = requests.get("https://socialblade.com/youtube/user/carykh/realtime")

soup = BeautifulSoup(r, 'html.parser')