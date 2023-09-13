def doA():
    num = int(input('10진수 입력:'))
    bin = ""
    while num>0:
        mod = num%2
        num = num//2
        bin = str(mod)+bin
    print(bin)

def doB():
    sec = int(input("초 입력:"))
    hour = sec//3600
    sec = sec%3600
    min = sec//60
    sec = sec%60
    print(f'{hour}시 {min}분 {sec}초')

doA()
doB()