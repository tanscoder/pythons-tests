st=1
n=int(input("enter"))
for i in range (1,10):
    for j in range (10):
        print("*",end="")
    for k in range (1,2*i):
         print(k,end="")
    for j in range (1,n-i+1) :
       print("*",end="")
