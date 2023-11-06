import time

from CrawlerController import *
from UserDataConverter import *


def TODOTest(userdata):
    result = []
    네이버한줄 = '더미'
    result.append(네이버한줄)
    네이버상세 = '더미'
    result.append(네이버상세)
    return result


def doTodayNaver(userdata):
    web = InitWebDriver()
    web.get(
        'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%EC%98%A4%EB%8A%98%EC%9D%98+%EC%9A%B4%EC%84%B8')

    성별 = 'l_man' if userdata['isMale'] else 'l_woman'
    ClickValueForGender('_genderLabel', 성별)

    생년월일 = TranceBirthDay(userdata)
    SendValueById("srch_txt", 생년월일)

    달력 = TranceCalendar(userdata['Calendar'])
    print(달력)
    time.sleep(3)
    web.find_element(By.XPATH,
                     '/html/body/div[3]/div[2]/div/div[1]/section[1]/div/div[2]/div[2]/div[1]/fieldset/div[3]/ul[1]').click()

    if 달력 in 'solar':
        web.find_element(By.XPATH,
                         '/html/body/div[3]/div[2]/div/div[1]/section[1]/div/div[2]/div[2]/div[1]/fieldset/div[3]/ul[1]/li[1]').click()
    elif 달력 in 'lunarGeneral':
        web.find_element(By.XPATH,
                         '/html/body/div[3]/div[2]/div/div[1]/section[1]/div/div[2]/div[2]/div[1]/fieldset/div[3]/ul[1]/li[2]').click()
    elif 달력 in 'lunarLeap':
        web.find_element(By.XPATH,
                         '/html/body/div[3]/div[2]/div/div[1]/section[1]/div/div[2]/div[2]/div[1]/fieldset/div[3]/ul[1]/li[3]').click()
    # ClickValueByName(달력)
    # print("하고 나옴")

    시간 = TranceTimeNum(userdata['BirthTime'])

    # web.execute_script('result_solo()')

    try:
        element = WebDriverWait(web, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".today_f_tit"))
        )
        div = web.find_element(By.CSS_SELECTOR, '.today_f_txt')
        print(div.text)
        return div.text
    finally:
        pass
        # web.quit()
