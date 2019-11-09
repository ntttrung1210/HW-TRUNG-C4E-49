from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.action_chains import ActionChains
import pandas as pd
import numpy as np
from flask import Flask, render_template
def get_ticker_data(ticker_id):
    rfile='excel_'+str(ticker_id.lower())+str('.csv')
    return pd.read_csv(rfile,encoding='utf-8', header=None, sep=',')
def get_ticker_data_by_field(ticker_id,fields):
    rfile='excel_'+str(ticker_id.lower())+str('.csv')
    data = pd.read_csv(rfile,encoding='utf-8', header=None, sep=',')
    return data[fields]
ls_id=['AAA','AAM','AAV','ABC','ABI','ABR','ABT','HSG','VIC','VIB','VID','VIN','HOT','FLC']
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
browser.get('https://www.cophieu68.vn/export.php')
time.sleep(2)
for v in range(len(ls_id)):
    name='https://www.cophieu68.vn/export/excelfull.php?id='+str(ls_id[v])
    browser.get(name)
app = Flask(__name__)
@app.route('/')
def list_name():
    return render_template('list_id.html',data=ls_id,a=len(ls_id))
@app.route('/data/<ticker_id>')
def data_id(ticker_id):  
    ls=[]
    data1=get_ticker_data(ticker_id)
    ls=data1[:len(data1)].values
    return render_template('printdata.html',data=ls,a=len(ls),b=len(ls[0]))
@app.route('/predict')
def predict_stock():
    ls_id_new=[]
    for v in range(len(ls_id)):
        data1=get_ticker_data(ls_id[v])
        ls=data1.head(20).iloc[:,10].values
        dk=0
        for i in range(1,len(ls)):
            ls[i]=float(ls[i])
        for i in range(1,3):
            if ls[i]>ls[i+1]:
                dk=1
            else:
                dk=0
                break
        sum=0
        if dk==1:
            for i in range(2,14):
                sum=sum+ls[i]
            sum=sum/12
            if ls[1]>sum:
                ls_id_new.append(ls_id[v])
    return render_template('list_id.html',data=ls_id_new,a=len(ls_id_new))
if __name__ == '__main__':
  app.run(host='127.0.0.1', port=8000, debug=True)
 