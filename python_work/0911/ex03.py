def doFor():
    sum = 0
    for i in range(1,11):
        sum = sum+i
    print(f"sum = {sum}")

def doWhile():
    i = 0
    sum = 0
    while i<11:
        sum = sum+i
        i = i+1
    print(f"sum = {sum}")

doFor()
doWhile()