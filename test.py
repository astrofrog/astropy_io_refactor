from __future__ import print_function

from table import Table

print(Table.read.__doc__)

t = Table.read('data.txt')

print(t)