# QUESTION 01

# Swap Two Numbers

# METHOD 1

num1 = 10
num2 = 20

print("Value of num1 before swipping",num1)
print("Value of num2 before swipping",num2)

temp = num1
num1 = num2                                                 # Swap Two Numbers
num2 = temp

print("Value of num1 after swipping",num1)
print("Value of num2 after swipping",num2)

# METHOD 2

num1 = int(input("Enter value for num1: "))
num2 = int(input("Enter value for num2: "))

temp = num1
num1 = num2
num2 = temp

print("Value of num1 after swipping",num1)
print("Value of num2 after swipping",num2)

#METHOD 3

# num1 = 10
# num2 = 20

print("Value of num1 before swipping",num1)
print("Value of num2 before swipping",num2)

num1,num2 = num2,num1

print("Value of num1 after swipping",num1)
print("Value of num2 after swipping",num2)


# QUESTION 02

# Check Number Is Prime Or Not

# METHOD 1

prime_num = 3
count = 0

if prime_num>1:
    for i in range(1,prime_num+1):                      # Condition to check number is prime or not
        if prime_num % i == 0:
            count += 1
    
    if count == 2:
        print("Number is a Prime Number")

    else:
        print("Number is not a prime number")

else:
    print("Number is not a prime number")


# METHOD 2
    
prime_num = int(input("Enter a number: "))
count = 0

if prime_num>1:
    for i in range(1,prime_num+1):
        if prime_num % i == 0:
            count += 1
    
    if count == 2:
        print("Number is a Prime Number")

    else:
        print("Number is not a prime number")

else:
    print("Number is not a prime number")


# QUESTION 03

# Find the factorial of the given number

# METHOD 1

num = 5
factorial = 1

if num<0:
    print("Factorial does not exit")


elif num == 0 or num == 1:
    print(f"Factorial of {num} is 1")

else:
    for i in range(1,num+1):
        factorial *= i

    print(f"factorial of {num} is {factorial}.")


#METHOD 2
    
def factorial(num):
    if num < 0:
        return f"Factorial of {num} does not exit"
    
    elif num == 0 or num ==1:
        return 1

    else:
        return (num)*factorial(num - 1)
    
num = int(input('Enter value: '))
print(factorial(num))


# QUESTION 04

# Fiboannci Series

num = int(input("Enter value: "))
n1 , n2 = 0 , 1
sum = 0

if num <= 0:
    print("Enter number greater than 0")

else:

    for i in range(0,num):
        print(sum)
        n1 = n2
        n2 = sum
        sum = n1 + n2


# QUESTION 05

# Find Sum of Elements in a list

# METHOD 1

L = [1,2,3,4,5]
print(sum(L))

# METHOD 2

L = [1,2,3,4,5]
count = 0
for i in L:                                              # Sum of all element in a list
    count +=i

print(count)

# METHOD 3

L = input("Enter values: ")
L = L.split()
temp = []
for i in L:
    a = int(i)
    temp.append(a)

print(sum(temp))


# METHOD 4

L = input("Enter value: ")
L = L.split()

temp = [int(i) for i in L]
print(sum(temp))


# QUESTION 06

# Find Maximum and Minimum value in a List

# METHOD 1

L = [10,50,30,20]
L.sort()

print("Maximum Value in a list is",L[-1])
print("Minimum Value in a list is",L[0])

# METHOD 2

L = [10,50,70,20]
print("Maximum Value in a list is",max(L))
print("Minimum Value in a list is",min(L))

# METHOD 3

L = input("Enter values: ")
L = L.split()

temp = [int(i) for i in L]
temp.sort()

print("Maximum Value in a list is",L[-1])
print("Minimum Value in a list is",L[0])


# QUESTION 07

# Find length of a list

# METHOD 1

L = [10,20,30,40,50]
print("The length of the list is",len(L))


# METHOD 2

L = [10,20,30,40,60]
count = 0

for i in L:
    count +=1

print("The length of the list is",count)


# QUESTION 08

