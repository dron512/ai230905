a = [1, 2, 3, 4]
a[0] = 10

b = (1, 2, 3, 4)
# b[0] = 10

print(a)
print(b)


def doA():
    return 10, 20, 30


result = doA()
print(type(result))
print(result)


def doB(a, b='b', c='c'):
    print(a, b, c)


c = (10, 20, 30)
doB(*c)
doB(c)
