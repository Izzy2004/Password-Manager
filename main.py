from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_numbers + password_symbols + password_letters
    shuffle(password_list)

    password = "".join(password_list)
    password_input.insert(0,password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = website_input.get()
    email = email_input.get()
    password = password_input.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Error", message="Please make sure all fields have been filled in!")

    else:
        try:
            with open('data.json', 'r') as f:
                data = json.load(f)

        except FileNotFoundError:
            with open('data.json', 'w') as f:
                json.dump(new_data, f, indent = 4)

        else:
            data.update(new_data)

            with open('data.json','w') as f:
                json.dump(data, f, indent=4)

        finally:
                website_input.delete(0, END)
                password_input.delete(0, END)


def find_password():
        website = website_input.get()
        try:
            with open('data.json','r') as f:
                data = json.load(f)
        except FileNotFoundError:
            messagebox.showinfo(title='Oops', message='No Data File Found')
        else:
            try:
                email = data[website]["email"]
                password = data[website]["password"]
            except KeyError:
                messagebox.showinfo(title='Oops',message="No details for the website exist")
            else:
                messagebox.showinfo(title=website,message=f'Email: {email}\nPassword: {password}')
        finally:
            website_input.delete(0,END)



# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.config(padx=50,pady=50)


canvas = Canvas(height=200,width=200)
lock_img = PhotoImage(file='logo.png')
canvas.create_image(100,100,image=lock_img)
canvas.grid(column=1,row=0)

website_label = Label(text='Website:')
website_label.grid(column=0,row=1)
email_label = Label(text='Email/Username:')
email_label.grid(column=0,row=2)
password_label = Label(text='Password:')
password_label.grid(column=0,row=3)

website_input = Entry(width=21)
website_input.grid(column=1,row=1)
email_input = Entry(width=38)
email_input.grid(column=1,row=2,columnspan=2)
email_input.insert(0,'arnoldaisaac@icloud.com')
password_input = Entry(width=21)
password_input.grid(column=1,row=3)

generate_button = Button(text='Generate Password', command=password_generator)
generate_button.grid(column=2,row=3)
add_button = Button(text='Add',width=36, command=save_password)
add_button.grid(column=1,row=4, columnspan=2)
search_button = Button(text='Search',width=13, command=find_password)
search_button.grid(column=2,row=1)



window.mainloop()