print("QUESTION--1")
'''print("We represent time in a way that’s easy for us to understand. However, Python stores it in tuples. These python tuples are made of nine numbers.

Index	Field	       Domain of Values
0	Year           (4 digits)	Ex.- 1995
1	Month	        1 to 12
2	Day	        1 to 31
3	Hour	        0 to 23
4	Minute	        0 to 59
5	Second	        0 to 61 (60/61 are leap seconds)
6	Day of Week	0 to 6 (Monday to Sunday)
7	Day of Year	1 to 366 (Julian day)
8	DST	        -1,0,1
Leap seconds are added to make up to Earth’s slowing rotation. When DST is 0, it isn’t applied. When it’s 1, it is applied. However, when it is -1, it is up to the library to determine that.

This tuple has an equivalent struct_time structure.'''
print("\n")
print("QUESTION-2")
import datetime
current = datetime.datetime.now()
print(current.strftime("%Y %b %d %H:%M:%S"))
print("\n")
print("QUESTION-3")
import datetime
current = datetime.datetime.now()
print(current.strftime("%b"))
print("\n")
print("QUESTION-4")
import datetime
current = datetime.datetime.now()
print(current.strftime("%d"))
print("\n")
print("QUESTION-4")
import datetime
d=datetime.datetime(2021,1,11)
print(d.day,d.month,d.year)
print("\n")
print("QUESTION-6")
import time
print("Local time is:",time.localtime(time.time()))
print("\n")
print("QUESTION-7")
import math
n=int(input("Enter the number "))
res=math.factorial(n)
print(res)
print("\n")
print("QUESTION-8")
import math
n=int(input("Enter the number "))
m=int(input("Enter the number "))
res=math.gcd(m,n)
print(res)
print("\n")
print("QUESTION-9[a]")
import os 
print(os.getcwd())
print("\n")
print("QUESTION-9[b]")

import os 
print(os.getcwd())
print(os.environ)

print("\n")
