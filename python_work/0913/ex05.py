dc = {'새우깡':700,"바나나킥":500}

for i in dc:
    dc[i] +=70

print(dc)

for key in dc.keys():
    print(key)

for value in dc.values():
    print(value)

for key,value in dc.items():
    print(key,value)