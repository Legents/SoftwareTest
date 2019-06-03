from selenium.webdriver import ActionChains
from selenium import webdriver
from time import sleep

import random
import csv
import re

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
    sleep(2)
    bs.back()
    sleep(2)
    bs.current_window_handle
    bs.back()
    sleep(2)
    bs.current_window_handle
    bs.refresh()
    sleep(3)
    return bs

if __name__ == '__main__':
    bs = webdriver.Firefox()
    bs.get("http://localhost/upload/login.php")
    bs = login(bs)
    f = open("message.txt", "r")
    lines = f.readlines()  # 读取全部内容
    for line in lines:
        bs = select_module(bs)
        list = re.split(';', line)
        print(list[0])
        print(list[1])
        bs = post_message(bs,list[0],list[1])
        bs.back()
        sleep(5)
    f.close()





