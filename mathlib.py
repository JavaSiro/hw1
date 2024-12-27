q=1
w=2
e=3
r=4
t=5
print(f'{q+w}, {r/w}, {q*w}')
q+=1
print(q)
w-=1
print(w)
e/=1
r*=2

first_number=float(input('type the first number:\n'))
second_number=float(input('now second:\n'))
print(first_number**2*second_number**2)



import math

n = int(input("Enter a non-negative integer: "))

if n < 0:
    print("Factorial is not defined for negative numbers.")
else:
    print(f"The factorial of {n} is {math.factorial(n)}.")

#    GCD
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

gcd = math.gcd(a, b)
print(f"The greatest common divisor of {a} and {b} is {gcd}.")