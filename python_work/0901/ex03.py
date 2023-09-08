# alt +ctrl+ l 자동정렬
a, b = 10, 20
print('a', a)
print('b', b)

a, b = b, a
print(f'a {a}')
print(f'b {b}')

def doC():
    return 30, 40

a, b = doC()
print(f'a {a}')
print(f'b {b}')

c = doC()
print(c)




