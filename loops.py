#DAY 1 & DAY 2

# Task 1
print("1)Numbers 1 to 100")
for i in range(1, 101):
    print(i)

# Task 2
print("\n2)Even Numbers")
for i in range(2, 51, 2):
    print(i)

# Task 3
print("\n3)Students")
students = ["Rahul", "Aman", "Priya", "Neha"]

for student in students:
    print(student)

# Task 4
print("\n4)Vowel Count")
text = "Generative AI"

count = 0
for char in text:
    if char.lower() in "aeiou":
        count += 1

print("Total vowels:", count)

# Task 5
print("\n5)Multiplication Table")

number = 5

for i in range(1, 11):
    print(f"{number} x {i} = {number * i}") # f-string





#DAY 2
#Task 1
#list1 = list(map(int, input("Enter numbers separated by spaces: ").split()))  #if you want list from the user
list1 = [23,45,91,16,52,88]

largest = list1[0]

for i in list1:
    if i > largest:
        largest = i

print("Largest is:", largest)

#Task 2 (using for loop)
num = int(input("enter a number:"))
fact = 1
for i in range(1,num+1):
    fact = fact * i
print("Factorial =",fact)

#using function:
def factorial(n):
    result = 1

    for i in range(1, n + 1):
        result *= i

    return result

num = int(input("Enter a number: "))
print("Factorial =", factorial(num))

#Task 3 
def count(para):
    words= para.split()
    return len(words)
text = input("enter a para:")
print("word count is:",count(text))

# Task 4
a= int(input("enter a number:"))
for i in range(1,a+1):
    for j in range(i):
        print("*",end=" ")
    print()

# Task 5
while True: # to keep displaying the menu until the user chooses Exit
    print("1) Addition")
    print("2) Subtraction")
    print("3) Multiplication")
    print("4) Division")

    choice = input("choose an option:")

    if choice == "5":
        break

    a=int(input("enter first number:"))
    b=int(input("enter second number:"))

    if choice == "1":
        print("result is:",a+b)

    if choice == "2":
        print("result is:",a-b)

    if choice == "3":
        print("result is:",a*b)

    if choice == "4":
        print("result is:",a/b)




