#pattern 1
# i=1
# while(i<=5):
#     j=1
#     while(j<=i):
#         print("*",end="")
#         j=j+1
#     print()
#     i=i+1
#pattern 1 by using loop
# for i in range(1,5):
#     for j in range (1,i+1):
#         print("*",end='')
#     print()


# print 2nd pattern using loop
# for i in range(5,0,-1):
#     for j in range(1,i+1):
#         print("*",end='')
#     print()


# print 3rd pattern using loop
# for i in range(1,6):
#     for k in range(1,6-i):
#         print(" ",end="")
#     for j in range(1,i+1):
#         print("*",end="")
#     print()


# print 4th patter sing loop
for i in range(1,6):
    for k in range(1,6-i):
        print(" ",end="")
    for j in range(1,(2*i-1)+1):
        print("*",end='')
    print()