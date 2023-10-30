import db

while True:
    print('1. select')
    print('2. insert')
    print('3. exit')
    ch = input('뭐할래요? ')
    if ch=='1':
        db.doSelect()
    elif ch=='2':
        name = input('이름을입력')
        age = int(input('나이'))
        gender = input('성별')
        db.doInsert(name, age, gender)
    elif ch=='3':
        print('종료됩니다.')
        break









