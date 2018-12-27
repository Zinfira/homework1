_author_ = 'Safargalieva Zinfira Ismagilovna'

print("Task №1")
number = input("Введите число: ")
i = 1
max_number = number[0]
while i<len(number):
    if int(max_number)<int(number[i]):
        max_number = number[i]
    i += 1

print("Большая цифра этого числа ", max_number)
