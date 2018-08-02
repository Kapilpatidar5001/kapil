#1.
#def generate_n_char(n,c):
#     for i in range(1,n+1):
#        print(c,end='')
#generate_n_char(5,"x")
    
#2.
'''
def max_in_list(l):
    max=0
    for i in l:
        x=int(i)
        if x > max:
            max=x
    print(max)
l=(input("enter list seperate element by comma:")).split(',')
max_in_list(l)
'''

#3.
'''
w=(input("enter list of words")).split(',')
l=[]
for i in w:
    l.append(len(i))
print(l)
  '''
#4.
'''
def max_in_list(l):
    max=0
    for i in l:
        x=int(i)
        if x > max:
            max=x
    print(max)

w=(input("enter list of words")).split(',')
l=[]
for i in w:
    l.append(len(i))
max_in_list(l)
'''

#5.
'''
w=(input("enter list of words")).split(',')
n=int(input("enter number"))
f=[]
def filter_long_words(l,n):
    for i in l:
        if len(i) > n:
            f.append(i)
    print(f)
filter_long_words(w,n)
'''
#6.

#def reverse(string):
#    return ''.join(reversed(string))
#punctuations = '''!()-[] {};:'"\,<>./?@#$%^&*_~'''
#my_str = input("Enter a string: ")
'''
my_str = "Hello!!!, he said ---and went."
no_punct = ""
for char in my_str:
   if char not in punctuations:
       no_punct = no_punct + char
print(no_punct)

if reverse(no_punct) == no_punct:
    print("True")
else:
    print("False")
'''
#7.
'''
def pangram():
    a=input("enter string")
    alpha="abcdefghijklmnopqrstuvwxyz"
    pl=""
    c=0
    for ch in a:
        for l in alpha:
            if ch==l and ch not in pl:
                pl=pl+ch
    for ch in pl:
        for l in alpha:
            if ch==l:
                c=c+1
    if c==26:
        print("true")
    else:
        print("false")
pangram()
'''

#8.
'''
dict={"merry":"god","chrimas":"jul","and":"och","happy":"gott","new":"nytt","year":"ar"}
print(dict["chrimas"])

def translate(e):
    s=[]
    for i in e:
        s.append(dict.get(i))
    print(s)
x=(input("enter list")).split(",")
translate(x)
'''
#9.
'''
l=list(input("enter string"))
print(l)
d={}
for i in l:
    if i in d.keys():
        d[i]=d[i]+1
    else:
        d[i]=1
print(d)
'''    
#14.
'''
import math
print(dir(math))
import numpy
print(dir(numpy))
'''
#13.
'''
f=open("emps.txt",'r')
data=f.read()
f.close()

x=data.split(',')
id=x[0]
name=x[1]
salary=x[2]
w=open("write.txt",'w')
print("id:{0} name:{1} salary:{2}".format(id,name,salary))
w.write(str(id)+","+str(name)+","+str(salary))
w.close()
'''
#12.
'''
class date:
    import datetime
    DT=datetime.datetime.now()
    def __init__(self):
        self.y=date.DT.year
        pass
    def displayTime(self):
        print("time-{0}:{1}:{2}".format(date.DT.hour,date.DT.minute,date.DT.second))
    def displayDate(self):
        print("date-{0}/{1}/{2}".format(date.DT.day,date.DT.month,date.DT.year))

class usedte:
    def __init__(self):
        d=date()
        d.displayTime()
        d.displayDate()
    
usedte()
'''
#10.
'''
##mathematics
def maximum(a):
    return max(a)

def maximum(l):
    max=0
    for i in l:
        x=int(i)
        if x > max:
            max=x
    return(max)

def maximum(l):
    return max(l)

#print(maximum([12,67,1,8]))


def add(x,y):
    z=[]
    for i,j in zip(x, y):
        z.append(int(i)+int(j))
    return z
def sub(x,y):
    z=[]
    for i,j in zip(x, y):
        z.append(int(i)-int(j))
    return z
def sort(x):
    x.sort()
    return x

###usemath.py
import mathematics
a = [int(x) for x in input("enter string").split(',')]
#b = [int(x) for x in input("enter string").split(',')]
def displaymax(x):
    print(mathematics.maximum(x))

def displayadd(a,b):
    print(mathematics.add(a,b))

def displaysort(a):
    print(mathematics.sort(a))
displaymax(a)

'''
#11.
#mathuse.py
'''
import pkg.mathematics.*
a = [int(x) for x in input("enter string").split(',')]
#b = [int(x) for x in input("enter string").split(',')]
def displaymax(x):
    print(maximum(x))

def displayadd(a,b):
    print(add(a,b))

def displaysort(a):
    print(sort(a))
displaymax(a)

#mathematics

def maximum(a):
    return max(a)

def maximum(l):
    max=0
    for i in l:
        x=int(i)
        if x > max:
            max=x
    return(max)

def maximum(l):
    return max(l)

#print(maximum([12,67,1,8]))


def add(x,y):
    z=[]
    for i,j in zip(x, y):
        z.append(int(i)+int(j))
    return z
def sub(x,y):
    z=[]
    for i,j in zip(x, y):
        z.append(int(i)-int(j))
    return z
def sort(x):
    x.sort()
    return x
'''
