import db

while True:
    print('1. select')
    print('2. insert')
    print('3. exit')
    ch = input('뭐할래요? ')
    if ch=='1':
        db.doSelect()
    elif ch=='2':
        db.doInsert()
    elif ch=='3':
        print('종료됩니다.')
        break









