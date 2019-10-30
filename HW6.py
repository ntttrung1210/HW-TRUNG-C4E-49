from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
browser=webdriver.Chrome()
browser.get("https://ctt-daotao.hust.edu.vn/")
time.sleep(2)
ele=browser.find_element_by_xpath("//*[contains(text(),'Dành cho Giảng viên/Sinh viên/Phụ huynh')]")
ele.click()
ele=browser.find_element_by_xpath("//input[@id='ctl00_ctl00_contentPane_MainPanel_MainContent_tbUserName_I']")
time.sleep(2)
ele.send_keys('20184318')
ele=browser.find_element_by_xpath("//input[@id='ctl00_ctl00_contentPane_MainPanel_MainContent_tbPassword_I_CLND']")
time.sleep(2)
ele.send_keys('1234')