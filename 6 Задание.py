my_list =[]
my_list2 = []
d1 = dict()
with open('Предметы.txt', encoding='utf-8') as f:
    for el in f:
        my_list.append(el.split())
for el in my_list:
     a = list(filter(lambda x: x != '—', el))
     for n in range (1, len(a)):
         b = a[n]
         b = int (b[:b.index('(')])
         a[n] = b
     my_list2.append(a)
for el in my_list2:
   d1[el[0]] = sum(el[1:])
print(d1)