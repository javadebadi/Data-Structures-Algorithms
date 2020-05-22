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

text_recieving_numbers = set()
text_sending_numbers = set()
call_recieving_numbers = set()
call_making_numbers = set()

for text in texts:
    text_sending_numbers.add(text[0])
    text_recieving_numbers.add(text[1])

for call in calls:
    call_making_numbers.add(call[0])
    call_recieving_numbers.add(call[1])

telemarketers = call_making_numbers - (text_sending_numbers | text_recieving_numbers | call_recieving_numbers)

print("These numbers could be telemarketers: ")
for number in telemarketers:
    print(number)
