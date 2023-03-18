var_1 = 5
var_2 = 3
print(var_1 + var_2)
print(var_1 - var_2)
print(var_1 * var_2)
print(var_1 / var_2)
print(var_1**var_2)
print(var_1 // var_2)
print(var_1 % var_2)

print('\nСложение списков и кортежей')
list_1 = [1,1]
list_2 = [2,2]
tuple_1 = 3,3
tuple_2 = 4,4
print(list_1 + list_2)
print(tuple_1 + tuple_2)
print(list_1 * 3)
print(tuple_1 * 3)

print('\nУсловные операции')
var_1 = 2
var_2 = 1.1
var_3 = 3
var_4 = 3
print(var_1 > var_2)
print(var_1 < var_2)
print(var_1 >= var_2)
print(var_1 <= var_2)
print(var_3 >= var_4)
print(var_3 <= var_4)
print(var_1 != var_2)
print(var_3 == var_4)

print('\nСравнение строковых типов')
str_1 = "C"
str_2 = "С"
print(str_1 < str_2)
print(ord(str_1))
print(ord(str_2))
print(chr(70))
print(chr(102))

print('\nУсловная конструкция if')
if 1>2:
 print("Действительно, 1 > 2")
print ('1>2 - ложь!')

print('\nЛогические операции')
var_1 = 5
if var_1 > 1 and var_1 < 10:
 print(var_1 + 1)

var_1 = 15
if var_1 < 1 or var_1 > 10:
 print(var_1 + 5)

list_1 = [1, 2, 4, 6, 8, 12]
var_1 = 6
if var_1 in list_1:
 print("Really, list_1 contains the variable var_1")

var_1 = 1
if type(var_1) is int:
 print("Really, var_1 is integer")