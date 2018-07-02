print("Question1")
n=int(input("Enter the number of lines: "))
with open("1.txt", "r") as text_file:
    contents = text_file.readlines()[-n:]
    for line in contents:
        print(line)
print('*'*10)
print('\n')

print("Question2")
file=open("1.txt","r+")

wordcount={}

for word in file.read().split():
    if word not in wordcount:
        wordcount[word] = 1
    else:
        wordcount[word] += 1

for k,v in wordcount.items():
    print(k, v)
print('*'*10)
print('\n')

print("Question3")
with open('1.txt','r') as ff:
    x=ff.read()
with open('2.txt','w') as zz:
    a=zz.write(x)
print('*'*10)
print('\n')

print("Question4")
with open('3.txt') as fh1, open('4.txt') as fh2:
    for line1, line2 in zip(fh1, fh2):
        print(line1+line2)
print('*'*10)
print('\n')

print("Question5")
data = []
with open('5.txt','r') as myfile:
    for line in myfile:
        data.extend(map(int, line.split(',')))
var=sorted(data)
print(var)
with open('6.txt','w') as myfile2:
    for ele in var:
        myfile2.write(str(ele))
print('*'*10)
