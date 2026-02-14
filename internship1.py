import tkinter as tk
from tkinter import messagebox
def cal_bmi():
    try:
        w=float(weight.get())
        h=float(height.get())
        bmi=round((w/h**2),2)
        if bmi<8.5:
            c="Underweight"
        elif bmi<25:
            c="Normal weight"
        elif bmi<30:
            c="Overweight"
        else:
            c="Obese"
        result_label.config(text=f"BMI: {bmi}\nCategory: {c}")
    except ValueError:
        messagebox.showerror("Input Error","Please enter correct data")
w=tk.Tk()
w.title("BMI Calculator")
w.geometry("300x250")
tk.Label(w,text="Height (m):").pack(pady=5)
height=tk.Entry(w)
height.pack()
tk.Label(w,text="Weight (kg):").pack(pady=5)
weight=tk.Entry(w)
weight.pack()
tk.Button(w,text="Calculate BMI",command=cal_bmi).pack(pady=10)
result_label=tk.Label(w,text="",font=("Calibri",16))
result_label.pack(pady=10)
w.mainloop()
