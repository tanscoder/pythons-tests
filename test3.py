t="""
import tkinter as tk

def bt1com():
    n = int(entr.get())
    subhead.config(text=n * 50)
    countdes()

def countdown(c):
      if c>=0:
          subhead2.config(text=f"This window closes in {c}seconds")
          win.after(1000,countdown,c-1)

      else:
          countdes()

def countdes():
    win.destroy()


def des():
    win.destroy()

win = tk.Tk()

win_width=win.winfo_screenwidth()

win_height=win.winfo_screenheight()


print(win_width,win_height)
win.title("Tkinter sample project")
win.geometry("500x350")#{win_height} {win_width}

subhead = tk.Label(text="Enter your number")
subhead.pack(pady=10)

subhead2=tk.Label(text=("Press enter on the screen after entering an integer"))
subhead2.pack()



button = tk.Button(text="Enter", command=bt1com)
button.pack(pady=20)#,side=tk.TOP,anchor=tk.CENTER,expand=True)


entr = tk.Entry()
entr.pack(pady=30)#anchor=tk.CENTER)

win.mainloop()

"""






comment="""import tkinter as tk


def BUTTON():
    #n=int(n)
    n=int(entr.get())
    heading.config(text=n*50)
    countdown(5)

def countdown(n):
    if n>=0:
        l.config(text=f"This window will close in {n} seconds")
        win.after(1000,countdown(n-1))

    else:
        des()


def des():
    win.destroy()

#bt2=tk.Button(text="Enter",command=fcn(n))

win = tk.Tk()


win.title("Test.tans")

win.geometry("500x350")

heading = tk.Label(win,text="Welcome to Tkinter test")
heading.pack(pady=10)

l = tk.Label(win,text="")
l.pack(pady=20)
button = tk.Button(win,text="Test Button",command=BUTTON)
button.pack(pady=20)

entr=tk.Entry()
entr.pack(pady=20)     #side=tk.BOTTOM

win.mainloop()"""





code2="""import tkinter as tk

def on_entry_click(event):
    if entry.get() == default_text:
        entry.delete(0, tk.END)
        entry.config(fg='black')

def on_focus_out(event):
    if entry.get() == "":
        entry.insert(0, default_text)
        entry.config(fg='grey')

root = tk.Tk()
root.title("Entry with Label")

default_text = "Enter your text here"

# Label
label = tk.Label(root, text="Your Label:")
label.pack(pady=5)

# Entry with default label text
entry = tk.Entry(root, fg='grey')
entry.insert(0, default_text)
entry.bind("<FocusIn>", on_entry_click)
entry.bind("<FocusOut>", on_focus_out)
entry.pack(pady=10)

root.mainloop()
"""





import tkinter as tk

deftxt=("Enter your value")


def BUTTON():
    #n=int(n)
    n=int(entr.get())
    #
    l.config(text=l)
    heading.config(text=f"Your answer is = {n * 50}",bg="#40E0D0")
    countdown(60)

def countdown(n):
    if n>=0:
        l.config(text=f"This window will close in {n} seconds")
        win.after(1000,lambda :countdown(n-1))

    else:

        des()

def des():
    win.destroy()

def onclick(event):

  if entr.get()==deftxt:
    entr.delete(0,tk.END)
    entr.config(fg="black")





def notclick(event):
  if entr.get()=="":

    entr.insert(0,deftxt)
    entr.config(fg="grey")



win = tk.Tk()                                                                                                                 # "Window defining"



win.title("Tinkter.window")
win.geometry("500x350")

heading = tk.Label(win,text="Welcome to Tkinter test",fg="black",bg="#40E0D9")           #   #40E0D0 Is the hex for turqouise

heading.pack(pady=10)
                                                                                         #   #       Is the hex for turquoise
l = tk.Label(win,text="helo there!")

l.pack(pady=10)

button = tk.Button(win,text="Click here",command=BUTTON,bg="black",fg="light blue",font=("Times Roman",13))

button.pack(pady=20)

entr=tk.Entry(win,fg="grey")

entr.pack(pady=20)

commented2="""entr2=tk.Entry()
entr2.pack()"""


entr.insert(0,deftxt)
entr.bind("<FocusIn>",onclick)
entr.bind("<FocusOut>",notclick)














