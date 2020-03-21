#!/usr/bin/env python3
import os

def get_file_list(current_directory):
    file_list = []
    files = os.listdir(current_directory)
    for file in files:
        full_path = os.path.join(current_directory, file)
        if os.path.isfile(full_path):
            file_list.append(os.path.relpath(full_path, start_path))
        if os.path.isdir(full_path):
            file_list += get_file_list(full_path)
    return file_list


sync_dir = "/home/wouter/Music"
os.chdir(sync_dir)
result = get_file_list("/home/wouter/Music")
print(result)
