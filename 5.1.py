import csv
from os import fdopen
import sys

filename = "rebiata1.txt"
fd = open(filename, "r")
reader = csv.reader(fd, delimiter="\t")
for row in reader:
    print(row)

filename = "rebiata2.txt"
fd = open(filename, "r")
reader = csv.reader(fd, delimiter="\t")
for row in reader:
    print(row)

print("Бажаєте порівняти групи? Введіть (2) якщо бажаєте порівняти")
x = int(input())
if x > 2:
    print("Добре, тоді до зустрічі")
if x <= 2:
    import filecmp 
similar = filecmp.cmp('rebiata1.txt', 'rebiata2.txt') 
print(similar) 

print("На цьому все")


  



