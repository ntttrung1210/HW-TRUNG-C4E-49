from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.action_chains import ActionChains
import pandas as pd
import matplotlib.pyplot as plt 
import random
import numpy as np
browser=webdriver.Chrome()
browser.get('https://www.cophieu68.vn/?fbclid=IwAR2dp7n5-OpjFYOzaH9KMItWw7_QH5op7g6xtMSZvFEUOW7e48kbN5kMh28')
time.sleep(2)
ele=browser.find_element_by_xpath("//*[contains(text(),' Đăng nhập')]")
ele.click()
ele=browser.find_element_by_xpath("//input[@name='username']")
time.sleep(2)
ele.send_keys('ntttrung1210@gmail.com')
ele=browser.find_element_by_xpath("//input[@name='tpassword']")
time.sleep(2)
ele.send_keys('123456'+Keys.RETURN)
time.sleep(2)
ele=browser.find_element_by_xpath("//*[contains(text(),'Dịch vụ Dữ Liệu')]")
ele.click()
ele=browser.find_elements_by_tag_name()
for i in ele:
    try:
        d=i.find_element_by_xpath("//*[contains(text(),'VNINDEX')]")
        k=i
    except:
        pass
print(k)
# browser.close()
# dataset=pd.read_csv('excel_^vnindex.csv')
# dataset.head(20)
# x=dataset.head(20).iloc[:,2].values
# y=[]
# for i in range(20):
#     y.append(i)
# plt.figure(figsize=(15,5))
# plt.plot(y,x)
# plt.show

