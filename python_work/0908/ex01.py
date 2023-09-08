jumin = input('주민등록번호 입력:')

def doEx01():
    global jumin
    jumin = list(jumin)
    jumin[8:] = ['XXXXXX']
    jumin = ''.join(jumin)
    print(jumin)

def doEx02():
    global jumin
    print(f'19{jumin[:2]}년 {jumin[2:4]}월{jumin[4:6]}일')

doEx01()
doEx02()
'''
3. st = [1,2] 리스트를 선언하고
   리스트에 3,4,5,6,7,8,9,10의 요소를 추가해 넣으세요

4.  st = [1,2,3,4,5,6,7,8,9,10]
   선언하고
   pop 함수를 사용하여
   for 구문을 작성해서 삭제와 동시에 값을 출력하시오
   출력 결과 예시
   1,   2,   3
   print(st) >>> []
'''