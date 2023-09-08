a = "ab_cd_ef"

mylist = a.split("_")

print(type(mylist))
print(mylist)

for i in mylist:
    print(i)

print(a.find('d'))
print(a.find('g'))

if 0:
    print("0은 false")
if 100:
    print("true")

if a.find('g'):
    print('g로 찾으면 -1나옵니다..')

# String a = "asb";
# if(a.contain())

if 'g' not in a:
    print('a 변수 안에 g가 없습니다.')

if 'a' in a:
    print('a 변수 안에 a가 있습니다.')











