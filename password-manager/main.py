from tkinter import * #class,constant
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    entry_password.insert(0,password)
    pyperclip.copy(password) #copy password on keyboard

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = entry_website.get()
    email = entry_email.get()
    password = entry_password.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops",message="Please make sure you haven't left any fields empty.") 
    else:
        is_ok = messagebox.askokcancel(title=website,message=f"These are the details entered: \nEmail: {email}" 
                                                    f"\nPassword: {password} \nIs it ok to save?")
        if is_ok:
            with open("data.txt","a") as data_file: #append mode
                data_file.write(f"{website} | {email} | {password}\n")
                entry_website.delete(0,END)
                entry_password.delete(0,END)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50,pady=50)

canvas = Canvas(width=200,height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100,100,image=logo_img)
canvas.grid(column=1,row=0)

label_website = Label(text="Website:")
label_website.grid(column=0,row=1)
label_email = Label(text="Email/Username:")
label_email.grid(column=0,row=2)
label_password = Label(text="Password:")
label_password.grid(column=0,row=3)

entry_website = Entry(width=52)
entry_website.grid(row=1,column=1,columnspan=2)
entry_website.focus() #for cursor
entry_email = Entry(width=52)
entry_email.grid(row=2,column=1,columnspan=2)
entry_email.insert(0, "aslaydn0@gmail.com") #default value
entry_password = Entry(width=33)
entry_password.grid(row=3,column=1)

generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(row=3,column=2)
add_button = Button(text="Add",width=44, command=save)
add_button.grid(row=4,column=1, columnspan=2)

window.mainloop()