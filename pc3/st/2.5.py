"""
Searching and Replacing Text
"""
import re
from calendar import month_abbr

text = 'yeah, but no, but yeah, but no, but yeah'
print(text.replace('yeah', 'yep'))

text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
# first pattern to match, second is to replace \3 (group number)
print(re.sub(r'(\d+)/(\d+)/(\d+)', r'\3-\1-\2', text))
datapat = re.compile(r'(\d+)/(\d+)/(\d+)')
print(datapat.sub(r'\3-\1-\2', text))


def change_date(m):
    mon_name = month_abbr[int(m.group(1))]
    return '{} {} {}'.format(m.group(2), mon_name, m.group(3))


print(datapat.sub(change_date, text))
newtext, n = datapat.subn(r'\3-\1-\2', text)
print(newtext)
print(n)
