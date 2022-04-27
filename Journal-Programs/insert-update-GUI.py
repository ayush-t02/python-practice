import tkinter as tk

r = tk.Tk()
r.geometry("300x160")
r.title('Insert - Update')

label4 = tk.Label(r, text="")
label4.pack()
# Entry box
user_input = tk.StringVar()
user_entry = tk.Entry(r, textvariable=user_input, font=('calibre', 10, 'normal'))
user_entry.pack()

# Label
label2 = tk.Label(r, text="Enter a value")
label2.pack()

# Functions
previous = ''
def inserting():
    global previous
    previous = user_input.get()
    if previous != "Enter a value":
        label2.configure(text=user_input.get())

def get_previous():
    return previous

def updating():
    for last in get_previous():
        if user_input.get() != last:
            label2.configure(text=user_input.get())


# Buttons
insert_btn = tk.Button(r, text='Insert', bd='5', command=inserting)
insert_btn.pack()

label3 = tk.Label(r, text="")
label3.pack()

update_btn = tk.Button(r, text='Update', bd='5', command=updating)
update_btn.pack()

r.mainloop()
