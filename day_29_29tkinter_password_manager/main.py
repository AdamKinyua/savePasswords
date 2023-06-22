from tkinter import *
from tkinter import messagebox

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
from random import randint, choice, shuffle
import pyperclip  # allows us to copy things to clipboard

json_info = """
JSON is a fancier way and most efficient way of writing and saving data that is easier to search through
json.dump() - writes
json.load() - reads
json.update() - updates 

"""


def password_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    new_password = [choice(letters) for _ in range(randint(8, 10))] + [choice(symbols) for _ in
                                                                       range(randint(2, 4))] + [choice(numbers)
                                                                                                for _ in
                                                                                                range(randint(2, 4))]
    shuffle(new_password)
    password = "".join(new_password)  # new string .join()

    pyperclip.copy(password)
    # pyperclip.paste(password)
    password_entry.insert(0, password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_data():
    is_ok = messagebox.askokcancel(title=website.get(),
                                   message=f"These are the details entered: \nEmail: {email_username_entry.get()}"
                                           f"\nPassword: {password_entry.get()}\n")
    if is_ok:
        if len(email_username_entry.get()) == 0 or len(password_entry.get()) == 0:
            messagebox.showinfo(title="Error", message="Fill all the blank spaces")


        else:
            with open("data.txt", mode="a") as file:
                file.write(f"{website.get()} | {email_username_entry.get()} | {password_entry.get()}\n")
            file.close()
            # Deleting all the content in the entry fields for the next
            website.delete(0, END)
            email_username_entry.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200, highlightthickness=0)
lock_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_image)
canvas.grid(column=1, row=0)

# ---------------Labels---------
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

email_username_label = Label(text="Email/Username:")
email_username_label.grid(column=0, row=2)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

# --------------Entries-------
website = Entry(width=57)
website.grid(row=1, column=1, columnspan=2)
website.focus()  # Putting the cursor in the entry box

email_username_entry = Entry(width=57)
email_username_entry.grid(row=2, column=1, columnspan=2)
email_username_entry.insert(0, "email@email.email")  # Insert this text at the first zeroeth character

password_entry = Entry(width=33)
password_entry.grid(column=1, row=3)

# --------------Buttons-------
generate_password_button = Button(text="Generate Password", width=19, command=password_generator)
generate_password_button.grid(column=2, row=3)

add_button = Button(text="Add", width=48, command=save_data)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
