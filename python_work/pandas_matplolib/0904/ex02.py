def doB():
    num1 = int(input("num1 = "))
    num2 = input("num2 = ")
    num3 = input("num3 = ")
    return num1 * int(num2) + int(num3)

def doC():
    num = input("num = ")
    print(f"{num}값의 제곱은 {int(num)**2}")

def doD():
    num1 = int(input("num1 = "))
    num2 = int(input("num2 = "))
    print(f"num1나누기 num2 = {num1//num2}")
    print(f"num1나누기 num2 나머지 {num1 % num2}")