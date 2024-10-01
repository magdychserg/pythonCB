#2.1. Напишите программу на Python, чтобы получить строку из заданной строки, в которой все вхождения ее первого символа
# были изменены на ‘$’, за исключением самого первого символа.
str_ = input('Введите строку: ')
result = str_[0] + str_[1:].replace(str_[0], '$')
print(result)

#2.2. Напишите программу на Python, чтобы получить одну строку из двух заданных строк, разделенных пробелом, и поменять
# местами первые два символа в каждой строке.
s1 = 'wollo'
s2 = 'Herld!'

s1, s2 = s2[:2] + s1[2:], s1[:2] + s2[2:]
print(s1, s2)
#2.3. Напишите скрипт на Python, который принимает входные данные от пользователя и отображает их обратно в верхнем и
#нижнем регистрах.
s = input()
print(s.lower(), s.upper())

#2.4. Получить из строки travel такой список городов: [‘Москва’, ‘Красноярск’, ‘Новосибирск’, ‘Челябинск’, ‘Магадан’,
# ‘Петропавловск-Камчатский’, ‘Курск’]
travel = "Города посещения Москва, Красноярск, Новосибирск, Челябинск, Магадан, Петропавловск-Камчатский, Курск"
result = list(travel.split(" "))
del result[0:2]
print(result)

#2.5. Получить из строк travel_1, travel_1 итоговый список result, в котором отсутствуют дубликаты наименований городов :
#[‘Москва’, ‘Красноярск’, ‘Новосибирск’, ‘Челябинск’, ‘Магадан’, ‘Петропавловск-Камчатский’, ‘Курск’]
travel_1 = "Города посещения Москва, Красноярск, Новосибирск, Челябинск, Магадан, Петропавловск-Камчатский, Курск"
travel_2 = "Города посещения Москва, Санкт-Петербург, Челябинск, Златоуст, Уфа, Самара, Курск, Новосибирск"
result_1 = list(travel_1.split(" "))
result_2 = list(travel_2.split(" "))
del result_1[0:2]
del result_2[0:2]
result = set(result_1 + result_2)
print(result)

#2.6 Из строк travel_1 и travel_2 получить список городов, которые присутствуют в обоих турах (пересечение).
#В данном случае, результатом должен быть такой список: [‘Москва’, ‘Челябинск’, ‘Курск’, ‘Новосибирск’]

travel_1 = "Города посещения Москва, Красноярск, Новосибирск, Челябинск, Магадан, Петропавловск-Камчатский, Курск"
travel_2 = "Города посещения Москва, Санкт-Петербург, Челябинск, Златоуст, Новосибирск, Уфа, Самара, Курск"
result_1 = list(travel_1.split(" "))
result_2 = list(travel_2.split(" "))
del result_1[0:2]
del result_2[0:2]
#resul_1 = set([result_1])
#resul_2 = set([result_2])
print(result_1)
print(result_2)
result = list(set(result_1) & set(result_2))
print(result)

#2.7 Обработать строку info и вывести информацию на стандартный поток вывода в виде:
#Город Красноярск Год основания 1628 Население 1205473 Площадь (кв.км) 413 Среднегодовая температура +2.0

info = 'Красноя́рск 1628 1205473 413 +2.0'

result = (list(info.split(" ")))
print('Город', result[0], 'Год основания', result[1], 'Население', result[2], 'Площадь', result[3], 'Температура',
      result[4])
#
