#this is the program of sum of number
x=int(input("Enter the number \n"))
sum=0
while x!=0:
    digit=x%10
    sum=sum+digit
    x=x//10
print("The sum of the number is ",sum)
      