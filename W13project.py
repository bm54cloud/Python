#!/usr/bin/env python3.7

# Import OS module
import os 

# Build a script that extracts the name and size of a file in your current working directory
path = os.getcwd()

# Get list of all files in current working directory
dir_list = list(os.listdir(path))

# Create dictionary of all files in the current working directory
file_dict = dict()

# Get list of file sizes in current working directory
# Dictionary syntax is dict_name[key] = value
for item in dir_list:
    file_size = os.stat(item)
    file_dict[item] = file_size

# {:d} tells the formatter to treat the argument as an integer
# {}'.format(name)
for item in file_dict:
    print({"File: {:30s} Size: {:d} Bytes".format(item,file_dict[item].st_size)})

