x=int(input("Enter the number:"))
if(x==0):
  print("neither prime nor composite")
elif(x%2==0 or x%3==0):
  print("this is not a prime number")
else:
  for i in range(2,x):
    if(x%i !=0):
      print("this number is prime number")
      break