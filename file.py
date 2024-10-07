# file_handling_assignment.py

# Task 1: File Creation
try:
    with open('my_file.txt', 'w') as f:
        f.write('Hello, this is my file!\n')
        f.write('Python file handling is interesting.\n')
        f.write('Here are some numbers: 1, 2, 3.\n')
except PermissionError:
    print('Error: Permission denied to create my_file.txt.')
finally:
    print('File creation attempt complete.')

# Task 2: File Reading and Display
try:
    with open('my_file.txt', 'r') as f:
        contents = f.read()
        print(contents)
except FileNotFoundError:
    print('Error: my_file.txt not found.')
except PermissionError:
    print('Error: Permission denied to read my_file.txt.')
finally:
    print('Read operation complete.')

# Task 3: File Appending
try:
    with open('my_file.txt', 'a') as f:
        f.write('File handling in python is essential for every programmer.\n')
        f.write('Appending files include adding more context to them.\n')
        f.write('It is crucial to organize your work in files.\n')
except PermissionError:
    print('Error: Permission denied to append to my_file.txt.')
finally:
    print('Append operation complete.')

# Final Read to Show All Content
try:
    with open('my_file.txt', 'r') as f:
        contents = f.read()
        print(contents)
except FileNotFoundError:
    print('Error: my_file.txt not found.')
except PermissionError:
    print('Error: Permission denied to read my_file.txt.')
finally:
    print('Final read operation complete.')