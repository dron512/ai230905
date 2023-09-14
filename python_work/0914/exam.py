dc = {'새우깡':700,'콘치즈':850,"꼬깔콘":750}
def doA():
    dc['홈런볼'] = 900
    print(dc)

def doB():
    for i in dc:
        dc[i] +=100
    print(dc)

def doC():
    del dc['콘치즈']
    dc['치즈콘'] = 950
    print(dc)