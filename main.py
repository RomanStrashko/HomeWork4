# A. Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример:
# если k = 2, то многочлены могут быть => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

# import random

# k = int(input('Введите натуральную степень: '))
#
# koef = {}
# for i in range(k + 1):
#     koef[i] = random.randint(0, 100)
# print(koef)
#
# equation = ''
# for i in range(k, -1, -1):
#     if koef[i] != 0:
#         if koef[i] == 1:
#             if i == 1:
#                 equation += f'x+ '
#             elif i == 0:
#                 equation += f'1 '
#             else:
#                 equation += f'x**{i}+ '
#         else:
#             if i == 1:
#                 equation += f'{koef[i]}*x+ '
#             elif i == 0:
#                 equation += f'{koef[i]} '
#             else:
#                 equation += f'{koef[i]}*x**{i}+ '
#
# print(equation + '= 0')
#
#
# n = equation + '= 0'
# data = open('equation2.txt', 'w', encoding='UTF-8')
# data.writelines(n)
# data.close()

# 2 Вариант записи без close

# with open('equation2.txt', 'w', encoding='UTF-8') as data:
#     data.writelines(n)
#






# B. Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.

equation1 = '45*x**3+ 91*x**2+ 76*x+ 10 = 0'
equation2 = '72*x**3+ 87*x**2+ 67*x+ 21 = 0'

equation1 = equation1.replace(' ', '')
print(equation1)
equation1 = equation1[:-2].split('+')
# print(equation1)
list1 = []
for i in equation1:
    list1.append(i.split('*x')[0])
# print(list1)
my_dict1 = {}
for i in range(len(list1)):
    my_dict1[i] = list1[i]
my_dict3 = {}
my_dict3 = {keys: int(values) for keys, values in my_dict1.items()}
print(my_dict3)

equation2 = equation2.replace(' ', '')
print(equation2)
equation2 = equation2[:-2].split('+')
# print(equation2)
list2 = []
for i in equation2:
    list2.append(i.split('*x')[0])
# print(list2)
my_dict2 = {}
for i in range(len(list2)):
    my_dict2[i] = list2[i]
my_dict4 = {}
my_dict4 = {keys: int(values) for keys, values in my_dict2.items()}
print(my_dict4)

sum_dict = {}
for i in my_dict3:
    if my_dict3.get(i) and my_dict4.get(i):
        sum_dict[i] = my_dict3.get(i) + my_dict4.get(i)
# sum_dict1 = {}
# sum_dict1 = {keys: str(values) for keys, values in sum_dict.items()}
print(sum_dict)

def decode_equation(equation: dict) -> str:
    new_equation = ''
    first = True
    for (key, value) in equation.items():
        if value != 0:
            if first:
                if value > 0:
                    new_equation += f'{value}*x**{key} '
                else:
                    new_equation += f' - {abs(value)}*x**{key} '
                first = False
            else:
                if value ==1:
                    if key == 1:
                        new_equation += f' + x '
                    elif key == 0:
                        new_equation += f' + 1 '
                    else:
                        new_equation += f' + x**{key} '
                elif value > 1:
                    if key == 1:
                        new_equation += f' + {value}*x '
                    elif key == 0:
                        new_equation += f' + {value} '
                    else:
                        new_equation += f' + {value}*x**{key} '
                elif value == -1:
                    if key == 1:
                        new_equation += f' - x '
                    elif key == 0:
                        new_equation += f' - 1 '
                    else:
                        new_equation += f' - x**{key} '
                elif value < 1:
                    if key == 1:
                        new_equation += f' - {abs(value)}*x '
                    elif key == 0:
                        new_equation += f' - {abs(value)} '
                    else:
                        new_equation += f'- {abs(value)}*x**{key} '

    return new_equation + '= 0'
equation = decode_equation(sum_dict)
print(equation)

with open('sum_equations.txt', 'w', encoding='UTF-8') as data:
    data.writelines(equation)



