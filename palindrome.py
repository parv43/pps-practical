x=int(input("Enter the number\n"))
p=x
rev=0
while(x>0):
    rev=(rev*10)+x%10
    x=x//10
if(p==rev):
    print("number is palindrome")
else:
    print("number is not palindrome")