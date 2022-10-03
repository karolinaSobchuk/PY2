#Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях. 
#Позиции хранятся в файле file.txt в одной строке одно число.

from random import randint
numbers = []
for i in range(5):
    numbers.append(randint (-5,5))
print(numbers)

def get_numbers(numbers):
    count =0 
    for element in numbers:
        count +=1
    return count
print('Числа: ', get_numbers(numbers))

x = int(input('Укажите позицию 1 элемента: '))
y = int(input('Укажите позицию второго элемента: '))

for i in range(len(numbers)):
    mult = numbers[x -1]*numbers[y - 1]
print(f'Ответ:  {mult}')



