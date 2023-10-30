'''
    i가 1일때 j는 a,b,c
    i가 2일때 j는 a,b,c
    i가 3일때 j는 a,b,c
'''
a = [1,2,3]
b = ['a','b','c']
for i in a:
    for j in b:
        print(j*i,end=" ")
print()
strs = ['fathera','mother','brother']
# s = 'father' c = f,a,t,h,e,r
# s = 'mother' c = m,o,t,h,e,r
# s = 'brother' c = b,r,o,t,h,e,r
cnt = 0
for s in strs:
    for c in s:
        if c=='r':
            cnt = cnt+1
    print(c)
print(cnt)