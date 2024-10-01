# -*- coding: utf-8 -*-

def likes(names):
    match names:
        case []: return 'no one likes this'
        case [a]: return f'{a} likes this'
        case [a, b]: return f'{a} and {b} like this'
        case [a, b, c]: return f'{a}, {b} and {c} like this'
        case [a, b, *rest]: return f'{a}, {b} and {len(rest)} others like this'

# Test degli esempi forniti
print(likes([]))  # Output: 'no one likes this'
print(likes(['Peter']))  # Output: 'Peter likes this'
print(likes(['Jacob', 'Alex']))  # Output: 'Jacob and Alex like this'
print(likes(['Max', 'John', 'Mark']))  # Output: 'Max, John and Mark like this'
print(likes(['Alex', 'Jacob', 'Mark', 'Max']))  # Output: 'Alex, Jacob and 2 others like this'
















