from tkinter import *

def button_cliked():
    new_text = input.get()
    my_label.config(text=new_text)

window = Tk()
window.title("My first GUI program")
window.minsize(width=500,height=300)
window.config(padx=100,pady=200)

# LABEL

my_label = Label(text="I am a label",font=("Arial",24,"bold"))
my_label["text"] = "new text"
my_label.config(text="new text")
#my_label.pack(side="bottom")
#my_label.place(x=0,y=0)
my_label.grid(column=0,row=0)

# BUTTON

button = Button(text="Click Me",command=button_cliked)
#button.pack()
button.grid(column=1,row=1)

new_botton = Button(text="new button")
new_botton.grid(column=2,row=0)

# ENTRY

input = Entry(width=10)
#input.pack()
input.grid(column=3,row=2)


window.mainloop()