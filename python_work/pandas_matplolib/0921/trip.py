from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# driver = webdriver.Chrome()
# driver.get("https://flight.naver.com/flights/domestic/TAE-CJU-20231011/CJU-TAE-20231012?adult=1&fareType=YC")
# try:
#     element = WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located((By.CSS_SELECTOR, "#__next > div > div.container > div.domestic_top__2ONl7 > div > div.layout_large__2AaMz > div > div > div.searchBox_tabpanel__1BSGR > button > span"))
#     )
#     test = driver.find_element(By.CSS_SELECTOR,'#__next > div > div.container > div.domestic_flight_content__ZPRcn > div > div.domestic_results__yNAgI > div:nth-child(2) > div > div.domestic_schedule__1Whiq > div > div.heading > div.airline > b')
#     print(test.text)
# finally:
#     driver.quit()

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

time.sleep(1)
도착도시 = web.find_element(By.CSS_SELECTOR,'#__next > div > div > div.main_searchbox__3vrV3 > div > div > div.searchBox_tabpanel__1BSGR > div.tabContent_routes__laamB > button.tabContent_route__1GI8F.select_City__2NOOZ.end')
도착도시.click()
time.sleep(1)
국내 = web.find_element(By.CSS_SELECTOR,'#__next > div > div > div.autocomplete_autocomplete__ZEwU_.autocomplete_is_arrival__JR22W > div.autocomplete_content__3RhAZ > section > section > button:nth-child(1)')
국내.click()
time.sleep(1)
제주 = web.find_element(By.CSS_SELECTOR,'#__next > div > div > div.autocomplete_autocomplete__ZEwU_.autocomplete_is_arrival__JR22W > div.autocomplete_content__3RhAZ > section > section > div > button:nth-child(2)')
제주.click()

time.sleep(1)
가는날달력 = web.find_element(By.CSS_SELECTOR,'#__next > div > div > div.main_searchbox__3vrV3 > div > div > div.searchBox_tabpanel__1BSGR > div:nth-child(2) > button:nth-child(1)')
가는날달력.click()

time.sleep(3)
가는날 = web.find_element(By.CSS_SELECTOR,'#__next > div > div > div.container_SearchModalContainer__2wVab > div.container_content__2w_MI.container_as_calendar__17CQb > div.calendar_calendar__2OzxE > div.calendar_content__1Xc5a > div > div:nth-child(3) > table > tbody > tr:nth-child(4) > td:nth-child(5) > button')
가는날.click()

time.sleep(2)
오는날 = web.find_element(By.CSS_SELECTOR,'#__next > div > div > div.container_SearchModalContainer__2wVab > div.container_content__2w_MI.container_as_calendar__17CQb > div.calendar_calendar__2OzxE > div.calendar_content__1Xc5a > div > div:nth-child(4) > table > tbody > tr:nth-child(1) > td:nth-child(5) > button')
오는날.click()
time.sleep(2)

항공권검색 = web.find_element(By.CSS_SELECTOR,'#__next > div > div > div.main_searchbox__3vrV3 > div > div > div.searchBox_tabpanel__1BSGR > button')
항공권검색.click()

try:
    element = WebDriverWait(web, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "#__next > div > div.container > div.domestic_top__2ONl7 > div > div.layout_large__2AaMz > div > div > div.searchBox_tabpanel__1BSGR > button"))
    )
    div = web.find_element(By.CSS_SELECTOR,'#__next > div > div.container > div.domestic_flight_content__ZPRcn > div > div.domestic_results__yNAgI > div:nth-child(2) > div > div.domestic_schedule__1Whiq')
    print(div.text)
finally:
    pass

time.sleep(3)
web.quit()

