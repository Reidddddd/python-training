"""
Name Tuple
Add the ability to access fields by name instead of position index.
"""
from collections import namedtuple
from enum import Enum
import csv
import sqlite3

Point = namedtuple('Point', ['x', 'y'])
p = Point(11, y=22)
print(p[0] + p[1])
x, y = p
print(x, y)
print(p.x + p.y)
print(p)
print()

# EmployeeRecord = namedtuple('EmployeeRecord', 'name, age, title, department, paygrade')
# for emp in map(EmployeeRecord._make, csv.reader(open("employee.csv", "rb"))):
#     print(emp.name, emp.title)
# print()
#
# conn = sqlite3.connect('/companydata')
# cursor = conn.cursor()
# cursor.execute('SELECT name, age, title, department, paygrade FROM employees')
# for emp in map(EmployeeRecord._make, cursor.fetchall()):
#     print(emp.name, emp.title)
# print()

t = [12, 22]
p2 = Point._make(t)
print(p2)
print()

p = Point(x=11, y=22)
print(p._asdict())
print()

pr = p._replace(x=88)
print("replace", pr)
print()

print(p._fields)
Color = namedtuple('Color', 'red green blue')
Pixel = namedtuple('Pixel', Point._fields + Color._fields)
pixel = Pixel(11, 22, 128, 255, 0)
print(pixel)
print(getattr(pixel, 'green'))
print()

d = {'x': 81, 'y': 22}
pt = Point(**d)
print(pt)
print()


class Point2(namedtuple('Point', 'x y')):
    __slots__ = ()

    @property
    def hypot(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def __str__(self):
        return 'Point: x=%6.3f y=%6.3f hypot=%6.3f' % (self.x, self.y, self.hypot)


for p in Point2(3, 4), Point2(14, 5 / 7):
    print(p)
print()

Point3D = namedtuple('Point3D', Point._fields + ('z',))
Account = namedtuple('Account', 'owner balance transaction_count')
default_account = Account('<owner name>', 0.0, 0)
johns_account = default_account._replace(owner='John')
janes_account = default_account._replace(owner='Jane')
print(johns_account)
print()

Status = namedtuple('Status', 'open pending closed')._make(range(3))
print(Status.open, Status.pending, Status.closed)


class Status(Enum):
    open, pending, closed = range(3)
