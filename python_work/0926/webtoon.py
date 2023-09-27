from selenium import webdriver
from selenium.webdriver.common.by import By
import download
import time

def doA():
    web = webdriver.Chrome()
    web.get('https://comic.naver.com/index')
    web.maximize_window()

    time.sleep(3)

    남성 = web.find_element(By.CSS_SELECTOR,
            '#container > div.content_wrap > div.Aside__aside_wrap--iF5ju > div:nth-child(2) > div > div.ComponentHead__tab_control--R1TyL > button:nth-child(3)')
    남성.click()

    time.sleep(1)
    litags = web.find_elements(By.CSS_SELECTOR,
                '#container > div.content_wrap > div.Aside__aside_wrap--iF5ju > div:nth-child(2) > ul > li')
    retValue = []
    for i, li in enumerate(litags):
        imgs = li.find_element(By.TAG_NAME,'img')
        download.down(imgs.get_attribute('src'),f'img{i}.png')
        spanText = li.find_element(By.CSS_SELECTOR,'.text');
        retValue.append(spanText.text)

    time.sleep(3)
    web.quit()
    return  retValue