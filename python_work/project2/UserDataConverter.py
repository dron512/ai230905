def TranceTimeNum(time):
    valuedict = {
        0: 99,
        1: 0,
        2: 2,
        3: 4,
        4: 6,
        5: 8,
        6: 10,
        7: 12,
        8: 14,
        9: 16,
        10: 18,
        11: 20,
        12: 22
    }
    return valuedict[time]


def TranceCalendar(calendar):
    valuedict = {
        '양력/평달': "solar",
        '음력/평달': "lunarGeneral",
        '음력/윤달': "lunarLeap"
    }
    return valuedict[calendar]


def TranceBirthDay(userdata):
    년도 = userdata['BirthYear']
    월 = userdata['BirthMonth']
    일 = userdata['BirthDay']
    return f'{년도}{str(월).zfill(2)}{str(일).zfill(2)}'
