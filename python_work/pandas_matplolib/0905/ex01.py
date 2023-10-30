def doA():
    big = int(input("큰수 입력: "))
    small = int(input("작은수 입력: "))
    sum = 0
    for i in range(small,big+1):
        print(f"i = {i}")
        sum +=i
    print(f"sum = {sum}")

doA()