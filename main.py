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
list_1 = [1, 3]
list_2 = [2, 2]
tuple_1 = 3, 3
tuple_2 = 4, 4
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
str_1 = "С"
str_2 = "A"
print(str_1 == str_2)
print(ord(str_1))
print(ord(str_2))
print(chr(71))
print(chr(102))

print('\nУсловная конструкция if')
if 1 > 2:
  print("Действительно, 1 > 2")
print('1>2 - ложь!')

print('\nЛогические операции')
var_1 = 5
if var_1 > 1 and var_1 < 10:
  print(var_1 + 1)

var_1 = 10
if not (var_1 > 1 and var_1 < 10):
  print(var_1 + 40)

var_1 = 2
if not var_1 < 1:
  print(var_1 + 5)

var_1 = 15
if var_1 < 1 or var_1 > 10:
  print(var_1 + 5)

var_1 = 10
if not (var_1 < 1 or var_1 > 10):
  print(var_1 + 20)

list_1 = [1, 2, 4, 6, 8, 12]
var_1 = 6
if var_1 in list_1:
  print("Really, list_1 contains the variable var_1")

var_1 = 1
if type(var_1) is int:
  print("Really, var_1 is integer")

print('\nУпражнение "Quiz"')
question_1 = 'У меня есть 4 лапы и хвост. Я очень умный. Я люблю играть с тобой. Когда я вижу кота, то говорю "Гав-гав". Кто я?'
question_2 = 'Я домашнее животное. Я мягкий и пушистый. Я люблю спать и пить молоко. Я не люблю мышей и собак. Я говорю "Мяу-мяу". Кто я?'
question_3 = 'Я большое сельскохозяйственное животное. Я могу быть черным, белым или коричневым. Я люблю есть зеленую травку. Я даю молоко. Я говорю "Му-му". Кто я?'
question_4 = 'У меня есть лапы и хвост. У меня нет зубов. Я могу плавать и нырять под водой. Я ношу свой дом с собой. Я - ... ?'
question_5 = 'Я живу в лесу. Я очень большой и пушистый. У меня большой нос, маленький хвост и четыре лапы. Я люблю есть рыбу и ягоды. Я - ...?'
answer_1 = "собака"
answer_2 = "кот"
answer_3 = "корова"
answer_4 = "черепаха"
answer_5 = "медведь"

result = 0
print(question_1)
user_answer = input()
if user_answer == answer_1:
  result+=1
  print('Вы ответили правильно!')
print(question_1)
user_answer = input()
if user_answer == answer_1:
  result+=1
 print('Вы ответили правильно!')
