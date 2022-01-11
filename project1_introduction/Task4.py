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
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

not_telemarketers = []
for tel1, tel2, _ in texts:
    if tel1 not in not_telemarketers:
        not_telemarketers.append(tel1)
    if tel2 not in not_telemarketers:
        not_telemarketers.append(tel1)
for _, tel2, _, _ in calls:
    if tel2 not in not_telemarketers:
        not_telemarketers.append(tel2)

list_telemarketers = []
for tel1, _, _, _ in calls:
    if tel1 not in list_telemarketers:
        if tel1 not in not_telemarketers:
            list_telemarketers.append(tel1)

list_telemarketers.sort()

print("These numbers could be telemarketers", *list_telemarketers, sep='\n')
