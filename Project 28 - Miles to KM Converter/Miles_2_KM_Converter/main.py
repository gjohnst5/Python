from tkinter import *


def calc():
    miles = float(user_input.get())
    answer = round(int(miles) * 1.61, 2)
    answer_label.config(text=answer)


window = Tk()
window.title("Mile to Km Converter")
window.config(padx=20, pady=20)

user_input = Entry(width=7)
user_input.grid(row=0, column=1)

miles_label = Label(text="Miles")
miles_label.grid(row=0, column=2)

equal_label = Label(text="is equal to")
equal_label.grid(row=1, column=0)

answer_label = Label(text="0")
answer_label.grid(row=1, column=1)

kilo_label = Label(text="Km")
kilo_label.grid(row=1, column=2)

calculate = Button(text="Calculate", command=calc)
calculate.grid(row=2, column=1)

window.mainloop()
