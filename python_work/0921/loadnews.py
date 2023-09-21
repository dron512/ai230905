from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def doload():
    web = webdriver.Chrome()
    web.get('https://imnews.imbc.com/news/2023/sports/')
    time.sleep(1)
    aele = web.find_element(By.CSS_SELECTOR,'#content > section > div.section.content_area > div.list_area.list_top.wrapper > ul > li:nth-child(1) > a')
    aele.click()
    time.sleep(1)
    imgele = web.find_element(By.CSS_SELECTOR,'#content > div > section.wrap_article > article > div.news_cont > div.news_txt > div > img')
    src = imgele.get_attribute('src')
    txt = web.find_element(By.CSS_SELECTOR,'#content > div > section.wrap_article > article > div.news_cont > div.news_txt')
    text = txt.text
    # web.back()
    time.sleep(3)
    web.quit()
    return src,text