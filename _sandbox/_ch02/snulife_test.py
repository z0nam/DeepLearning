# -*- coding: utf-8 -*-
"""
Created on Fri Jul 14 14:55:17 2017

@author: sncc
"""
from selenium import webdriver
from bs4 import BeautifulSoup as bs

def snulife_login(user, pw, phantom_path):
    browser = webdriver.PhantomJS(phantom_path)
    browser.implicitly_wait(3)
    login_page = "http://snulife.com/index.php?act=dispMemberLoginForm"
    browser.get(login_page)
    print('로그인 페이지에 접근')
    id_e = browser.find_element_by_id(id_= "uid")
    id_e.clear()
    id_e.send_keys(user)
    pw_e = browser.find_element_by_id(id_= "upw")
    pw_e.clear()
    pw_e.send_keys(pw)
    
    submit_path = '#fo_member_login > div.btnArea > span.btn'
    form = browser.find_element_by_css_selector(submit_path)
    form.submit()
    print("로그인 버튼 클릭")
    
    best_bbs1 = "http://snulife.com/gongsage/114024213"
    browser.get(best_bbs1)
    html = browser.page_source
    soup = bs(html, 'html.parser')
    browser.quit()
    return soup

if __name__ == "__main__":
    phantom_path = "/Users/j/Downloads/phantomjs-2.1.1-macosx/bin/phantomjs"
    soup = snulife_login('', phantom_path)
    soup_str = str(soup)
    with open('example1.html', 'w', encoding="utf-8") as f:
        f.write(soup_str)
