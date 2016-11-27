"""
Sorting a List of Dictionaries by a Common Key
"""
from operator import itemgetter

rows = [
    {'fname': 'brian', 'lname': 'jones', 'uid': 1003},
    {'fname': 'david', 'lname': 'beazley', 'uid': 1002},
    {'fname': 'john', 'lname': 'cleese', 'uid': 1001},
    {'fname': 'big', 'lname': 'jones', 'uid': 1004}
]
rows_by_fname = sorted(rows, key=itemgetter('fname'))
rows_by_uid = sorted(rows, key=itemgetter('uid'))
print(rows_by_fname)
print(rows_by_uid)
rows_by_lfname = sorted(rows, key=itemgetter('lname', 'fname'))
print(rows_by_lfname)
print()

rbfname = sorted(rows, key=lambda r: r['fname'])
rblfname = sorted(rows, key=lambda r: (r['lname'], r['fname']))

print(min(rows, key=itemgetter('uid')))
print(max(rows, key=itemgetter('uid')))
