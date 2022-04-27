import tkinter
import tkinter as tk
from tkinter import ttk

r = tk.Tk()
r.geometry("300x160")
r.title('Converter')

label2 = tk.Label(r, text="")
label2.pack()

# Entry box
user_input = tk.DoubleVar()
user_entry = tk.Entry(r, textvariable=user_input, font=('calibre', 10, 'normal'))
user_entry.pack()

label3 = tk.Label(r, text="")
label3.pack()

# Combobox
n = tk.StringVar()
options = ttk.Combobox(r, width=27, textvariable=n)
options['values'] = (' Celsius --> F',
                     ' m/s --> km/hr',
                     ' KB --> GB',
                     ' secs --> mins')
options.pack()
options.current()

label4 = tk.Label(r, text="")
label4.pack()


def Converting():
    if n.get() == ' Celsius --> F':
        ans = ((user_input.get() * 9.0 / 5.0) + 32.0)
        label1 = tk.Label(r, text=ans)
        label1.pack()

    if n.get() == ' m/s --> km/hr':
        ans = (user_input.get() * 3.6)
        label1 = tk.Label(r, text=ans)
        label1.pack()

    if n.get() == ' KB --> GB':
        ans = (user_input.get() / 1024)
        label1 = tk.Label(r, text=ans)
        label1.pack()

    if n.get() == ' secs --> mins':
        ans = (user_input.get() / 60)
        label1 = tk.Label(r, text=ans)
        label1.pack()


btn = tkinter.Button(r, text='Calculate', bd='5', command=Converting)
btn.pack()


r.mainloop()
