'''
1. a = [10,20,30,40] 을 넣고 for 구문과 range문을 사용해서 데이터를 출력하세요
10 20 30 40
'''


def doA():
    a = [10, 20, 30, 40]
    for item in a:
        print(item, end=" ")


'''
2. 1부터 30까지의 숫자중 3의 배수이면서 2의 배수인것을 출력한다,(if,for구문사용)
  6,12,18,24
'''


def doB():
    for i in range(1, 31):
        if i % 3 == 0 and i % 2 == 0 and i != 30:
            print(i, end=",")
        elif i % 3 == 0 and i % 2 == 0:
            print(i)


def doC():
    num = int(input('몇단 출력할래?'))
    for i in range(2, 10, 2):
        print(f"{num} * {i} = {num * i}")


doA()
print()
doB()
doC()
