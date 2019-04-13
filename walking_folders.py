#!/usr/bin/env python
import os

START_FOLDER = "."

for curr_dir, folders, files in os.walk(START_FOLDER):
    if '.git' in curr_dir:
        continue
    print(curr_dir)
    for file_name in files:
        file_path = os.path.join(curr_dir, file_name)
        file_size = os.path.getsize(file_path)
        if file_name.endswith('.py') and file_size > 100:
                print("    {:6d} {}".format(file_size, file_name))

