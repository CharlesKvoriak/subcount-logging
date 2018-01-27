from bs4 import BeautifulSoup
import requests
import os.path

def getsubcount(user):
	r = requests.get("https://socialblade.com/youtube/user/"+user+"/realtime")

	html = r.text

	soup = BeautifulSoup(html, 'html.parser')

	countline = soup.find(id="rawCount")

	count = str(countline.string)

	return count

def log(user):
	writepath = "log.csv"
	mode = 'a' if os.path.exists(writepath) else 'w'

	with open(writepath, mode) as f:
    	f.write('subscriber data for'+user+'\n')