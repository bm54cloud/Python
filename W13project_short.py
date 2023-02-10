#!/usr/bin/env python3.7

import os 

path = os.getcwd()
file_list = []

for item in os.listdir():
    file_details = os.stat(item)
    file_list.append({'path':path+'/'+item, 'size':file_details.st_size})

print(*file_list, sep="\n")