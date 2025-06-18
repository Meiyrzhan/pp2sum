import os
#Exercise 1-------------------------------------------------------------------------------------------------
import os

path = input("Enter the path: ")

print("\nDirectories:")
print([d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))])

print("\nFiles:")
print([f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))])

print("\nAll contents:")
print(os.listdir(path))

#Exercise 2-------------------------------------------------------------------------------------------------
import os

path = input("Enter the path to check: ")

print(f"Exists: {os.path.exists(path)}")
print(f"Readable: {os.access(path, os.R_OK)}")
print(f"Writable: {os.access(path, os.W_OK)}")
print(f"Executable: {os.access(path, os.X_OK)}")

#Exercise 3-------------------------------------------------------------------------------------------------
import os

path = input("Enter a path: ")

if os.path.exists(path):
    print("Path exists.")
    print("Directory part:", os.path.dirname(path))
    print("File part:", os.path.basename(path))
else:
    print("Path does not exist.")

#Exercise 4-------------------------------------------------------------------------------------------------
file_path = input("Enter file path: ")

try:
    with open(file_path, 'r') as file:
        lines = file.readlines()
        print(f"Number of lines: {len(lines)}")
except FileNotFoundError:
    print("File not found.")

#Exercise 5-------------------------------------------------------------------------------------------------
data = ['apple', 'banana', 'cherry']

with open('output.txt', 'w') as f:
    for item in data:
        f.write(item + '\n')

print("List written to 'output.txt'")

#Exercise 6-------------------------------------------------------------------------------------------------
import string

for letter in string.ascii_uppercase:
    with open(f"{letter}.txt", "w") as f:
        f.write(f"This is file {letter}.txt\n")

print("26 files created.")

#Exercise 7-------------------------------------------------------------------------------------------------
src = input("Enter source file path: ")
dst = input("Enter destination file path: ")

try:
    with open(src, 'r') as f1, open(dst, 'w') as f2:
        f2.write(f1.read())
    print("File copied successfully.")
except FileNotFoundError:
    print("Source file not found.")

#Exercise 8-------------------------------------------------------------------------------------------------
import os

file_path = input("Enter file path to delete: ")

if os.path.exists(file_path):
    if os.access(file_path, os.W_OK):
        os.remove(file_path)
        print("File deleted.")
    else:
        print("No write access to the file.")
else:
    print("File does not exist.")

