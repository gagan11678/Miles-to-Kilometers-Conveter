from tkinter import *

window = Tk()


input_box = Entry()
input_box.grid(row=0, column=1)

label1 = Label(text="Miles")
label1.grid(row=0, column=2)

label2 = Label(text="Equals to")
label2.grid(row=1, column=0)

label3 = Label(text="KM")
label3.grid(row=1, column=2)

ans_label = Label(text='0')
ans_label.grid(row=1, column=1)


def calculate():
    miles = int(input_box.get())
    ans = round((miles * 1.609344), 2)
    ans_label.config(text=ans)


button = Button(text='Calculate', command=calculate)
button.grid(row=2, column=1)

window.mainloop()
