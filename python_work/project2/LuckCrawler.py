from GetDataWithsaju import GetLuckyItem
from GetDataWithNaver import TODOTest, doTodayNaver


def TranceLuckData(userdata):
    print(userdata)
    try:
        data = GetLuck(userdata)
        result = {
            'Num': data[0],
            'Direction': data[1],
            'Color': data[2],
            'Flavor': data[3],
            'Fruit': data[4],
            'Animal': data[5],
            'BodyParts': data[6],
            'Mind': data[7],
            'Guide': data[8],
            'NaverSummary': data[9],
            'NaverDetail': data[10]
        }
        return result
    except Exception as e:
        print(e)


def GetLuck(userdata):
    doTodayNaver(userdata)
    return GetLuckyItem(userdata) + TODOTest(userdata)

# TranceLuckData({'Name': '이창민', 'BirthYear': 1989, 'BirthMonth': 1, 'BirthDay': 1, 'BirthTime': 0, 'isMale': True, 'Calendar': '음력/평달'})
