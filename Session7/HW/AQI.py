from urllib.request import urlopen
from bs4 import BeautifulSoup
import json
#step 1: Creat connection:
capital = input("Choice a capital: ")
url = "https://wind.waqi.info/nsearch/full/{}?n=4".format(capital)
conn = urlopen(url)
#step 2: Download page
raw_data = conn.read()
page_content = raw_data.decode("utf8")

data_aqi = json.loads(page_content)
time = data_aqi['results'][0]['s']['t'][0]
AQI = data_aqi['results'][0]['s']['a']
location = data_aqi['results'][0]['s']['n'][0]
#KQ:
print("-------------------------------------")
print("Location: ",location)
print("Time: ",time)
print("AQI: ",AQI)
print("-------------------------------------")



