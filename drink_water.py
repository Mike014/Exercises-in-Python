import math

def drink_water(bottle_height, bottle_radius, water_height, crow_mouth, little_stones):
    s = (bottle_height - crow_mouth - water_height) * bottle_radius**2 * math.pi 
    i = 0
    while s > 0 and i < len(little_stones):
        s -= little_stones[i]
        i += 1
    return little_stones[:i] if s <= 0 else 'The crow is dead.' 

# Test degli esempi forniti
print(drink_water(10, 2, 3, 4, [5, 6, 7, 8, 9, 10, 11, 12]))  # Debug output
assert drink_water(10, 2, 3, 4, [5, 6, 7, 8, 9, 10, 11, 12]) == [5, 6, 7, 8, 9, 10]
assert drink_water(20, 1, 2, 3, [4, 5, 6, 7, 8, 9, 10, 11, 12]) == [4, 5, 6, 7, 8, 9, 10]
assert drink_water(20, 1, 2, 3, [4, 5, 6, 7, 8, 9, 10]) == [4, 5, 6, 7, 8, 9, 10]
assert drink_water(20, 2, 15, 6, [4, 5, 6, 7, 8, 9, 10]) == []
assert drink_water(20, 2, 15, 5, [4, 5, 6, 7, 8, 9, 10]) == []
assert drink_water(20, 1, 2, 3, [4, 5, 6, 7, 8, 9]) == "The crow is dead."

print("Tutti i test sono passati!")
