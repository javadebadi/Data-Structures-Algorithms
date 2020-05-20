# Project 0


## About the data
The text and call data are provided in csv files.

The text data `text.csv` has the following columns: sending telephone number (`string`), receiving telephone number (`string`), timestamp of text message (`string`).

The call data (`call.csv`) has the following columns: calling telephone number (`string`), receiving telephone number (`string`), start timestamp of telephone call (`string`), duration of telephone call in seconds (`string`)

All telephone numbers are 10 or 11 numerical digits long. Each telephone number starts with a code indicating the location and/or type of the telephone number. There are three different kinds of telephone numbers, each with a different format:

- Fixed lines start with an area code enclosed in brackets. The area codes vary in length but always begin with 0. Example: "(022)40840621".
- Mobile numbers have no parentheses, but have a space in the middle of the number to help readability. The mobile code of a mobile number is its first four digits and they always start with 7, 8 or 9. Example: "93412 66159".
- Telemarketers' numbers have no parentheses or space, but start with the code 140. Example: "1402316533".


## Worst-case Big O estimation
In this section, we provide estimation for worst case order of the solution for each task.
### Task 0
```python
print("First record of texts, " + texts[0][0] + " texts " + texts[0][1] + " at time " + texts[0][2] )
print("Last record of calls, " + calls[-1][0] + " calls " + calls[-1][1] + " at time " + calls[-1][2] + ", lasting " + calls[-1][3] + " seconds")

```
The first line have these operations:
- a call of print function  (1)
- 6 strings concatenation (6 + 5)
- Indexing list 3 times and indexing the result again (3 + 3)    

Total operations = 18    
**Order = O(18) = O(1)**

The second line have these operations:
- a call of print function  (1)
- 6 strings concatenation (9 + 8)
- Indexing list 4 times and indexing the result again (4 + 4)    

Total operations = 26    
**Order = O(26) = O(1)**

**Order of Task 0 = O(1)**


### Task 1
```python
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
```

The run-time of this Task for large outputs depends mostly on two `for` loops and `set` function.

Time complexity of `append` function for a `list` object is **O(1)**. Thsu, if the number of rows in a csv file is n, then the order of each for loop computation (with two append) is **O(2n) = O(n)**. The set function in worst case has a time complexity of **O(n)**.

**Order of Task 1 = O(n)**

### Task 3
```python
longest_id = 0
longest = 0

for i in range(len(calls)):
    if longest < int(calls[i][3]):
        longest = int(calls[i][3])
        longest_id = i

print(calls[longest_id][0] + " spent the longest time, " + calls[longest_id][3] + " seconds, on the phone during September 2016.")
```

The tow first line: O(2) = O(1)
The for loop: the for loop in worst case has 4 times indexing of array, two call to int() , one comparison and two assignment, therefore it has order of O( (4+2+1+2)n ) = O(9n) = O(n)
The final line: O(4 + 4 + 3) = O(11) = O(1)

**Order of Task 2 = O(n)**
