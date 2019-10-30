from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
browser=webdriver.Chrome()
act=ActionChains
browser.get("https://music.apple.com/us/playlist/top-100-global/pl.d25f5d1181894928af76c85c967f8f31")
time.sleep(2)
ele=browser.find_elements_by_xpath("//li[@class='we-selectable-item is-available we-selectable-item--allows-interaction ember-view tracklist-item tracklist-item--song  song-list-row']")
list_music=[]
for i in ele:
    try:
        d={"name_song":i.find_element_by_xpath("//div[@class='spread']").text}
        list_music.append(d)
    except Exception as ex:
        print(ex)
print(list_music)
browser.close()