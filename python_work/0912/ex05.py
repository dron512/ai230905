from circle import doA as a,doB
# from circle import doB

# print(circle.PI)

def main():
    r = float(input('반지름 입력: '))
    result = a(r)
    print(f'원 넓이는 {result}')

    result = doB(r)
    print(f'원 둘레는 {result}')

main()
