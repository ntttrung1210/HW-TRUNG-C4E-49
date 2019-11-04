# Exercise 1

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import xlsxwriter 
from youtube_dl import YoutubeDL
import time
workbook = xlsxwriter.Workbook('top100song.xlsx')
worksheet=workbook.add_worksheet()
browser=webdriver.Chrome()
browser.get("https://music.apple.com/us/playlist/top-100-global/pl.d25f5d1181894928af76c85c967f8f31")
time.sleep(2)
song=[]
musician=[]
for i in range(1330,2619,13):
    id1='ember'+str(i)
    song.append(browser.find_element_by_id(id1).text)
for i in range(1331,2619,13):
    id1='ember'+str(i)
    musician.append(browser.find_element_by_id(id1).text)
worksheet.write('A1','Song')
worksheet.write('B1','Musician')
for i in range(100):
    new_row_1='A'+str(i+2)
    new_row_2='B'+str(i+2)
    worksheet.write(new_row_1,song[i])
    worksheet.write(new_row_2,musician[i])
browser.close()
workbook.close() 
options = {
    'default_search': 'ytsearch', 
    'max_downloads': 1 
}
dl = YoutubeDL(options)
for i in range(100):
    dl.download([str(song[i])+str(musician[i])])




# #Exercise 2

# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# import time
# import xlsxwriter
# from selenium.webdriver.common.action_chains import ActionChains
# workbook=xlsxwriter.Workbook('bao_cao_tai_chinh.xlsx')
# worksheet=workbook.add_worksheet()
# browser=webdriver.Chrome()
# browser.get('http://s.cafef.vn/bao-cao-tai-chinh/VNM/IncSta/2017/3/0/0/ket-qua-hoat-dong-kinh-doanh-cong-ty-co-phan-sua-viet-nam.chn')
# time.sleep(2)
# worksheet.write("A1","Trước           Sau")
# worksheet.write("B1","Quý 4-2016")
# worksheet.write("C1","Quý 1-2017")
# worksheet.write("D1","Quý 2-2017")
# worksheet.write("E1","Quý 3-2017")
# ele1=browser.find_elements_by_class_name('r_item ')
# l=[]
# for j in ele1:
#     d=j.find_elements_by_xpath("//*[@class='b_r_c']")
#     for k in d:
#         try:
#              g=k.text
#              l.append(g)
#         except Exception as ex:
#             print(ex)
# j=1
# for i in range(1,140,6):
#     j=j+1
#     worksheet.write("A"+str(j),l[i])
# j=1
# for i in range(2,141,6):
#     j=j+1
#     worksheet.write("B"+str(j),l[i])
# j=1
# for i in range(3,142,6):
#     j=j+1
#     worksheet.write("C"+str(j),l[i])
# j=1
# for i in range(4,143,6):
#     j=j+1
#     worksheet.write("D"+str(j),l[i])
# j=1
# for i in range(5,144,6):
#     j=j+1
#     worksheet.write("E"+str(j),l[i])
# workbook.close()
# browser.close()


