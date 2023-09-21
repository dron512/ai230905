from selenium import webdriver
from selenium.webdriver.common.by import By

import time

web = webdriver.Chrome()
web.get('https://flight.naver.com/')
web.maximize_window()

출발도시 = web.find_element(By.CSS_SELECTOR,'#__next > div > div > div.main_searchbox__3vrV3 > div > div > div.searchBox_tabpanel__1BSGR > div.tabContent_routes__laamB > button.tabContent_route__1GI8F.select_City__2NOOZ.start')
출발도시.click()
time.sleep(1)
국내 = web.find_element(By.CSS_SELECTOR,'#__next > div > div > div.autocomplete_autocomplete__ZEwU_.is_departure > div.autocomplete_content__3RhAZ > section > section > button:nth-child(1)')
국내.click()
time.sleep(1)
대구 = web.find_element(By.CSS_SELECTOR,'#__next > div > div > div.autocomplete_autocomplete__ZEwU_.is_departure > div.autocomplete_content__3RhAZ > section > section > div > button:nth-child(7)')
대구.click()

time.sleep(3)
web.quit()

