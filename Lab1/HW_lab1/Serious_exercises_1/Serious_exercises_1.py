from urllib.request import urlopen
from bs4 import BeautifulSoup
from youtube_dl import YoutubeDL

#Step 1: Creat connection
url = "https://www.apple.com/itunes/charts/songs/"
conn = urlopen(url)

#Step 2: Download page
raw_data = conn.read()
page_content = raw_data.decode("utf8")
#Muốn tạo file html-> lưu file dantri.html dươi dạng raw_data
with open("apple.html", "wb") as f: 
    f.write(raw_data)
#Step 3: Find ROI(vùng quan tâm)
soup = BeautifulSoup(page_content, "html.parser")
section = soup.find("section", "section chart-grid")
div = section.find("div")
# print(soup)
#Step 4: Extract ROI
li_list = div.ul.find_all("li")
new_list = []
for li in li_list:
    h3 = li.h3
    a = h3.a
    name = a.string

    h4 = li.h4
    a = h4.a
    artist = a.string

    songs = {
        "name":name,
        "artist":artist,
    }
    new_list.append(songs)


#Step 5: save data(excel)
import pyexcel
pyexcel.save_as(records=new_list, dest_file_name="Topsongs.xlsx")


#ý 2:
options = {
    "default_search":"ytsearch",
    # bảo người tải xuống tìm kiếm thay vì tải xuống trực tiếp
    "max_downloads": 1,
    # Yêu cầu người tải xuống chỉ tải xuống mục đầu tiên (âm thanh)
    "format":"bestaudio/audio",
}
dl = YoutubeDL(options)
for i in new_list:
    dl.download(i["name"])

