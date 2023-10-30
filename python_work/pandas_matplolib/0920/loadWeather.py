from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def doload():
    web = webdriver.Chrome()    #크롬브라우저실행
    web.get('https://www.naver.com/') #주소이동

    # 저번에는 id class 로 했는데
    # full xpath
    '''
        selenium 
        find_element() find_elements()
        By.ID
        By.ClASS_NAME
        BY.CSS_SELECTOR
        BY.XPATH
    '''
    a = web.find_element(By.CSS_SELECTOR,'#right-content-area > div.Layout-module__right_top___h3g3v > div:nth-child(3) > div > div.DailyBoardView-module__info_group___f8OSu > div:nth-child(1) > a.DailyBoardView-module__link_info_detail___miKv5 > div.DailyBoardView-module__info_weather___uEgXj > div.DailyBoardView-module__weather_temperature___pOAGy')
    retVal = a.text
    time.sleep(2)   #3초 쉬어라
    web.quit()  #종료해라
    print(retVal)
    return retVal

# doload()