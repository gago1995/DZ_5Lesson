my_list = []
n = 1
with open('text.txt', encoding='utf-8') as f:
    for el in f:
        my_list.append(el.split())
for el in my_list:
    print(f'В строке {n} ({el}) {len(el)} слов(а)')
    n = n + 1