# Task num 1

vowels = ['a','e','i','o','u']
string = input('type a text no less than 10 letters: ')

def remove_vowel(string):

    result = [i for i in string if i.lower() not in vowels]
    result = ''.join(result)
    return result
 
a = remove_vowel(string)
print(f'Left consonants are: {a}')


# Task num 10

earth_weight = int(input('Type your mass in 2023: '))
moon_index = 0.165
moon_weight_2023 = earth_weight * moon_index
print('Ваш вес в 2023 году: ' + str(moon_weight_2023))

for i in range(1, 16):
    print(i, round(earth_weight * moon_index, 2))
    earth_weight += 1


# Task num 3:

list_1 = ['a', 'bc', 'de']
list_2 = ['ab', 'c', 'de']

def func(list1, list2):
    if list1 == list2: 
        return 'Yes, lists are equal'
    
print(func(list1='', list2=''))


# Task num 12

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



