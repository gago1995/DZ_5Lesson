my_list =[]
zp = []
with open('ZP.txt', encoding='utf-8') as f:
    for el in f:
        my_list.append(el.split())
print('Сотрудники с ЗП менее 20000 р.:')
for el in my_list:
    zp.append(float(el[1]))
    if float(el[1]) < 20000:
        print(el[0])
print('Средняя ЗП: ', round(sum(zp) / len(zp),2))