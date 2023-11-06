import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def InitWebDriver():
    global wait
    web = webdriver.Chrome()
    wait = WebDriverWait(web, 10)
    return web


def SendKeyByName(element_name, key_values):
    input_element = wait.until(EC.element_to_be_clickable((By.NAME, element_name)))
    input_element.send_keys(key_values)
    return


def GetTextBySelector(selector):
    element = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, selector)))
    return element.text


def ClickValueByName(key_values):
    time.sleep(3)

    target = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, f'ul[data-value="solar"]')))
    target.click()

    print(target)

    print(key_values)

    time.sleep(3)

    # target_on=wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, f'ul[data-value="solar"]'+'.on')))
    # target_value = target_on.find_element(By.CSS_SELECTOR, f'li[data-value="{key_values}"]')

    # print(target_value.text)
    # target_value.click()
    return


def SendValueById(element_id, key_values):
    input_element = wait.until(EC.element_to_be_clickable((By.ID, element_id)))
    input_element.send_keys(key_values)
    return


def ClickValueForGender(element_name, key_values):
    target_value = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, f'.{element_name}[for="{key_values}"]')))
    target_value.click()
    return
