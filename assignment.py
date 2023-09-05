#Calculation of X+7=20
#To solve for X, subtract 7 from each side of the equation

X = 20-7
input("The value of X in the equation is :")
print(X)

#OR

print(f"The value of X is:  {X}")

#Calulating quadratic equation

#Given coefficient
a = 1
b = -1
c = -6
#Calculate the discriminant

D = b**2 - 4*a*c

#Calculate both potential roots
x1 = (-b + D**0.5) / (2*a)
x2 = (-b + D**0.5) / (2*a)

print(f"The roots of the equation are: {x1} and {x2}")

#Fibonacci calculation

# a, b = 0, 1

# print(a)
# print(b)

# for _ in range (7):
# a, b = b, a + b
# print(b)

# a,b, _ =[0,1 b-10]

#Arithmetic operations function. Such as addition, subtraction, multiplication, and division

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    try:
        result = x / y
        return result
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."

print(add(5, 3))       
print(subtract(5, 3))  
print(multiply(5, 3)) 
print(divide(5, 3))   
print(divide(5, 0))    

#Factorization
def factorial(n):
    if n == 0:
        return 1
    else:
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result


print(factorial(0))  
print(factorial(1))  
print(factorial(5)) 
