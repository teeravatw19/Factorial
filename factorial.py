from tkinter import *

def factorial():
    num = int(number_input.get())

    fac = 1
    if num < 0:
        print("Sorry, factorial does not exist for negative numbers")
    elif num == 0:
        print("The factorial of 0 is 1")
    else:
        for i in range(1,num + 1):
            fac = fac*i
    
    output = ''
    output += (str(num) + "! = " + str(fac))
    output_label.configure(text=output)

window = Tk()
window.title('MyProject')
window.minsize(width=200, height=160)
window.configure(background='#111111')

title_label = Label(master=window, text='Factorial'.upper(), background="#111111", fg="white")
title_label.pack(pady=3)

number_input = Entry(master=window, background="#222222" , fg="white")
number_input.pack(pady=10)

go_button = Button(master=window, text="Calculate", background="#333333", fg="white", command=factorial)
go_button.pack(pady=3)

output_label = Label(master=window, background="#111111", fg="white")
output_label.pack(pady=5)

window.mainloop()