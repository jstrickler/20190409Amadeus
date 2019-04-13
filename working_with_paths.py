#!/usr/bin/env python
import sys
import os
from datetime import datetime

folder_name = 'DATA'
file_name = 'alice.txt'

file_path = os.path.join(folder_name, file_name)

print("file path:", file_path)

with open(file_path) as file_in:
    pass

file_size = os.path.getsize(file_path)
print("file size:", file_size)
raw_timestamp = os.path.getmtime(file_path)
print("raw timestamp:", raw_timestamp)
timestamp = datetime.fromtimestamp(raw_timestamp)
print("file timestamp:", timestamp)

print("folder:", os.path.dirname(file_path))
print("basename:", os.path.basename(file_path))
print("absolute path:", os.path.abspath(file_path))

for x in file_path, "DATA", "DATA/betsy.txt":
    print(x, end=' ')
    print(os.path.exists(x), end=' ')
    print(os.path.isdir(x), end=' ')
    print(os.path.isfile(x), end=' ')
    print(bool(os.access(x, os.R_OK | os.W_OK)))
