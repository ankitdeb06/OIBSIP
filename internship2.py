import tkinter as tk
import random
import string
def generate_password():
    l=int(length.get())
    c=string.ascii_letters+string.digits+string.punctuation
    p=""
    for i in range(l):
        p+=random.choice(c)
    result_label.config(text=p)
w=tk.Tk()
w.title("Password Generator")
w.geometry("300x200")
tk.Label(w,text="Password Length:").pack(pady=5)
length=tk.Entry(w)
length.pack()
tk.Button(w,text="Generate Password", command=generate_password).pack(pady=10)
result_label=tk.Label(w,text="",font=("Calibri",16))
result_label.pack(pady=10)
w.mainloop()
