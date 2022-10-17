# Напишите программу, удаляющую из текста все слова, содержащие ""абв""

# my_text ='Напишите абв напиабв програбвмму программу, удаляющую из\ этого абв текста все вабвс слова, содерабващие содержащие "абв" '
# print(f'Исходный текст: {my_text}')                                         #выводим вводимый текст на экран
# def del_word(my_text):                                                      #заводим название  функции
#     my_text =list(filter(lambda  x: 'абв' not in x, my_text.split()))       # производим фильтр нашего списка
#     return ' '.join(my_text)                                                # в произведенной строке передаем метод join в список,
#                                                                             # состоящий из строковых типов.Объединяем в 1 строку,
#                                                                             #разделяя пробелами.

# my_text = del_word(my_text)                                                 # называем функцию
# print(f'Результат: {my_text}')  


# Задайте последовательность чисел. Напишите программу, 
# которая выведет список неповторяющихся элементов исходной последовательности.

# Старая задача
# numbers = [10, 20, 20, 30, 30, 4, 5]
# list_of_unique_numbers = []
# for i in numbers:
#  if numbers.count(i)==1:
#     list_of_unique_numbers.append(i)
# print(list_of_unique_numbers)

# Через List comprehension с if
# numbers = [10, 20, 20, 30, 30, 4, 5]
# print(numbers)
# list_of_unique_numbers = [i for i in numbers if numbers.count(i)==1]
# print(list_of_unique_numbers)


# Старая
# nums = [int(input('Введите элемент списка: ')) 
# for i in range(int(input('Введите длину списка: ')))]
# mult = 1
# for i in nums:
#     mult *= i
# print(f'Весь список: {nums}')
# print(f'Произведение элементов списка: {mult}')

# Измененная
# nums = [n for n in range(1,6)]
# print(f'Исходный список: {nums}')
# mult = 1
# for i in nums:
#     mult *= i
# print(f'Весь список: {nums}')
# print(f'Произведение элементов списка: {mult}')

#  Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

# list = input('Введите ряд чисел через пробел: ').split()
# list_mult = []

# for i in range(len(list) // 2):
#     j = int(list[i]) * int(list[-1 - i])
#     list_mult.append(j)
#     i *= 1
# print('Произведение пар чисел списка:', list_mult)

# def mult_lst(lst):  
#     l = len(lst)//2 + 1 if len(lst) % 2 != 0 else len(lst)//2
#     new_lst = [lst[i]*lst[len(lst)-i-1] for i in range(l)]
#     print(new_lst)
# lst = [2, 3, 4, 5, 6]
# mult_lst(lst)
# lst = list(map(int, input("Введите числа через пробел:\n").split()))
# mult_lst(lst)


# Задайте список из вещественных чисел. 
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
#   [1.1, 1.2, 3.1, 5, 10.01] => 0.19

# list_num =[1.1, 1.2, 3.1, 5, 10.01]
# ost_list = []
# for i in range(len(list_num)):
#     a = int(list_num[i])
#     b= round(list_num[i] - int(list_num[i]), 2)
#     ost_list.append(b)
#     c_min = ost_list[0]
#     c_max = ost_list[0]
#     for j in ost_list:
#         if j < c_min:
#             c_min=j
#         else:
#             if j>c_max:
#                 c_max=j
# d=c_max-c_min

# print(d)


# lst = list(map(float, input("Введите числа через пробел:\n").split())) # Мы использовали list(), чтобы объект map был выведен как список, а не в трудной для интерпретации объектной форме, например: <map object at 0x7fc250003a58>. 
                                                                         #Объект map является итератором наших результатов, чтобы мы могли использовать его в цикле for или использовать list() для превращения в список


# new_lst = [round(i%1,2) for i in lst if i%1 != 0]
# print(max(new_lst) - min(new_lst))

# Задайте список из нескольких чисел. 
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
#   [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12


# def sum_odd_index(lst):
#     s = 0
#     for i in range(len(lst)):
#         if i % 2 != 0:
#             s += lst[i]
#     print(f"Сумма равна: {s}")

# lst = [2, 3, 5, 9, 3]
# sum_odd_index(lst)
# lst = list(map(int, input("Введите числа через пробел:\n").split()))  #Мы использовали list(), чтобы объект map был выведен как список, а не в трудной для интерпретации объектной форме, например: <map object at 0x7fc250003a58>. 
                                                                        #Объект map является итератором наших результатов, чтобы мы могли использовать его в цикле for или использовать list() для превращения в список
# sum_odd_index(lst)