# Swap First and Last Element in a List

# METHOD 1

L = [10,30,60,20,50]
L[0],L[-1] = L[-1],L[0]
print(L)

# METHOD 2

L = [10,30,20,60,50]
first = L.pop(0)
last = L.pop(-1)

L.insert(0,last)
L.append(first)

print(L)


# QUESTION 09

# Swap Any Two elements in a List

L = [50,60,20,10,90]
L[0],L[2] = L[2],L[0]

print(L)


# QUESTION 10

# METHOD 1

# Remove Nth Occurrence of the given word

my_list = ["Geeks","for","Geeks"]
unique_list = list(set(my_list))
unique_list.reverse
print(unique_list)
        

# METHOD 2 

my_list = ["Geeks","for","Geeks"]
temp = []

for i in my_list:
    if i not in temp:
        temp.append(i)

print(temp)


# QUESTION 11

# Check the value is in list or not

my_list = [1,6,3,5,3,4]

if 4 in my_list:
    print("Element found")

else:
    print('Element not found')


# QUESTION 12

# How to Clear a List

# METHOD 1

my_list = [1,2,5,7,8]
my_list.clear()
print(my_list)


# METHOD 2

my_list = [1,2,5,7,8]
temp = []

for i in my_list:
    if i in temp:
        temp.append(i)

print(temp)


# QUESTION 13

# How to Reverse a List

# METHOD 1

my_list = [1,2,5,7,8]
(my_list.reverse())
print(my_list)


# METHOD 2

my_list = [1,2,5,7,8]
my_list = my_list[::-1]
print(my_list)


# QUESTION 14

# How to copy a list

# METHOD 1

my_list = [1,2,5,7,8]
my_list_copy = my_list[:]

print(my_list_copy)


# METHOD 2

my_list = [1,2,5,7,8]
my_list_copy = []
my_list_copy.extend(my_list)

print(my_list_copy)


# METHOD 3

my_list = [1,2,5,7,8]
my_list_copy = list(my_list)

print(my_list_copy)


# METHOD 4

my_list = [1,2,5,7,8]
my_list_copy = my_list.copy()

print(my_list_copy)


# QUESTION 15

# Count Occurrences of an element in a list

my_list = [10,20,80,20,20,10,50]

temp = {}

for i in my_list:
    if i not in temp:
        temp[i] = 1
    else:
        temp[i] += 1


for key,value in temp.items():
    if value > 1:
        print(f"{key} appears {value} times")


# QUESTION 16

# Multiply all the numbers in a list

# METHOD 1

L = [3,2,4]
count = 1

for i in L:
    count *= i

print(count)


# QUESTIONSS 17

# Find 2nd Largest Number in a List

L = [60,70,11,20,90]
L.sort()
print(L[-2])


# QUESTION 18

# Check if word is palindrome or not

palindrome = input("Enter a word: ")

if palindrome == palindrome[::-1]:
    print("Word is Palindrome")

else:
    print("Word is not a Palindrome")


# QUESTION 19

# Reverse Words in a String

# METHOD 1

str = input("Enter sentence: ")
str = str.split()

str.reverse()

output = " ".join(str)

print(output)


# METHOD 2

str = input("Enter sentence: ")
str = str.split()

str = str[::-1]

output = " ".join(str)

print(output)


# QUESTION 20

# Substring Presence in Given String

# METHOD 1

str = "Welcome to Python Programming"
temp = "Python"

if str.find(temp)==-1:
    print("Not Found")
   
else:
    print("Found")


# METHOD 2
    
str = "Welcome to Python Programming"

if "Python" in str:
    print("Found")

else:
    print("Not Found")


# QUESTION 21

# Check length of the string

# METHOD 1

str = "Python"
print(len(str))


# METHOD 2

str = "Python"
count = 0

for i in str:
    count +=1

print(count)


# QUESTION 22

# Check string contains Special Characters 

str = "welcome"

if str.isalpha():
    print("No Special Character found")

else:
    print("Special Character Found")
        

