from urllib.request import urlopen
from bs4 import BeautifulSoup
from youtube_dl import YoutubeDL

#Step 1: Creat connection
url = "http://s.cafef.vn/bao-cao-tai-chinh/VNM/IncSta/2017/3/0/0/ket-qua-hoat-dong-kinh-doanh-cong-ty-co-phan-sua-viet-nam.chn"
conn = urlopen(url)

#Step 2: Download page
raw_data = conn.read()
page_content = raw_data.decode("utf8")
#Muốn tạo file html-> lưu file dantri.html dươi dạng raw_data
with open("scafe.html", "wb") as f: 
    f.write(raw_data)
#Step 3: Find ROI(vùng quan tâm)
soup = BeautifulSoup(page_content, "html.parser")
table = soup.find("table", id = "tableContent")
# print(soup)
#Step 4: Extract ROI
td_list = table.find_all("td","b_r_c")
news_list = []
for k in td_list:
    data = k.string
    news = {"Kết quả hoạt động kinh doanh": data}
    news_list.append(data)
#Step 5: save data(excel)
import pyexcel
pyexcel.save_as(records=news_list, dest_file_name="ROI.xlsx")


