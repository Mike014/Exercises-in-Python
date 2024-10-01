# -*- coding: utf-8 -*-

def reverse_years(years):
    # This function sorts the list of years in descending order using bubble sort.

    for i in range(len(years)):
        # Iterate over the list multiple times
        for _ in range(len(years) - 1):
            # Compare each pair of adjacent elements
            if years[_] < years[_ + 1]:
                # Swap if the current element is less than the next element
                years[_], years[_ + 1] = years[_ + 1], years[_]

    return years

if __name__ == '__main__':
    # List of years as string
    years = ['1980', '1990', '2000', '2010', '2020']
    # Print the sorted list of years in descending order
    print(reverse_years(years))
