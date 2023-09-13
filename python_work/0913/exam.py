import random

def do01():
    i = 0
    while True:
        print(i,end=" ")
        i = i+1
        if i==10:
            break

def do01_1():
    i = 0
    while i<10:
        print(i,end=" ")
        i = i+1


def do02():
    i = 9
    while True:
        print(i,end=" ")
        i = i-1
        if i==-1:
            break

def do02_1():
    i = 9
    while i>-1:
        print(i,end=" ")
        i = i-1


def do03():
    num = input('몇단 구구단 출력할래?')
    for i in range(9,0,-1):
        print(i*int(num),end=" ")

def do04():
    nansuary = []
    for i in range(5):
        num = random.random()
        nansuary.append(int(num * 100))

    print(nansuary)

def do05():
    win = 0
    draw= 0
    lose=0
    chstr = ['바위','가위','보']

    while True:
        num = int(input('바위는 1, 가위는 2, 보는 3 무엇을 입력하시겠습니까?'))
        com = (random.random()*3)+1
        com = int(com)
        print(f"당신의 선택은 {chstr[num-1]} 컴퓨터는 {chstr[com-1]}")
        if num == com :
            draw +=1
        if num == 2 and com == 1:
            lose +=1
            break
        if num == 2 and com == 3:
            win +=1
    print(f"win = {win} draw = {draw} lose = {lose}")











