st=1
n=int(input("enter"))
for i in range (1,10):
    for j in range (10):
        print("*",end="")
    for k in range (1,2*i):
         print(k,end="")
    for j in range (1,n-i+1) :
       print("*",end="")





# #print("Hello world ")
#
# def  intlen(n):
#         len=0
#         n=str(n)
#
#         for i in n:
#                  len+=1
#         return len
#
# def digit(n,i):
#
#         p=0
#
#         n=str(n)
#         for j in n:
#
#            if (i==p):
#
#                  j=int (j)
#
#                  return  j
#
#            p+=1
#
#         return  "index out of bounds"
#
#
# N = int(input(" enter your number "))
#
# og=N
#
# rev=0
#
# l=intlen(N)
#
# print (")
#
# n1=digit(N,0)
#
# n2=digit(N,l-1)
#
# m=(10**l-1)
#
#
#
# N=(N-(n1*m))+(n2*m)
#
# N=(N-n2)+n1
#
#
# #for i in range(1,l+1):
#
# #        n1=N%10
#
# #        N=N//10
#
# #        rev +=n1*(10**(l-i))
#
#
# print (" original number ",og," revesed number ",rev )

        		

# for i in range(0,5):
#     #for j inn range
#
#      I= str(i+1)
#      st=" "*(5-i)+(I+" ")*(2*i+1)+" "
#      print(st)
