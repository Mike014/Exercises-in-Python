# -*- coding: utf-8 -*-
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"This is the original list: {numbers}\n")

# Lista di esempio
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Estrarre i primi 5 elementi
first_five = numbers[:5]
print(f"First five elements: {first_five}\n")

# Estrarre gli ultimi 5 elementi
last_five = numbers[-5:]
print(f"Last five elements: {last_five}\n")

# Estrarre elementi dal 3° al 7° (indice 2 a 6)
middle_slice = numbers[2:7]
print(f"Middle slice: {middle_slice}\n")

# Estrarre ogni secondo elemento
every_second = numbers[::2]
print(f"Every second element: {every_second}\n")

# Estrarre ogni terzo elemento
every_third = numbers[::3]
print(f"Every third element: {every_third}\n")

# Estrarre elementi in ordine inverso
reversed_list = numbers[::-1]
print(f"Reversed list: {reversed_list}\n")

# Estrarre elementi dal 2° al penultimo (indice 1 a -1)
second_to_penultimate = numbers[1:-1]
print(f"Second to penultimate: {second_to_penultimate}\n")

# Estrarre gli ultimi 3 elementi in ordine inverso
last_three_reversed = numbers[:-4:-1]
print(f"Last three elements reversed: {last_three_reversed}\n")

# Estrarre elementi dal 4° al 2° in ordine inverso (indice 3 a 1)
reverse_middle_slice = numbers[3:0:-1]
print(f"Reverse middle slice: {reverse_middle_slice}\n")

# Estrarre ogni secondo elemento a partire dal 2° (indice 1)
every_second_from_second = numbers[1::2]
print(f"Every second element from second: {every_second_from_second}\n")

# Estrarre ogni secondo elemento fino al penultimo (indice -1)
every_second_to_penultimate = numbers[:-1:2]
print(f"Every second element to penultimate: {every_second_to_penultimate}\n")


