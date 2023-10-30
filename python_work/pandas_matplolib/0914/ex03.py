from aa.age import Age_Info

fa = Age_Info()
fa.age = 20
fa.up_age()
Age_Info.up_age(fa)
print(fa.get_age())

mo = Age_Info()
mo.age = 30
mo.up_age()
print(mo.get_age())

me = Age_Info()
me.age = 12
me.up_age()
print(me.get_age())

print(f"가족 모두의 나이 합= {fa.age+mo.age+me.age}")

# Age_Info.up_age(fa)
# print(Age_Info.get_age(fa))