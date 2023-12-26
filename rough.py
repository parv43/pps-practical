# patern 1 
for i in range(1,6):
    for j in range(1,i+1):
        print("*",end="")
    print()

# patern 2
for i in range(5,0,-1):
    for j in range(1,i+1):
        print("x",end="")
    print()

# patern 3
for i in range(1,6):
    for k in range(1,6-i):
        print(" ",end="")
    for j in range(1,i+1):
        print("*",end="")
    print()

# pattern 4
for i in range(5,0,-1):
    for k in range(1,6-i):
        print(" ",end="")
    for j in range(1,i+1):
        print("x",end="")
    print()

# pattern 5
for i in range(1,6):
    for k in range(1,6-i):
        print(" ",end="")
    for j in range(1,(2*i-1)+1):
        print("x",end="")
    print()

