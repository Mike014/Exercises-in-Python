from itertools import groupby

def sum_consecutives(lst):
    return [sum(group) for key, group in groupby(lst)]





