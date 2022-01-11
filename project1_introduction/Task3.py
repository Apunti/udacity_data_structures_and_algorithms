"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""
counter_080 = 0
counter_total = 0
area_set = set()
for tel1, tel2, _, _ in calls:
    if tel1[:5] == '(080)':
        counter_total += 1
        if tel2[0] == '(':
            index = tel2.find(')')
            area_set.add(tel2[:index] + tel2[index])
            if tel2[:5] == '(080)':
                counter_080 += 1
        elif tel2[:3] == '140':
            area_set.add(tel2[:3])
        elif tel2[0] in ['7', '8', '9']:
            area_set.add(tel2[:4])

if counter_total == 0:
    counter_total = 1

percentage = round(counter_080 * 100 / counter_total, 2)

area_list = sorted(list(area_set))

print("The numbers called by people in Bangalore have codes:", *area_list, sep='\n')

print(
    "{} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.".format(percentage))
