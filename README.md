# Data-Structures-Algorithms
Udacity Data Structures and Algorithms Nanodegree

## Introduction
### Efficiency
Writing efficient codes is very important. Efficiency is important in **time** and **space**.    
Usually, there is a tradeoff between time and space efficiency. The faster **algorithms** usually need bigger **memory**, and using less **memory** slows down the program.

<img alt="Comparison computational complexity" src="https://upload.wikimedia.org/wikipedia/commons/7/7e/Comparison_computational_complexity.svg" width="50%">  

Comparison computational complexity. The Figure is take from [Wikipdia](https://upload.wikimedia.org/wikipedia/commons/7/7e/Comparison_computational_complexity.svg). The x-axis shows the number of input and the y-axis shows the computational complexity of a computation.

There are two points:    
1- As the input to an algorithm increases, the run time  of the algorithm may also increase     
2- Different algorithms may increase at different orders

### Order
The rate of increase for number of operations of an algorithm with respect to number of inputs is called **order** and denoted by **O**.

computational complexity | N | **O**(n)
--- | --- | ---
linear | n | O(n)
quadratic | n<sup>2</sup> | O(n<sup>2</sup>)

The [Big O cheatsheet](https://www.bigocheatsheet.com/) describes the order of each data structure for any operation. The same for python language is [here](https://wiki.python.org/moin/TimeComplexity).

## Data Structures
### Arrays and Linked Lists
#### Collection
Collection is a generic type of data structure. It is just group of objects.
- no particular order
- no requirements to have objects of the same type
#### Lists
- order (access elements by ordered numbers)
- no fixed length (add or remove elements)
#### Arrays
Arrays are lists which have other properties:
- order
- fixed size
- elements of arrays are build next to each other in memory
- all elements of an array have the same size
- we can use index to point to location of each element in arrays

Python `list`s are essentially dynamic arrays by these definitions. Python `string`s are arrays too.

### Maps and Hashing

#### Set
Set is a data structure which is similar to list, but :
- set does not have intrinsic order unlike list
- No value is repeated in set

#### Map
Map is a set based data structure. Each element in map is pairwise element of <key, value>. The keys in Map data structure has a set data structure.

Python dictionary `dict` is a built-in map data structure.

#### Hash function
Hash function is maps a **value** to **hash value**.     
Hash functions are these really incredible `magic` functions which can map data of any size to a fixed size data. This fixed sized data is often called hash code or hash digest.   
Hash Maps    
Constant time lookups

## Basic Algorithms

## Advanced Algorithms
