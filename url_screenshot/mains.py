#! /usr/bin/env python3

import json
import time
import urllib.request

API_KEY = input("Enter your page2images API_KEY : ")
API_URL = 'http://api.page2images.com/restfullink'
basic = 'http://api.page2images.com/restfullink?'
link = input("Enter the url of the page that you wanna take a Screenshot : ")

url = basic + 'p2i_url=' + link + '&p2i_key=' + API_KEY
print("Fetching the Screenshot of " + link + ".....")

while (1):
	time.sleep(1)
	print("Loading ..... ")
	request = urllib.request.urlopen(url).read().decode('utf-8')
	jsondata = json.loads(request)
	if (jsondata['status'] == 'finished'):
		print('The url of the Screenshot is : ' + jsondata['image_url'])
		x = input("Do you want to download it? (y/n)")
		if(x == 'y'):
			file = input("Give the name for the generated png image:\n")
			filename = file + '.png'
			urllib.request.urlretrieve( jsondata['image_url'] , filename )
			print("Your png file has been saved as " + filename)
		break
