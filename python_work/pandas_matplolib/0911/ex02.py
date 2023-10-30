'''
    int() float() list() str() bool()
    len() max() min()
'''
a = "abcdef"

if 'a' in a:
    print('a 변수 안에 a 문자열이 있습니다.')

if 'g' not in a:
    print('a 변수 안에 g 문자열이 없습니다.')

if a:
    print('변수 a는 True 입니다.')

b = ""
print(bool(b))

c = []
print(bool(c))