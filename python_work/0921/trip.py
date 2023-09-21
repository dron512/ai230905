from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://flight.naver.com/flights/domestic/TAE-CJU-20231011/CJU-TAE-20231012?adult=1&fareType=YC")
try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "#__next > div > div.container > div.domestic_top__2ONl7 > div > div.layout_large__2AaMz > div > div > div.searchBox_tabpanel__1BSGR > button > span"))
    )
    test = driver.find_element(By.CSS_SELECTOR,'#__next > div > div.container > div.domestic_flight_content__ZPRcn > div > div.domestic_results__yNAgI > div:nth-child(2) > div > div.domestic_schedule__1Whiq > div > div.heading > div.airline > b')
    print(test.text)
finally:
    driver.quit()

# import time
#
# web = webdriver.Chrome()
# web.get('https://flight.naver.com/')
# web.maximize_window()
#
# 출발도시 = web.find_element(By.CSS_SELECTOR,'#__next > div > div > div.main_searchbox__3vrV3 > div > div > div.searchBox_tabpanel__1BSGR > div.tabContent_routes__laamB > button.tabContent_route__1GI8F.select_City__2NOOZ.start')
# 출발도시.click()
# time.sleep(1)
# 국내 = web.find_element(By.CSS_SELECTOR,'#__next > div > div > div.autocomplete_autocomplete__ZEwU_.is_departure > div.autocomplete_content__3RhAZ > section > section > button:nth-child(1)')
# 국내.click()
# time.sleep(1)
# 대구 = web.find_element(By.CSS_SELECTOR,'#__next > div > div > div.autocomplete_autocomplete__ZEwU_.is_departure > div.autocomplete_content__3RhAZ > section > section > div > button:nth-child(7)')
# 대구.click()
#
# time.sleep(3)
# web.quit()

