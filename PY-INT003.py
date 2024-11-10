from currency_converter import CurrencyConverter
import tkinter as tk

a = CurrencyConverter()

window = tk.Tk()
window.geometry("1000x500")
window.configure(bg="lightgreen")

def clicked():
    try:
        amount = float(e1.get())
        cur1 = e2.get().upper()
        cur2 = e3.get().upper()
        
        data = a.convert(amount, cur1, cur2)
        
        l5.config(text=f"Converted Amount: {data:.2f} {cur2}")
    except Exception as e:
        l5.config(text="Error: Please check input values.")

l1 = tk.Label(window, text="Currency Converter", font="Times 20 bold", bg="lightyellow")
l1.place(x=150, y=35)
l2 = tk.Label(window, text="Enter Amount:", font="Times 18", bg="lightyellow")
l2.place(x=50, y=80)
e1 = tk.Entry(window)
e1.place(x=300, y=90)
l3 = tk.Label(window, text="Enter Currency :", font="Times 18", bg="lightyellow")
l3.place(x=50, y=130)
e2 = tk.Entry(window)
e2.place(x=300, y=140)

l4 = tk.Label(window, text="Enter Target Currency:", font="Times 18", bg="lightyellow")
l4.place(x=50, y=180)
e3 = tk.Entry(window)
e3.place(x=300, y=190)

b1 = tk.Button(window, text="Convert", command=clicked )
b1.place(x=280, y=240)

l5 = tk.Label(window, text="", font="Times 18")
l5.place(x=280, y=290)

window.mainloop()
