# import tkinter as tk
#
# def on_button_click():
#     label.config(text="Button Clicked!")
#     countdown(5)
# def countdown(n):
#     if n>=0:
#           label2.config(text=f"this window will close in {n} seconds")
#           root.after(1000,lambda:countdown(n-1))
#     else:
#          close
#
# def close():
#     root.destroy()
#
#
# root = tk.Tk()
# root.title("Tkinter in PyCharm")
#
# geo=root.geometry("50000x70000")
#
# label = tk.Label(root, text="Hello, Tkinter!")
# label.pack()
#
# label2=tk.Label(root,text="Hit enter placed on the screen after you have entered your value")
# label2.pack()
#
# button = tk.Button(root, text="Click Me", command=on_button_click)
# button.pack()
#
# root.mainloop()
#
#
#
#
# n=5
# x=0
# for i in range (n):
#    if(x<n):
#        # print("*"*i)
#    else:
#
#      continue

# Ms=8#int(input())
# M="8 -10"#input()
# M=M.split(' ')
# M=map(int,M)
# M=set(M)
#
# Ns=7#int(input())
# N="5 6 7"#input()
# N=N.split(' ')
# N=map(int,N)
# N=set(N)
# U=M.union(N)
# I=N.intersection(M)
# SD=U.difference(I)
# SD=set(SD)
# for i in SD:
#    print(i)





n="4"#input()
a="789"#input()
m="5"#input()
b="666"#input()
a1=""
b1=""

for i in a:
   a1+=i+" "

for i in b:
    b1+=i+" "
print(a1)
A=set(a1.split(' '))
B=set(b.split(' '))
print(A)
#print(A)
c=0
for i in A:
      if(c<7):
        print(i)
        c+=1
       # print(c)
      else:
        print(type(i))














