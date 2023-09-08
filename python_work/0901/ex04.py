# class A:
#     def doA(self):
#         a=10
def doA(name):
    print(f'안녕하세요 {name}입니다.')
    print('안녕하세요',name,'입니다.')

def doB(num1,num2):
    return num1+num2

doA('홍길동')
c = doB(5,3)
print(c)
d = doB('안녕','하세요')
print(d)
e = doB(str(5),'안녕')
print(e)
