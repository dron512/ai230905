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
