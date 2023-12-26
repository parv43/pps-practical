x=int(input("Enter the year\n"))
if(x%4==0):
    print("yes year is leap year")
elif(x%100==0 and x%400==0):
    print("yes number is leapyear")
else:
    print("sorry number is not leap year")
