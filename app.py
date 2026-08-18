name = input("Enter name: ")
() == "yes"

print("\n--- Student Details ---")
print("Name:", name)
print("Roll Number:", roll_number)
print("CGPA:", cgpa)
print("Result:", "Pass" if passed else "Fail")
a=int(input())
b=int(input())
print(a+b)
a=float(input("Enter a first number:"))
b=float(input("enter a second number:"))
print(a+b)
print(a-b)
print(a*b)
print(a/b)

print(a==b)
print(a!=b)
print(a>b)
print(a<b)
num =int(input("Enter a number:"))
print(num % 2 == 0)



marks = 80

if marks >= 90:
    print("Grade: A")
elif marks >= 80:
    print("Grade: B")
elif marks >= 70:
    print("Grade: C")
elif marks >= 60:
    print("Grade: D")
elif marks >= 50:
    print("Grade: E")
elif marks >= 40:
    print("Grade: F")
else:
    print("Fail")





for i in range(1, 11):
    print("Number:", i)
    print("Square:", i * i)
    print("Cube:", i * i * i)
    print("done")



    count = 1
while count <= 5:
    print(count)
    count += 1


    


for i in range(1, 6):
    for j in range(i):
        print("*", end="")
        print()



def greet(name):
 print("Hello, " + name + "!Welcome to the program.")
