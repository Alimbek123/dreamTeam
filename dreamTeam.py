# Task num 1
# Спросите у пользователя строку НА Английском или целое предложение и
# удалите все глассные буквы там.
# То что осталось от строки выведите на экран.
# Строка не должна быть короче 10 символов.

vowels = ['a','e','i','o','u']
string = input('type a text no less than 10 letters: ')

def remove_vowel(string):

    result = [i for i in string if i.lower() not in vowels]
    result = ''.join(result)
    return result
 
a = remove_vowel(string)
print(f'Left consonants are: {a}')


# Task num 10
# Если вы были на Луне сейчас, ваш вес будет 16,5% от вашего веса земли.
# Для его расчета необходимо умножить на 0,165.
# Если в ближайшие 15 лет ваш вес будет увеличиваться на 1 кг каждый год.
# Какой будет ваш вес каждый год на Луне в следующем 15 лет?

earth_weight = int(input('Type your mass in 2023: '))
moon_index = 0.165
moon_weight_2023 = earth_weight * moon_index
print('Ваш вес в 2023 году: ' + str(moon_weight_2023))

for i in range(1, 16):
    print(i, round(earth_weight * moon_index, 2))
    earth_weight += 1


# Task num 3:
# Вам даны 2 листа:

# list_1 = ['a', 'bc', 'de']
# list_2 = ['ab', 'c', 'de']

# Напишите функцию которая их принимает и сравнивает на равность.
# Пример где листы равны:

    # a + bc + de = abcde
    # ab + c + de = abcde

    # list_1 = ['123', 'abc', 'de']
    # list_2 = ['1', '23', 'abcde']

# Пример где листы НЕ равны:

    # a + cb + de = acbde
    # ab + c + de = abcde

    # list_1 = ['123', 'abc', 'de']
    # list_2 = ['123', 'de', 'abc']


list_1 = ['a', 'bc', 'de']
list_2 = ['ab', 'c', 'de']

def func(list1, list2):
    if list1 == list2: 
        return 'Yes, lists are equal'
    
print(func(list1='', list2=''))


# Task num 12
# Напишите функцию который будет конвертировать Фаренгейт в Цельсии и
# наоборот.

temp = float(input("ВВЕДИТЕ ЛЮБОЕ ЗНАЧЕНИЕ ПО ФАРЕНГЕЙТУ: "))

def func(temp):
    result_cal = (temp - 32) * 5/9
    return result_cal


calcius = int(input('ВВЕДИТЕ ЛЮБОЕ ЗНАЧЕНИЕ ПО ЦЕЛЬСИЮ: '))

def func2(calcius):
    result_temp = (calcius * 9%5) + 32
    return result_temp 

a = func(temp)
print(f'ВВЕДЕННОЕ ЗНАЧЕНИЕ ПО ФАРЕНГЕЙТУ БУДЕТ: {a} ПО ЦЕЛЬСИИ')

b = func2(calcius)
print(f'ВВЕДЕННОЕ ЗНАЧЕНИЕ ПО ЦЕЛЬСИИ БУДЕТ: {b} ПО ФОРЕНГЕЙТУ')



