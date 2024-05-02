l="""import tkinter as tk

root = tk.Tk()

# Creating labels with different anchor values
label_center = tk.Label(root, text="Center", bg="yellow")
label_north = tk.Label(root, text="North", bg="cyan")
label_south = tk.Label(root, text="South", bg="magenta")
label_east = tk.Label(root, text="East", bg="green")
label_west = tk.Label(root, text="West", bg="orange")

# Packing labels with different anchor values
label_center.pack(side=tk.BOTTOM,anchor=tk.CENTER,expand=True)
label_north.pack(side=tk.BOTTOM,anchor=tk.N)
label_south.pack(side=tk.BOTTOM,anchor=tk.S)
label_east.pack(side=tk.BOTTOM,anchor=tk.E)
label_west.pack(side=tk.BOTTOM,anchor=tk.W)


root.mainloop()"""
import tkinter as tk

deftxt = "enter your number"



def funct():
    n = enter.get()
    global n1
    global c
    c=0
    n1=""
    for i in n:
        if ord(i) in range (48, 58):

            i=str(i)
            n1+=i
            c+=1
            mainfct(n)
            continue
        else:

            subhead.config(text="Please enter your phone number only ie, numerics only:")
            enter.delete(0,tk.END)
            break


k="""def mainfct(num):

       if c==10:
         subhead.config(text="sucessful!")
       else:
           subhead.config(text="Please enter all the numbers")

"""
def mainfct(num):

    global c
    if c == 10:
        subhead.config(text="Successful!")
    else:
        subhead.config(text="Please enter exactly 10 numeric digits")


# ... (rest of your code remains unchanged)


def onclick(n):
    if enter.get()==deftxt:
        enter.delete(0,tk.END)
        enter.config(fg="black")
def noclick(n):
    if enter.get()=="":
        enter.insert(0,deftxt)
        enter.config(fg="grey")



prog=tk.Tk()

title=prog.title("Number guessing program")

geos=prog.geometry("500x500")

head=tk.Label(prog,text="Enter your phone number",bg="#40E0D0")
head.pack(pady=70)


subhead=tk.Label(prog,text="Enter main part of the phone number only")
subhead.pack(pady=10)


enter=tk.Entry(prog,fg="grey")
enter.pack(pady=70)

enter.insert(0,deftxt)
enter.bind("<FocusOut>",noclick)
enter.bind("<FocusIn>",onclick)
buton=tk.Button(text="Enter",command=funct)
buton.pack(pady=50)
prog.mainloop()








