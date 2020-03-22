#!/usr/bin/env python3
import os
import queue
import time


class Scanner():
    def __init__(self):
        self.queue = queue.Queue()

    def get_file_list(self, current_directory, start=None):
        if not start:
            start = current_directory
        try:
            files = os.listdir(current_directory)
        except PermissionError:
            return
        for file in files:
            full_path = current_directory + "/" + file
            if os.path.isfile(full_path):
                self.queue.put(os.path.relpath(full_path, start))
            if os.path.isdir(full_path):
                self.get_file_list(full_path, start)

    def print_queue(self):
        size_maybe = self.queue.qsize()
        while not self.queue.empty():
            print(self.queue.get())
        print(size_maybe)


start_time = time.time()
sync_dir = "/home/wouter/Sources"
scanner = Scanner()
scanner.get_file_list(sync_dir)
time_delta1 = time.time() - start_time
scanner.print_queue()
time_delta2 = time.time() - start_time
print("\n{:.2f} seconds".format(time_delta1))
print("\n{:.2f} seconds".format(time_delta2))