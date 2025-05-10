import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from utils import print_separator, print_file_header

print_file_header("11-python_file_handling.py")

"""
    File Handling:
        - open (<file_name> <file_path>, <mode>)
            * file_path:
                . relative path: ./file.txt
                . absolute path: /Users/username/Desktop/file.txt
            * file_name:
                . file.txt
                . file.csv
            * mode: 
                . r: read              =>  open & read for (text format)
                . r+: read and write   =>  open & read and write for (text format)
                . w: write             =>  open & write for (text format)
                . a: append            =>  open & append for (text format)

                . rb: binary mode      =>  open & read for (binary format)
                . rb+: binary mode     =>  open & read and write for (binary format)
                . wb: binary mode      =>  open & write for (binary format)
                . ab: binary mode      =>  open & append for (binary format)

        - close(<file_object>)         => doesn't take any arguments

        Note:
            - with open (<filename> <file_path>, <mode>) as <file_object>:
                . automatically closes the file after the block is executed
"""

script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, "test.txt")

file = open(file_path, mode = 'r')

print(file.readline())

file.close()

print_separator()

# better at exception handling and will close the file automatically
with open(file_path, mode = 'r') as file:
    print(file.readline())

print_separator()

'''
    file are used to permentaly store data
        - data is stored in the disk
        - data is not lost when the program is closed

    but with the variables, the data is lost when the program is closed
    or computer is turned off because it is stored in the RAM (Random Access Memory)
'''

# Create new file in the same directory as the script, because we are using docker container
new_file_path = os.path.join(script_dir, 'new_file.txt')

try:
    with open(new_file_path, 'w') as file:
        file.write('Hello there\n')
    with open(new_file_path, 'a') as file:
        file.writelines(['More text\n', 'A bit more text\n'])
except FileNotFoundError as e:
    print("Error: File not found: ", e)
except Exception as e:
    print("Error: something went wrong: ", e)
finally:
    print('File closed')

print_separator()

try:
    with open(new_file_path, 'r') as file:
        print("File content:")
        print (file.read())
    print_separator()
    with open(new_file_path, 'r') as file:
        print("First line: ", file.readline())
        print("Second line: ", file.readline())
        print("Third line: ", file.readline())
        print("Fourth line: ", file.readline())
        print("Fifth line: ", file.readline())
    print_separator()
    with open(new_file_path, 'r') as file:
        print("\nRead all lines and store in a list: ", file.readlines())
    print_separator()
    with open(new_file_path, 'r') as file: # this returns a list by default
        for line in file:
            print ("line = ", line)
except FileNotFoundError as e:
    print("Error: File not found: ", e)
except Exception as e:
    print("Error: something went wrong: ", e)