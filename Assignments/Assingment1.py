# Assingment 1.1: WAP to print your name three times
i=0
while i<3:
    print("Ishank Goyal")
    i=i+1
  
#Assingment 2.1: WAP to add three numbers and print the result.
a=3
b=5
c=7
print(a+b+c)

#Assingment 2.2: WAP to concatinate three strings and print the result.

str1="Ishank "
str2="Goyal "
str3="2Q14"
print(str1+str2+str3)

#Assingment 4.1: WAP to print the table of 7, 9.
for i in range(0,11):
    print("7 x",i,"=",7*i,"        9 x",i,"=",9*i)
    
    
#Assingment 4.2: WAP to print the table of n and n is given by user.    
n=input("Enter number to print its table")
n=int(n)
for i in range(0,11):
    print(n,"x",i,"=",n*i)
    
#Assingment 4.3: WAP to add all the numbers from 1 to n and n is given by user.
x=input("Enter number to print sum till there")
x=int(x)
print(x*(x+1)/2)
#or
sum=0
for i in range(1,x+1):
    sum=sum+i
print(sum)

#Assingment 5.1: WAP to find max amoung three numbers and input from user. [Try max() function]

i=6
j=7
k=8
print("max of three numbers is",max(i,j,k))

#Assingment 5.2: WAP to add all numbers divisible by 7 and 9 from 1 to n and n is given by the user.
sum=0
n=int(input("Enter n to find sum of numbers divisible from 1 to n "))
for i in range(1,n+1):
    if(i%7==0 and i%9==0):
        sum=sum+i
        
print("sum of all numbers divisible from 1 to",n,"is",sum)    

#Assingment 5.3: WAP to add all prime numbers from 1 to n and n is given by the user.
n=int(input("Enter n to find sum of prime numbers from 1 to n "))
def primeCheck(num):
    for i in range (2,num):
        if(num%i==0):
            return False
    return True
    
sum=0
for i in range(2,n+1):
    if(primeCheck(i)):
        sum=sum+i
print(sum)

#WAP using function that add all odd numbers from 1 to n, n is given by the user.
def add_odd(n):
    sum=0
    for i in range(1,n+1):
        if(i%2!=0):
            sum=sum+i
    return sum  
  
n=int(input("Enter n to add all odd numbers from 1 to n ")) 
print(add_odd(n))

#WAP using function that add all prime numbers from 1 to n, n given by the user.
n=int(input("Enter n to find sum of prime numbers from 1 to n "))
def primesum(num):
    sum=0
    for i in range(2,n+1):
        if(primeCheck(i)):
          sum=sum+i
    return sum

print(sum)