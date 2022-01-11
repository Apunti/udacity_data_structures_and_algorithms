def rearrange_digits(input_list):
    sorted_list = None
    for num in input_list:
        if sorted_list is None:
            sorted_list = [num]
        else:
            sorted_list = insert_element(sorted_list, num)
    first = 0
    second = 0
    for i in range(len(sorted_list)):
        mod = i % 2
        div = i // 2
        if mod == 0:
            first += sorted_list[i] * 10 ** div
        elif mod == 1:
            second += sorted_list[i] * 10 ** div
    return first, second


def insert_element(num_list, num):
    length = len(num_list)
    middle = length // 2
    if length == 0:
        return [num]
    elif num > num_list[middle]:
        return num_list[:middle + 1] + insert_element(num_list[middle + 1:], num)
    elif num < num_list[middle]:
        return insert_element(num_list[:middle], num) + num_list[middle:]
    else:
        return num_list.insert(middle, num)


def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")


### TEST CASES ###

print(rearrange_digits([1, 2, 3, 4, 5]))
# `[542, 31]

print(rearrange_digits([1]))
# `[1,0]

print(rearrange_digits([4, 6, 2, 5, 9, 8]))
# [964, 852]
