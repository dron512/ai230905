from CrawlerController import *
from UserDataConverter import *


def GetLuckyItem(userdata):
    web = InitWebDriver()
    web.get('https://sazoo.com/ss/run/life/todayitem/')

    이름 = userdata['Name']
    SendKeyByName('mNA', 이름)

    년도 = userdata['BirthYear']
    SendKeyByName('mYY', 년도)

    월 = userdata['BirthMonth']
    if 월 != 1:
        SendKeyByName('mMM', 월)

    일 = userdata['BirthDay']
    if 일 != 1:
        SendKeyByName('mDD', 일)

    시간 = TranceTimeNum(userdata['BirthTime'])
    SendKeyByName('mHH', 시간)

    성별 = '남성' if userdata['isMale'] else '여성'
    SendKeyByName('mSE', 성별)

    달력 = userdata['Calendar']
    SendKeyByName('mSL', 달력)

    web.execute_script("javascript:FormCheck()")

    result = GetDataFromWeb(web)

    return result


def GetDataFromWeb(web):
    result = []
    try:
        숫자 = GetTextBySelector(
            'body > table:nth-child(2) > tbody > tr > td > table > tbody > tr:nth-child(1) > td:nth-child(2) > table > tbody > tr:nth-child(2) > td > table > tbody > tr > td > table > tbody > tr:nth-child(4) > td > table > tbody > tr:nth-child(2) > td > table > tbody > tr > td > table > tbody > tr > td > table > tbody > tr:nth-child(3) > td > table > tbody > tr:nth-child(1) > td > b > font')
        숫자 = 숫자.split(":")[1].strip()
        숫자 = int(숫자)
        result.append(숫자)
        방향 = GetTextBySelector(
            'body > table:nth-child(2) > tbody > tr > td > table > tbody > tr:nth-child(1) > td:nth-child(2) > table > tbody > tr:nth-child(2) > td > table > tbody > tr > td > table > tbody > tr:nth-child(4) > td > table > tbody > tr:nth-child(2) > td > table > tbody > tr > td > table > tbody > tr > td > table > tbody > tr:nth-child(3) > td > table > tbody > tr:nth-child(2) > td > b > font')
        방향 = 방향.split(":")[1].strip()
        result.append(방향)
        색깔 = GetTextBySelector(
            'body > table:nth-child(2) > tbody > tr > td > table > tbody > tr:nth-child(1) > td:nth-child(2) > table > tbody > tr:nth-child(2) > td > table > tbody > tr > td > table > tbody > tr:nth-child(4) > td > table > tbody > tr:nth-child(2) > td > table > tbody > tr > td > table > tbody > tr > td > table > tbody > tr:nth-child(3) > td > table > tbody > tr:nth-child(3) > td > b > font')
        색깔 = 색깔.split(":")[1].strip()
        result.append(색깔)
        맛 = GetTextBySelector(
            'body > table:nth-child(2) > tbody > tr > td > table > tbody > tr:nth-child(1) > td:nth-child(2) > table > tbody > tr:nth-child(2) > td > table > tbody > tr > td > table > tbody > tr:nth-child(4) > td > table > tbody > tr:nth-child(2) > td > table > tbody > tr > td > table > tbody > tr > td > table > tbody > tr:nth-child(3) > td > table > tbody > tr:nth-child(4) > td > b > font')
        맛 = 맛.split(":")[1].strip()
        result.append(맛)
        과일 = GetTextBySelector(
            'body > table:nth-child(2) > tbody > tr > td > table > tbody > tr:nth-child(1) > td:nth-child(2) > table > tbody > tr:nth-child(2) > td > table > tbody > tr > td > table > tbody > tr:nth-child(4) > td > table > tbody > tr:nth-child(2) > td > table > tbody > tr > td > table > tbody > tr > td > table > tbody > tr:nth-child(3) > td > table > tbody > tr:nth-child(5) > td > b > font')
        과일 = 과일.split(":")[1].strip()
        result.append(과일)
        동물 = GetTextBySelector(
            'body > table:nth-child(2) > tbody > tr > td > table > tbody > tr:nth-child(1) > td:nth-child(2) > table > tbody > tr:nth-child(2) > td > table > tbody > tr > td > table > tbody > tr:nth-child(4) > td > table > tbody > tr:nth-child(2) > td > table > tbody > tr > td > table > tbody > tr > td > table > tbody > tr:nth-child(3) > td > table > tbody > tr:nth-child(6) > td > b > font')
        동물 = 동물.split(":")[1].strip()
        result.append(동물)
        신체부위 = GetTextBySelector(
            'body > table:nth-child(2) > tbody > tr > td > table > tbody > tr:nth-child(1) > td:nth-child(2) > table > tbody > tr:nth-child(2) > td > table > tbody > tr > td > table > tbody > tr:nth-child(4) > td > table > tbody > tr:nth-child(2) > td > table > tbody > tr > td > table > tbody > tr > td > table > tbody > tr:nth-child(7) > td > b > font')
        result.append(신체부위)
        마음가짐 = GetTextBySelector(
            'body > table:nth-child(2) > tbody > tr > td > table > tbody > tr:nth-child(1) > td:nth-child(2) > table > tbody > tr:nth-child(2) > td > table > tbody > tr > td > table > tbody > tr:nth-child(4) > td > table > tbody > tr:nth-child(2) > td > table > tbody > tr > td > table > tbody > tr > td > table > tbody > tr:nth-child(11) > td > b > font')
        result.append(마음가짐)
        생활가이드 = GetTextBySelector(
            'body > table:nth-child(2) > tbody > tr > td > table > tbody > tr:nth-child(1) > td:nth-child(2) > table > tbody > tr:nth-child(2) > td > table > tbody > tr > td > table > tbody > tr:nth-child(4) > td > table > tbody > tr:nth-child(2) > td > table > tbody > tr > td > table > tbody > tr > td > table > tbody > tr:nth-child(15) > td > b > font')
        result.append(생활가이드)

        return result
    finally:
        web.quit()
