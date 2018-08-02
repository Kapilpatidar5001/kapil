1.
name=input("enter name")
print("Hello " +name)

2.
n1=input("enter first number")
n2=input("enter second number")
x=int(n1)+int(n2)
if x >= 0:
    print("positive")
else:
    print("negative")

3.
n=5
while True:
    x=int(input("enter number"))
    if x == n:
        print("correct")
        break
    else:
        continue


4.
firstname=input("enter first name")
lastname=input("enter last name")
wholename=firstname+" "+lastname
print(wholename)

5.
str=input("enter string")
print(str.swapcase())

6
a=[1,2,3,4,5]
s=0
m=1
for i in a:
    s=s+i
    m=m*i
print(s)
print('\n')
print(m)

7.
x=[12,23,"abs","ads",6]
print(x)
y=input("enter a value")
print(y)
z=x.index(y)
print(z)
if z >= 0 & z <= 4:
    print("true")
else:
    print("false")

8.
l1=(input("enter list 1 seperated by comma")).split(',')
l2=(input("enter list 2 seperated by comma")).split(',')
flag=0
for i in l1:
    for j in l2:
        if i==j:
            flag=1
            print("true")
            break
        else:
            continue
        
if flag==0:
    print("false")

9.
st=input().split()
k="*"
for i in range(0,len(st)):
    print(k*int(st[i]))
    """j=1
    while j <= i:
        print("*",end='')
        j=j+1"""
print(k*st[i])
    
    
