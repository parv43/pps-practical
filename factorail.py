x=int(input("Enter the number which you want to find the fatorial/n"))
factorial=1
for i in range(1,x+1):
    factorial=factorial*i
print(factorial)
# n = int(input("Enter a number: "))
# factorial = 1
# if n < 0: #Check if the number is negative
#    print("Factors do not exist for negative numbers.")
# elif n == 0: #Check if the number is zero
#    print("The factorial of 0 is 1.")
# else:
#    for i in range(1,n + 1):
#        factorial = factorial*i
#    print("The factorial of",n,"is",factorial)
