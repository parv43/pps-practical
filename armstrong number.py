x=int(input("Enter the number\n"))
order=len(str(x))
sum=0
temp=x
if( order==1 and x!=1):
    print("number is not armstrong")
else:
    while(x>0):
        digit=x%10
        sum=sum+digit**order
        x=x//10
    if(temp==sum):
        print("number is armstrong")
    else:
        print("number is not armstrong")
