def sort_012(input_list):
    i = 0
    count = 0
    while i < len(input_list) - 1:
        if not input_list[i] in [0, 1, 2]:
            return 'The input list is not correct'
        if len(input_list) - 1 <= count + i:
            return input_list
        if input_list[i] == 0:
            del input_list[i]
            input_list.insert(0, 0)
            i += 1
        elif input_list[i] == 2:
            del input_list[i]
            input_list.append(2)
            count += 1
        elif input_list[i] == 1:
            i += 1
    return input_list


def test_function(test_case):
    sorted_array = sort_012(test_case)
    print(sorted_array)
    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")


### TEST CASES ###

print(sort_012([0, 2, 1, 0, 0, 2, 1, 0, 2, 1]))
# [0,0,0,0,1,1,1,2,2,2]

print(sort_012([]))
# []

print(sort_012([2, 2, 3]))
# 'The input list is not correct'
