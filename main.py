import tkinter as tk

#function to update the text entry with button clicks
def press(num):
    current = entry_var.get()
    entry_var.set(current + str(num))

#function to evaluate the expression in the entry widget
def equal():
    try:
        result = eval(entry_var.get())
        entry_var.set(result)
    except Exception as e:
        entry_var.set("Error")

#function to clear the entry widget
def clear():
    entry_var.set("")

#setup the main window
root = tk.Tk()
root.title("Simple GUI calculator Application")
root.geometry("400x600")

# string variable to update the entry widget dynamically
entry_var = tk.StringVar()

#entry widget to display the input and output
entry = tk.Entry(root, textvariable=entry_var, font=('Arial', 24), bd=10, insertwidth=2, width=14, borderwidth=4,foreground='maroon')
entry.grid(row=0, column=0, columnspan=4)

#button layout
buttons = [
    ('7',1,0), ('8',1,1), ('9',1,2), ('/',1,3),
    ('4',2,0), ('5',2,1), ('6',2,2), ('*',2,3),
    ('1',3,0), ('2',3,1), ('3',3,2), ('-',3,3),
    ('0',4,0), ('.',4,1), ('+',4,2), ('=',4,3),
    ('C',5,0)
]

#loops to create buttons and place them using grid
for (text, row, col) in buttons:
    if text == '=':
        button = tk.Button(root,text=text, padx=20, pady=20, font =('Arial', 18),command=equal,bg='green').grid(row=row, column=col)
    #clear button at the bottom
    elif text == 'C':
        button = tk.Button(root, text=text, padx=20, pady=20, font=('Arial', 18),command=clear,bg = '#e74c3c',highlightcolor='yellow').grid(row=row, column=col)
    else:
        tk.Button(root, text=text, padx=20, pady=20, font=('Arial', 14),command=lambda t=text:press(t),bg='#3498db').grid(row=row, column=col)


#run the main loop
root.mainloop()


    