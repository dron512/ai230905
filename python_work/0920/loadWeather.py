from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def doload():
    web = webdriver.Chrome()    #크롬브라우저실행
    web.get('https://www.naver.com/') #주소이동

    # 저번에는 id class 로 했는데
    # full xpath
    a = web.find_element(By.XPATH,'/html/body/div[2]/div[2]/div/div[2]/div/div[1]/div[4]/div/div[2]/div[1]/a[1]/div[1]/div[2]')
    retVal = a.text
    time.sleep(2)   #3초 쉬어라
    web.quit()  #종료해라
    return retVal

# doload()