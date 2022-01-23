#1. Задачка: 
#Дан строка, она состоит только из букв английского алфавита.
#Первый участник пишет сбор статистики - какие буквы сколько
#раз встречаются.
#Второй участник клонирует к себе репозиторий и
#пишет вывод на экран самой часто встречающейся буквы
#без использования функций max, sorted и т.д.
#Изменения производить в своей ветке!
#Загружать на github свою ветку!
#Первый участник скачивает к себе ветку с изменениями,
#проверяет код, соединяет ветки, снова кладет на github.

check_string = input("Write a string: ")

count = {}

for s in check_string:
  if s in count:
    count[s] += 1
  else:
    count[s] = 1

for key in count:
  if count[key] >= 1:
    print (key, count[key])

max_num = 0

for word in count.keys():
    if count[word] > max_num:
        max_num = count[word]
print("Max number:", max_num)

