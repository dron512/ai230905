import pandas as pd

'''
    read_excel 파일 없으면 에러
    데이터프레임 pd.DataFrame(data)
    파일을 만들어야 합니다.
    
    1. 저장시에 데이터를 저장하기 data.xlsx
    2. weather.py 조회버튼
     -> 엑셀데이터를 가져와서 tableWidget 보여주기
'''
def doSave(도시,최저,최고,날씨):
    try:
        data = pd.read_excel('data.xlsx',usecols=['도시','최저','최고','날씨'])
    except Exception as e:
        data = {
            '도시':[],
            '최저':[],
            '최고':[],
            '날씨':[],
        }
        data =pd.DataFrame(data)
    data.loc[len(data)] = [도시,최저,최고,날씨]
    data.to_excel('data.xlsx')


def doDelete(index):
    try:
        data = pd.read_excel('data.xlsx',usecols=['도시','최저','최고','날씨'])
    except Exception as e:
        data = {
            '도시':[],
            '최저':[],
            '최고':[],
            '날씨':[],
        }
        data =pd.DataFrame(data)
    data = data.drop(index=index)
    data.to_excel('data.xlsx')


def doLoad():
    data = pd.read_excel('data.xlsx')
    return data[data.columns[1:]]