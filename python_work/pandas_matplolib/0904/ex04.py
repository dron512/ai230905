# 향상된 for구문입니다....
def doA():
    temp = [0,1,2]
    for i in temp:
        print(i)

doA()

# range(1,11)
# [1,2,3,4,5,6,7,8,9,10]

# range(0,11)
# [0,1,2,3,4,5,6,7,8,9,10]

sum = 0
for i in range(11):
    sum = sum + i

print(sum)