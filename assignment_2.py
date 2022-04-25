#assignment 2 : Fibonacci numbers

# Getting Nth term
nth_term = int(input("How many terms you need :"))

# Initiation of first 2 numbers
x=0
y=1

# Fibonacci Numbers
if nth_term == 0:
    print(x)

elif nth_term == 0:
    print(x)

elif nth_term == 1:
    print(y)

elif nth_term > 2:
    print(x)
    print(y)
    for i in range (2,nth_term):
        z=x+y
        x=y
        y=z
        print(z)

else:
    print("Enter Correct Number")
