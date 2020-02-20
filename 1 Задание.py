f = open('123.txt','w')
while True:
    s = input('Введите данные:')
    if s == '': break
    f.write(s+'\n')
f.close()