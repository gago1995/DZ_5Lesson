my_list =[]
with open('Числительные.txt', encoding='utf-8') as f:
    for el in f:
        my_list.append(el.split())
with open('НовыеЧислительные.txt',  'w', encoding='utf-8') as f1:
        for el in my_list:
            if el [0] == 'One': el [0] = 'Один'
            elif el [0] == 'Two': el [0] = 'Два'
            elif el [0] == 'Three': el [0] = 'Три'
            elif el[0] == 'Four': el[0] = 'Четыре'
            print(el[0], el[1], el[2], file=f1)