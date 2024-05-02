

import tkinter as tk

deftxt="enter your number"




def countdel(n):
       count=n
       if count>=0:
         subhead2.config(text=f"This window close in {count} seconds")
         prog.after(1000,countdel,n-1)
       else:
           prog.destroy()










def funct():
    n = enter.get()
    global n1
    global c
    global value
    c=0
    n1=""
    for i in n:
        if ord(i) in range (48, 58):
            i=int(i)
            l=i+1
            l=str(l)
            n1+=l
            c+=1
            value=True
            continue
        elif ord(i) not in range(48,58):
            subhead.config(text="Please enter your phone number only ie, numerics only",bg="#40E0D0")
            enter.delete(0,tk.END)
            value=False
            break
    mainfct(value)

def mainfct(num):
     if num==True:
       if c==10:
           subhead.config(text=f"{n1}")
           subhead2.config(text="Here is your number. Have fun!")
           #countdel(10)

       elif(c<=10):
           subhead.config(text="Please enter all the numbers")
           prog.after(10000,subhead.config(title="Enter your phone number"))
       else:
           subhead.config(text="please enter up to 10 numbers")
           subhead2.config(text="Yo -_- how many numbers you got in your phone number?-_-",bg="light blue",fg="red")
     elif (num==False):
           subhead2.config(text="click enter After entering your phone number")



def onclick(n):
    if enter.get() == deftxt:
        enter.delete(0, tk.END)
        enter.config(fg="black")


def noclick(n):
    if enter.get() == "":
        enter.insert(0, deftxt)
        enter.config(fg="grey")


prog=tk.Tk()

title=prog.title("Number guessing program")

geos=prog.geometry("500x500")

head=tk.Label(prog,text="Enter your phone number",bg="#40E0D0")
head.pack(pady=70)

subhead=tk.Label(prog,text="Enter main part of the phone number only")
subhead.pack(pady=0)

subhead2=tk.Label(text=" ")
subhead2.pack(pady=0)

enter=tk.Entry(prog,fg="grey")
enter.pack(pady=70)

enter.insert(0,deftxt)

enter.bind("<FocusOut>",noclick)
enter.bind("<FocusIn>",onclick)

buton=tk.Button(text="Enter",command=funct)
buton.pack(pady=50)

prog.mainloop()











