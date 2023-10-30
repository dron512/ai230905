class AA:
    def __init__(self):
        print('생성자호출')
        self.a = 10
        self.b = 20

    def __str__(self):
        return f"self.a = {self.a} , self.b= {self.b}"

a1 = AA()
print(a1)
