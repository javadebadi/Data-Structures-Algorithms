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

telephone_number_list = []

# append telephone numbers in texts file to telephone_number_list
for text in texts:
    telephone_number_list.append(text[0])
    telephone_number_list.append(text[1])
# append telephone numbers in calls file to telephone_number_list
for call in calls:
    telephone_number_list.append(call[0])
    telephone_number_list.append(call[1])

# find distinct telephone numbers
telephone_number_set = set(telephone_number_list)

# print length of list of telephone numbers
print(len(telephone_number_list))
# print number of distinct telephone numbers
count = len(telephone_number_set)
print("There are " + str(count) + " different telephone numbers in the records.")
