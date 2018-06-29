print("QUESTION-1")
try:
  a=3
  if a<4:
    a=a/(a-3)
    print(a)
except ZeroDivisionError as e:
     print("ERROR OCCURED")
     print(e)
print("\n")
print("QUESTION-2")
try:
    l=[1,2,3]
    print(l[3])
except Exception as e:
    print(e)
print("\n")
print("QUESTION-3")
try:
    raise NameError("Hi there")  # Raise Error
except NameError as e:
    print("An exception")
    print(e)
    raise  # To determine whether the exception was raised or not
# An Exception
# Hi there
print("\n")
print("QUESTION-4")
def AbyB(a,b):
	try:
		c = ((a+b) / (a-b))
	except ZeroDivisionError:
		print("a/b result in 0")
	else:
		print(c)

AbyB(2.0, 3.0)#Give result -5
AbyB(3.0, 3.0)#Give exception
print("\n")
print("QUESTION-5")
try :
    from math import gauri
except ImportError as er:
    print("EXCEPTION OCCURED")
    print(er)
    print("\n")
try:
    li = [0,1,3,str]
    print(li[5])
except IndexError as er2:
    print("EXCEPTION OCCURED")
    print(er2)
    print("\n")
try:
    val = int("meenal")
except ValueError as er3:
    print("EXCEPTION OCCURED")
    print(er3)
print("\n")
print("QUESTION-6")
class AgeTooSmallError(Exception):
    "Raised when age is less than 18"

age = 18

while True:
    try:
        ip_age = int(input("enter the age:"))
        if (ip_age<age):
            raise AgeTooSmallError
        break
    except  AgeTooSmallError:
        print("Age must not be less than 18")
        print()
print("It's perfect"
    




