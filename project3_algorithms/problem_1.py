def sqrt(number):
    if type(number) is not int:
        return "You must enter a number!"
    if number < 0:
        return "It must be a positive number!"
    if number == 1 or number == 0:
        return number
    else:
        return _sqrt(number, 0, number)


def _sqrt(number, min_value, max_value):
    middle = (min_value + max_value) // 2
    if middle == min_value:
        return min_value
    middle_power2 = middle ** 2
    if middle_power2 < number:
        return _sqrt(number, middle, max_value)
    elif middle_power2 > number:
        return _sqrt(number, min_value, middle)
    else:
        return middle


### TEST CASES ###
# The commented part is the expected output.

print(sqrt('s'))
# 'You must enter a number!'
print(sqrt(0))
# 0
print(sqrt(-1))
# 'It must be a positive number!'
print(sqrt(27))
# 5
