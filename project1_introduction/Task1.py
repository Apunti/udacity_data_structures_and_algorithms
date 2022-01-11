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
TASK 1:
How many different telephone numbers are there in the records?
Print a message:
"There are <count> different telephone numbers in the records."
"""

counter = 0
telf_list = []
for tel1, tel2, _ in texts:
    if tel1 not in telf_list:
        counter += 1
        telf_list.append(tel1)
    if tel2 not in telf_list:
        counter += 1
        telf_list.append(tel2)

for tel1, tel2, _, _ in calls:
    if tel1 not in telf_list:
        counter += 1
        telf_list.append(tel1)
    if tel2 not in telf_list:
        counter += 1
        telf_list.append(tel2)

print("There are {} different telephone numbers in the records.".format(counter))
