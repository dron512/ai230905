'''
운세가져오기
https://m.unsin.co.kr/unse/tojung/total/form?year=2023

pyqt5를 이용해서
생년월일을 넣고
불러오기를 눌렀을때

GUI 화면에 출력되도록 한다.
'''

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

def doYear():
    web = webdriver.Chrome()
    web.get('https://m.unsin.co.kr/unse/tojung/total/form?year=2023')
    time.sleep(2)

    이름 = web.find_element(By.CSS_SELECTOR,'#user_name')
    이름.send_keys('abcd')

    년도 = web.find_element(By.CSS_SELECTOR,'#birth_yyyy')
    년도.send_keys('1985년')

    월 = web.find_element(By.CSS_SELECTOR,'#birth_mm')
    월.send_keys('5월')

    일자 = web.find_element(By.CSS_SELECTOR,'#birth_dd')
    일자.send_keys('11일')

    시간 = web.find_element(By.CSS_SELECTOR,'#birth_hh')
    시간.send_keys('申 (15:30 ~ 17:29)')

    양력음력 = web.find_element(By.CSS_SELECTOR,'#birth_solunar')
    양력음력.send_keys('양력')

    운세볼년도 = web.find_element(By.CSS_SELECTOR,'#target_yyyy')
    운세볼년도.click()

    년도선택 = web.find_element(By.CSS_SELECTOR,'#target_yyyy > option:nth-child(14)')
    년도선택.click()

    time.sleep(3)
    web.execute_script('result_solo()')
    time.sleep(5)
    try:
        element = WebDriverWait(web, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".saju_box"))
        )
        div = web.find_element(By.CSS_SELECTOR,'#content > article > div.result > div.saju_box > div:nth-child(6)')
        return div.text
    finally:
        time.sleep(5)
        web.quit()

def doToday():
    web = webdriver.Chrome()
    web.get('https://m.unsin.co.kr/unse/free/today/form')

    이름 = web.find_element(By.CSS_SELECTOR, '#user_name')
    이름.send_keys('abcd')

    년도 = web.find_element(By.CSS_SELECTOR, '#birth_yyyy')
    년도.send_keys('1985년')

    월 = web.find_element(By.CSS_SELECTOR, '#birth_mm')
    월.send_keys('5월')

    일자 = web.find_element(By.CSS_SELECTOR, '#birth_dd')
    일자.send_keys('11일')

    시간 = web.find_element(By.CSS_SELECTOR, '#birth_hh')
    시간.send_keys('申 (15:30 ~ 17:29)')

    양력음력 = web.find_element(By.CSS_SELECTOR, '#birth_solunar')
    양력음력.send_keys('양력')

    time.sleep(3)
    web.execute_script('result_solo()')
    time.sleep(5)

    try:
        element = WebDriverWait(web, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".today_f_tit"))
        )
        div = web.find_element(By.CSS_SELECTOR,'.today_f_txt')
        print(div.text)
        return div.text
    finally:
        time.sleep(5)
        web.quit()
