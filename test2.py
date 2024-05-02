#
# import tkinter as tk
#
# l=""""root = tk.Tk()
#
# # Creating labels with different anchor values
# label_center = tk.Label(root, text="Center", bg="yellow")
# label_north = tk.Label(root, text="North", bg="cyan")
# label_south = tk.Label(root, text="South", bg="magenta")
# label_east = tk.Label(root, text="East", bg="green")
# label_west = tk.Label(root, text="West", bg="orange")
#
# # Packing labels with different anchor values
# label_center.pack(side=tk.BOTTOM,anchor=tk.CENTER,expand=500)
# label_north.pack(side=tk.BOTTOM,anchor=tk.N)
# label_south.pack(side=tk.BOTTOM,anchor=tk.S)
# label_east.pack(side=tk.BOTTOM,anchor=tk.E)
# label_west.pack(side=tk.BOTTOM,anchor=tk.W)
#
# root.mainloop()"""
#
#
# #def cal(n1 ,n2):
# #
# #       for i in n2:
# #           if ord(i) in range(48,58):
# #                 n1=i
# #
# #           elif i == " " :
# # deftxt="Enter your value here"
# # def onclick():
# #      if digit1 == deftxt :
# #          digit1.delete(0,tk.END)
# #          digit1.config(fg="Black")
# #
# # def ofclick():
# #     if digit1 == "":
# #         digit1.insert(0,deftxt)
# # #digit
# #
# #
# #
# #
# #
# #
# #
# #
# #
# # calci=tk.Tk()
# # window_title=calci.title("Calculator.userTANS")
# # background_set=calci.config(bg="#40E0D0")
# #
# # calci.geometry("5000x5000")
# #
# # head1=tk.Label(text="Click enter button after entering your number",bg="pink",fg="#6bb7f0")
# # head1.pack(pady=30)
# #
# #
# #
# #
# # digit1=tk.Entry(fg="grey")
# # digit1.bind("<inFocus>",onclick())
# # digit1.bind("<outFocus>",ofclick())
# # digit1.pack()
# #
# #
# #
# #
# #
# # keypad=[
# #     "1" , "2" , "3",
# #     "4" , "5" , "6",
# #     "7" , "8" , "9",
# #     "+" , "0" , "-",
# #     "/" , "x" , ")",
# #           "(",
# #
# #       ]

# # def butclick(n):
# #     row=1
# #     column=0
# #     for i in keypad:
# #         if column>3:
# #             return
# #
# # #lbl=tk.Label(text=keypad)
# # #lbl.pack(pady=10)
#
#
# but1=tk.Button(text="Enter",bg="#6bb7f0",fg="#ff3333");
# but1.pack(pady=90);


Ms = 8
M = "8 -10"
M = map(int, M.split())
M = set(M)

Ns = 7
N = "5 6 7"
N = map(int, N.split())
N = set(N)

U = M.union(N)
I = N.intersection(M)
SD = U.difference(I)

print("Symmetric Difference:")
for i in SD:
    print(i)