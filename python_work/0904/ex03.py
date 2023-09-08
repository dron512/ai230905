# 실행 단축키 ctrl+ shift + f10 or shift+f10
# 여러개줄 ctrl + / 주석 설정
# import os
#
# os.chdir("/")

def doA():
    print(10)
doA()

test = "10+20*3"
result = eval(test)
print(result)

test = "doA()"
eval(test)