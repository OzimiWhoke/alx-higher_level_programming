#!/usr/bin/node
import sys

def read_file_content(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            print(content)
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")

if len(sys.argv) < 2:
    print("Please provide the file path as an argument.")
else:
    file_path = sys.argv[1]
    read_file_content(file_path)
