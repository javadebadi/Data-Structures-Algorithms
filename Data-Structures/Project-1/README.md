# Project 1
## Data Structures

### Problem 2: Finding File
For this problem, the goal is to write code for finding all files under a directory (and all directories beneath it) that end with ".c".     
Skills:
- Using Python `os` module
- Recursion

>- Problem 2
  .Algorithm:
    - create a list to store path of ".c" files (list_of_c_files)
    - list all file and directories in a path
    - add ".c" files to list_of_c_files
    - repeat the last two line above for directories inside the path and add path of ".c" files to list_of_c_files
