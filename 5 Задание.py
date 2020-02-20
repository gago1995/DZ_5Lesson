my_list =[]
with open('Числа.txt', encoding='utf-8') as f:
    my_list.extend(map(int, f.read().split()))
print(my_list)
print(sum(my_list))