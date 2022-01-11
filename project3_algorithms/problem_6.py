def get_min_max(ints):
    if len(ints) == 0:
        return None, None
    max_value = -1
    min_value = ints[0]
    for num in ints:
        if num > max_value:
            max_value = num
        if num < min_value:
            min_value = num
    return min_value, max_value


## Example Test Case of Ten Integers
print(get_min_max([3, 7, 23, 6, 4, 78, 4]))
# (3, 78)

print(get_min_max([0]))
# (0,0)

print(get_min_max([7, 7, 7, 7, 7, 7]))
# (7,7)

print(get_min_max([]))
# (None, None)
