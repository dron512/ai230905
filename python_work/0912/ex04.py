st = [1,2,3,4,5,6]
a = 10

def doA(s):
    s[0] = 10
    s[-1] = 20

def doB(k):
    k = 20
    print("k = ",k)

doA(st)
doB(a)

print(st)
print("a = ",a)