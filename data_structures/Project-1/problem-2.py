# Finding files
import os

def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """
    list_of_paths_endswith_c = []  #  a list to append path of all .c files

    # find path of all file and directories of given path
    all_files_paths = [os.path.join(path ,dir) for dir in os.listdir(path)]

    for path in all_files_paths:
        if path.endswith(".c"):  #  append .c files to list of .c files
            list_of_paths_endswith_c.append(path)
        elif os.path.isdir(path): #  check for subdirectores
            #  then add list of .c files in subdirectores using Recursion
            list_of_paths_endswith_c.extend(find_files(suffix, path))


    return list_of_paths_endswith_c

print(find_files(".c","testdir"))
