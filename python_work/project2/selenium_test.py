import traceback


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json
import time
from selenium.webdriver.common.keys import Keys

# 웹 드라이버 초기화
driver = webdriver.Chrome()

#path_to_Chromedriver = "D:/samwork_python/python_work/pandas_matplolib/1006/chrome_driver/chromedriver-win64"

# 웹 사이트로 이동
driver.get(url = "https://kosis.kr/statHtml/statHtml.do?orgId=101&tblId="
                 "DT_1J20017&vw_cd=MT_ZTITLE&list_id=" "P2_6&scrId=&seqNo="
                 "&lang_mode=ko&obj_var_id=&itm_id=&conn_path=K1&path="
                 "%25EB%25AC%25BC%25EA" "%25B0%2580%2520%253E%2520%25EC%2586%258C"
                 "%25EB%25B9%2584%25EC%259E%2590%25EB%25AC%25BC%25EA" ""
                 "%25B0%2580%25EC%25A1%25B0%25EC%2582%25AC%25EC%2597%25B0%25EC"
                 "%2587%2584%25EB%25B0%25A9%25EC" "%258B%259D%2520%25EC%2586%258C%"
                 "25EB%25B9%2584%25EC%259E%2590%25EB%25AC%25BC%25EA%25B0%2580" ""
                 "%25EC%25A7%2580%25EC%2588%2598%282020%253D100%29")

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--disable-popup-blocking")


# Interact with the page //*[@id="btn_time"]
try :
    wait = WebDriverWait(driver, 20)
    wait.until(EC.presence_of_element_located((By.ID,'iframe_rightMenu')))
    iframe = driver.find_element(By.ID,'iframe_rightMenu')
    driver.switch_to.frame(iframe)

    if iframe:
        wait.until(EC.presence_of_element_located((By.ID, 'iframe_centerMenu1')))
        iframe = driver.find_element(By.ID, 'iframe_centerMenu1')
        driver.switch_to.frame(iframe)

    if iframe :
        time.sleep(3)
        wait.until(EC.presence_of_element_located((By.ID, "btn_time")))
        element = driver.find_element(By.ID, "btn_time")
        element.click()

        checkbox_xpaths = ['//*[@id="ft-id-4"]/li[1]/span',
                           '//*[@id="ft-id-4"]/li[2]/span',
                           '//*[@id="ft-id-4"]/li[3]/span',
                           '//*[@id="ft-id-4"]/li[4]/span',
                           '//*[@id="ft-id-4"]/li[5]/span',
                           '//*[@id="ft-id-4"]/li[6]/span']
        driver.find_element(By.ID,'timePopListYBtn').click()
        for xpath in checkbox_xpaths:
            # wait.until(
            #     EC.presence_of_all_elements_located(
            #         (By.XPATH, xpath))
            # )
            driver.find_element(By.XPATH, xpath).click()

        driver.find_element(By.ID, "btnTimeAccept").click()
        #wait for dynamic content
        element = wait.until(
            EC.presence_of_element_located((By.ID, "mainTable"))
        )

    #extract data
        data = driver.find_element(By.ID, "mainTable").text
        print(data)

        time.sleep(5)

     # save data to a temporary JSON file
        with open('temp_data.json', 'w', encoding='utf-8') as json_file:
            json.dump({"data": data}, json_file)

except Exception as e:
    print('에렁')
    e = traceback.format_exc()
    print(e)

finally :
    driver.quit()

