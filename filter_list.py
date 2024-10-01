from collections import Counter

def delete_nth(order,max_e):
    new_lst = []
    counts = Counter()

    for i in order:
        if counts[i] < max_e:
            new_lst.append(i)
            counts[i] += 1

    return new_lst

# Test the function
print(delete_nth([1, 2, 3, 1, 2, 1, 2, 3], 2))  # Output: [1, 2, 3, 1, 2, 3]
print(delete_nth([20, 37, 20, 21], 1))         # Output: [20, 37, 21]




