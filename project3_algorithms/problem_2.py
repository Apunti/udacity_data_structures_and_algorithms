def rotated_array_search(input_list, number):
    if type(number) is not int:
        return 'You must enter a number!'
    return _rotated_array_search(input_list[0], input_list, 0, len(input_list) - 1, number)


def _rotated_array_search(first_item, input_list, min_value, max_value, number):
    middle = (min_value + max_value) // 2
    if middle == min_value:
        if input_list[min_value] == number:
            return min_value
        elif input_list[max_value] == number:
            return max_value
        else:
            return -1
    if input_list[middle] < first_item:
        if number >= first_item:
            return _rotated_array_search(first_item, input_list, min_value, middle - 1, number)
        else:
            if number > input_list[middle]:
                return _rotated_array_search(first_item, input_list, middle + 1, max_value, number)
            elif number == input_list[middle]:
                return middle
            else:
                return _rotated_array_search(first_item, input_list, min_value + 1, middle - 1, number)
    elif input_list[middle] > first_item:
        if number < first_item:
            return _rotated_array_search(first_item, input_list, middle, max_value, number)
        else:
            if number < input_list[middle]:
                return _rotated_array_search(first_item, input_list, min_value, middle - 1, number)
            elif number > input_list[middle]:
                return _rotated_array_search(first_item, input_list, middle + 1, max_value, number)
            else:
                return middle


def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1


def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")


### TEST CASES ###

print(rotated_array_search([6, 7, 8, 9, 10, 1, 2, 3, 4], 1))
# 5
print(rotated_array_search([6, 7, 8, 9, 10, 1, 2, 3, 4], 0))
# -1
print(rotated_array_search([6, 7, 8, 9, 10, 1, 2, 3, 4], 's'))
# 'You must enter a number!'
