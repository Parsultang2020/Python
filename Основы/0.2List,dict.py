##########СПИСОК############
spisok = [1, 3, 5, 65, 65, 65, "df", ["stroka", 99.88, 4584]]
spisok_2 = [2745, 453, 3, 55]
print(spisok)
spisok.append(23)            # append добавляет элемент 23 в конец списка
print(spisok)
spisok.extend(spisok_2)       # extend добавляет список 2 в конец списка 1
print(spisok)
spisok.insert(4, "vstavka")      # insert добавляет vstavka на 4 индекс
print(spisok)
spisok.remove(65)                 # remove удаляет первый попавшийся элемент 65
print(spisok)
spisok.pop(7)                     # pop удаляем элемент под индексом 7 (в данном случае строку)
print(spisok)
print("65 встречается в списке:", spisok.count(65))            # count считает, сколько 65 в списке
print("индекс числа 23 =", spisok.index(23))
spisok_2.sort()                               # сортировка по возрастанию
print(spisok_2)
spisok_2.reverse()
print(spisok_2)                  # просто переворачивает список
spisok_podspisok = [1, 2, 3, ['a', 'b', 'c']]
print(spisok_podspisok[3][2])      # выведет с, т.к. 3 индекс - подсписок, 2 индекс - с
print(spisok[-1])       # индекс -1 - последний элемент списка
print(spisok[-2])       # индекс -2 - предпоследний элемент списка

i = 0
while i < 5:
    print(spisok[i], end=" ")
    i += 1
print("\n")
for a in "list":
    for b in "dict":
        if a != "s" and b != "c":
            print(a+b, end=" ")        # end=" " делает из столбика строку
print("\n")
##################КОРТЕЖ################

spisokA = [1, 2, 3, "3df"]
kortej = (1, 2, 3, "3df")        # Кортеж занимает меньше места 28 против 36
print(spisokA.__sizeof__())       # В кортеже нельзя удалить, пеменять местами элементы
print(kortej.__sizeof__())
kortej_hello = tuple("Hello, World!")   # tuple разбивает на каждый элемент
print(kortej_hello)

########СЛОВАРИ##########################

dict_1 = {}
dict_2 = {"test": 1}   # test - ключ, обращаемся к ключу
dict_3 = {"test1": 1, "test2": 2, "test3": "teeeeeest", 1: 232323, 2: [1, 2, 3]}
print(dict_3["test3"])
print(dict_3[1])
print(dict_3[2][2])
dict_4 = {}
for k in range(10):
    dict_4[k] = k**3
print(dict_4)

input()


