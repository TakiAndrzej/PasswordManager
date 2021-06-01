from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
import json
# ---------------------------- LOOK FOR PASSWORD ------------------------------- #
def searching():
    if website_entry.get() == '':
        messagebox.showinfo(title="Oops", message="You didn't enter enough data to save!")
    else:
        try:
            try:
                with open("passwords.json", "r") as file:
                    data = json.load(file)
            except:
                messagebox.showerror(title="ERROR", message="You didn't save any passwords yet!")
        except FileNotFoundError:
            messagebox.showerror(title="ERROR", message="You didn't save any passwords yet!")
        else:
            if website_entry.get() in data:
                messagebox.showinfo(title=f"{website_entry.get()} info",
                                    message=f"E-mail: {data[website_entry.get()]['email']}\n"
                                            f"Password: {data[website_entry.get()]['password']}")
            else:
                messagebox.showerror(title="ERROR", message="No data for this website in database")

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers


    shuffle(password_list)

    password = "".join(password_list)

    password_entry.delete(0, END)
    password_entry.insert(0, password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_password():

    new_data = {
        website_entry.get(): {
            "email": email_entry.get(),
            "password": password_entry.get(),
        }
    }

    if website_entry.get() == '' or password_entry.get() == '':
        messagebox.showinfo(title="Oops", message="You didn't enter enough data to save!")
    else:
        try:
            try:
                with open("passwords.json", "r") as file:
                    data = json.load(file)
            except:
                data = {}
        except FileNotFoundError:
            with open("passwords.json", "w") as file:
                json.dump(new_data, file, indent=4)
        else:
            data.update(new_data)

            with open("passwords.json", "w") as file:
                json.dump(data, file, indent=4)
        finally:
            password_entry.delete(0, END)
            website_entry.delete(0, END)
            website_entry.focus()

# ---------------------------- UI SETUP ------------------------------- #


if __name__ == "__main__":

    window = Tk()
    window.title("Password Manager")
    window.config(padx=50, pady=50)

    # Canvases

    canvas = Canvas(height=200, width=200)
    photo = PhotoImage(file="logo.png")
    canvas.create_image(100, 100, image=photo)
    canvas.grid(column=1, row=0)

    # Labels

    website_label = Label(text="Website:")
    website_label.grid(column=0, row=1)

    email_label = Label(text="Email/Username:")
    email_label.grid(column=0, row=2)

    password_label = Label(text="Password:")
    password_label.grid(column=0, row=3)

    # Buttons

    generate_button = Button(text="Generate Password", width=21,  command=generate_password)
    generate_button.grid(column=2, row=3)

    add_button = Button(text="Add", width=40, command=save_password)
    add_button.grid(column=1, row=4, columnspan=2)

    search_button = Button(text="Search", width=21, command=searching)
    search_button.grid(column=2, row=1)

    # Entries
    website_entry = Entry(width=21)
    website_entry.grid(column=1, row=1)
    website_entry.focus()

    email_entry = Entry(width=47)
    email_entry.grid(column=1, row=2, columnspan=2)
    email_entry.insert(0, "norbert-zuber@wp.pl")

    password_entry = Entry(width=21)
    password_entry.grid(column=1, row=3)



    window.mainloop()