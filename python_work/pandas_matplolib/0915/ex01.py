def doA():
    try:
        num = int(input('나이를 입력하세요'))
        print(f'num = {num}')
        result = num/0
        print(result)
    except ValueError as msg:
        print('valueError')
        print(msg)
    except ZeroDivisionError as msg:
        print('ZeroDivisionError')
        print(msg)
    finally:
        print('무조건 실행')
    print('정상종료')

doA()