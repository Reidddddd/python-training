"""
Keeping the Last N Items
"""
from collections import deque


def search(lines, pattern, history=5):
    previous_lines = deque(maxlen=history)
    for line in lines:
        if pattern in line:
            print('?', line)
            yield line, previous_lines
        previous_lines.append(line)


with open('D:/development/workspace/python-training/pc3/ch1/dsa/1.2.py') as f:
    for ln, prevlines in search(f, 'print', 2):
        for pline in prevlines:
            print(pline)
        print('!', ln)
        print('-'*20)
