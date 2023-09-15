from selenium import webdriver # selenium 모듈 가져오기
from selenium.webdriver.common.by import By

import time # time 모듈가져오기

def doLoad():
    web = webdriver.Chrome() # 크롬 실행
    web.get(url='http://silverfang.zc.bz/bbs/board.php?bo_table=news') # 주소이동

    time.sleep(5)   # 5초 재우기
    print(web.current_url) # 현재 주소 출력

    subs = web.find_elements(By.CLASS_NAME,"subject")
    # print(subs)

    texts = ''
    for ele in subs:
        texts += ele.text
    web.close() #창 닫기
    return texts

def doLoad2():
    web = webdriver.Chrome() # 크롬 실행
    web.get(url='https://dhlottery.co.kr/common.do?method=main') # 주소이동

    main = web.window_handles
    for i in main:
        if i != main[0]:
            web.switch_to.window(i)
            web.close()

    web.switch_to.window(main[0])
    time.sleep(3)

    no1 = web.find_element(By.ID,"drwtNo1").text
    no2 = web.find_element(By.ID, "drwtNo2").text
    no3 = web.find_element(By.ID, "drwtNo3").text
    no4 = web.find_element(By.ID, "drwtNo4").text
    no5 = web.find_element(By.ID, "drwtNo5").text
    no6 = web.find_element(By.ID, "drwtNo6").text
    bonus = web.find_element(By.ID, "bnusNo").text
    
    web.close() #창 닫기
    return no1,no2,no3,no4,no5,no6,bonus

