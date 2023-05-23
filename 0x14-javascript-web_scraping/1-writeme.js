#!/usr/bin/node

import sys

def write_to_file(file_path, content):
    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(content)
            print("Content successfully written to the file.")
    except Exception as e:
        print(f"An error occurred while writing to the file: {e}")

if len(sys.argv) < 3:
    print("Please provide the file path and content as arguments.")
else:
    file_path = sys.argv[1]
    content = sys.argv[2]
    write_to_file(file_path, content)
