import tkinter as tk
import requests
def get_weather():
    c=city.get()
    api="a3d73cb4926e48f281993243251207"
    url=f"http://api.weatherapi.com/v1/current.json?key={api}&q={c}"
    d=requests.get(url).json()
    if "error" not in d:
        t=d["current"]["temp_c"]
        condition=d["current"]["condition"]["text"]
        result_label.config(text=f"Temperature: {t} °C\nCondition: {condition}")
    else:
        result_label.config(text="City mot found")
w=tk.Tk()
w.title("Weather App")
w.geometry("300x220")
tk.Label(w,text="Enter City Name:").pack(pady=5)
city=tk.Entry(w)
city.pack()
tk.Button(w,text="Get Weather",command=get_weather).pack(pady=10)
result_label=tk.Label(w,text="",font=("Calibri",16))
result_label.pack(pady=10)
w.mainloop()
