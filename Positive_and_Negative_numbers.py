import random 

positive_even_number = random.randrange(2, 101, 9)
negative_even_number = random.randrange(-100, -1, 9)
list_positive_numbers = []
list_negative_numbers = []

def loop_numbers():
    for i in range(2, 101, 9):
        list_positive_numbers.append(i)
    
    for i in range(-100, 0, 9):
        list_negative_numbers.append(i)

    print(f"Positive numbers: {list_positive_numbers}")
    print(f"Negative numbers: {list_negative_numbers}")
    
def printumbers():
    for i in range(len(list_positive_numbers)):
        if list_positive_numbers[i] % 2 == 0:
            print(f"Positive even number: {list_positive_numbers[i]}")

    for i in range(len(list_negative_numbers)):
        if list_negative_numbers[i] % 2 == 0:
            print(f"Negative even number: {list_negative_numbers[i]}")

if __name__ == '__main__':
    loop_numbers()
    printumbers()
    print('End of program')




