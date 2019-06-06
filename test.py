from selenium.webdriver import ActionChains
from selenium import webdriver
from time import sleep

import random
import time
import csv
import re

class Loginfo(object):
    def __init__(self):
        fname=time.strftime('%Y-%m-%d',time.gmtime())
        print(fname)
        self.log=open(fname+".txt",'w')

    def log_write(self,msg):
        self.log.write(msg)

    def log_close(self):
        self.log.close()

def login(bs):
    user = bs.find_element_by_xpath('//input[@name="pwuser"]')
    userdata = csv.reader(open('userdata.csv', encoding='utf-8'))
    for row in userdata:
        user.send_keys(row[0])
        sleep(0.5)
        pwd = bs.find_element_by_xpath('//input[@name="pwpwd"]')
        pwd.send_keys(row[1])
        sleep(2)
        submit = bs.find_element_by_xpath('//input[@name="submit"]')
        submit.click()
        sleep(2)
    return bs

def select_module(bs):
    bs.current_window_handle
    modules = bs.find_elements_by_xpath('//h3/a')
    module = random.choice(modules)
    module.click()
    sleep(2)
    post_btn = bs.find_element_by_xpath('//img[@id="td_post"]')
    post_btn.click()
    '''ActionChains(bs).move_to_element(post_btn).perform()
    sleep(2)
    post = bs.find_element_by_xpath('//div[@id="pw_box"]')
    sleep(2)
    post.click()'''
    sleep(1)
    return bs

def post_message(bs,title,text):
    bs.current_window_handle
    atc_title = bs.find_element_by_xpath('//input[@id="atc_title"]')
    atc_title.send_keys(title)

    textarea = bs.find_element_by_xpath('//textarea[@id="textarea"]')
    textarea.send_keys(text)

    submit = bs.find_element_by_xpath('//input[@name="Submit"]')
    submit.click()
    if title == '':
        bs.find_element_by_xpath('//img[@src="images/error_bg.gif"]')
        close = bs.find_element_by_xpath('//input[@value="关闭"]')
        close.click()
        result = 'title is empty'
    elif title.isspace():
        bs.current_window_handle
        go_back = bs.find_element_by_xpath('//input[@value="返 回 继 续 操 作"]')
        sleep(2)
        go_back.click()
        sleep(2)
        result = 'title is space'
    elif len(title)>100:
        bs.find_element_by_xpath('//img[@src="images/error_bg.gif"]')
        close = bs.find_element_by_xpath('//input[@value="关闭"]')
        close.click()
        result = 'title is too long'
    elif len(title) < 100 and len(text)<3:
        bs.find_element_by_xpath('//img[@src="images/error_bg.gif"]')
        close = bs.find_element_by_xpath('//input[@value="关闭"]')
        close.click()
        result = 'text is too short'
    elif len(text)>50000:
        bs.find_element_by_xpath('//img[@src="images/error_bg.gif"]')
        close = bs.find_element_by_xpath('//input[@value="关闭"]')
        close.click()
        result = 'text is too long'
    else:
        bs.current_window_handle
        bs.back()
        result = 'success!'
    sleep(2)
    bs.back()
    sleep(2)
    bs.current_window_handle
    bs.back()
    sleep(2)
    bs.current_window_handle
    bs.refresh()
    sleep(3)
    return result

if __name__ == '__main__':
    log = Loginfo()
    bs = webdriver.Firefox()
    bs.get("http://localhost/upload/login.php")
    login(bs)
    bs.current_window_handle
    f = open("message.txt", "r")
    lines = f.readlines()  # 读取全部内容
    for line in lines:
        select_module(bs)
        bs.current_window_handle
        list = re.split(';', line)
        msg = post_message(bs,list[0],list[1])
        print(msg)
        log.log_write('title:' + list[0] + '|||||text:' + list[1].strip() + '|||||result:' + msg + '\n')
        sleep(5)
    f.close()
    log.log_close()



