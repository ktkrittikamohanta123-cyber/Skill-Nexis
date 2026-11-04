# Assignment 3: Even/Odd and Prime Number Checker
# Check whether a number is even or odd and whether it is prime.

num = int(input("Enter a number: "))

# Check whether the number is even or odd.
if num % 2 == 0:
    print(num, "is an Even number")
else:
    print(num, "is an Odd number")

# Check whether the number is prime.
if num <= 1:
    print(num, "is not a Prime number")
else:
    for i in range(2, num):
        if num % i == 0:
            print(num, "is not a Prime number")
            break
    else:
        print(num, "is a Prime number")
