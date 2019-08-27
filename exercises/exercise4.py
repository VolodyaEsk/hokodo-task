"""
Command to run the program:
    python exercise4.py < exercise4_data.txt
"""

import fileinput

output = []

for line in fileinput.input():
    name, age, height = map(str.strip, line.split(','))
    output.append((name, age, height))

output.sort(key=lambda x: x)
print(output)

