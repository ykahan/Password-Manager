from tkinter import *
from tkinter import messagebox
from random import randint

WINDOW_HEIGHT = 200
WINDOW_WIDTH = 200


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def create_random_password():
    password = generate_password()
    insert_password(password)
    process_clipboard(password)


def process_clipboard(password):
    window.clipboard_clear()
    window.clipboard_append(password)


def generate_password():
    characters = get_characters()
    password = ""
    for num in range(0, 50):
        char = randint(0, len(characters) - 1)
        password += characters[char]
    return password


def insert_password(password):
    password_entry.delete(0, END)
    password_entry.insert(0, password)


def get_characters():
    lower_case_letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
                          "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    upper_case_letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
                          "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    numerals = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    specials = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "_", "-", "=", "+", "|",
                "\\", "/", ",", "<", ".", ">", "?", "~", "`", ":", ";"]
    characters = lower_case_letters + upper_case_letters + numerals + specials
    return characters


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_or_cancel():
    has_data = check_data()
    if has_data:
        proceed = verify_proceed()
        save_data(proceed)
        display_save_or_cancel_message(proceed)
        clear_fields()
    else:
        throw_no_data_error()


def save_data(proceed):
    if proceed:
        new_data = website_entry.get() + "\n" + username_entry.get() + "\n" + password_entry.get() + "\n\n"
        with open("data.txt", "a") as file:
            file.write(new_data)
        return True


def check_data():
    if password_entry_has_data() and username_entry_has_data() and website_entry_has_data():
        return True
    return False


def throw_no_data_error():
    messagebox.showwarning(title="Field Empty", message="Please fill all data fields")


def display_save_or_cancel_message(proceed):
    if proceed:
        messagebox.showinfo(title="Done", message="Your data has been saved")
    else:
        messagebox.showinfo(title="Cancelling", message="Cancelled, please enter new data")


def verify_proceed():
    display_message = f"Please verify:\n\n" \
              f"Website => {website_entry.get()}\n" \
              f"Username => {username_entry.get()}\n" \
              f"Password => {password_entry.get()}\n\n"
    proceed = messagebox.askokcancel(
        title="Verify",
        message=display_message)
    return proceed


def clear_fields():
    website_entry.delete(0, END)
    password_entry.delete(0, END)


def website_entry_has_data():
    if len(website_entry.get()) > 10:
        return True
    return False


def password_entry_has_data():
    if len(password_entry.get()) > 7:
        return True
    return False


def username_entry_has_data():
    if len(username_entry.get()) > 7:
        return True
    return False


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)
pi = PhotoImage(file="logo.png")

canvas = Canvas(width=WINDOW_WIDTH, height=WINDOW_HEIGHT, highlightthickness=0)
canvas.create_image((WINDOW_HEIGHT / 2 - 40, WINDOW_WIDTH / 2), image=pi)
canvas.grid(row=0, column=1)

website_label = Label(window)
website_label.config(text="Website")
website_label.grid(row=1, column=0)

website_entry = Entry(window)
website_entry.config(width=35)
website_entry.grid(sticky="w", row=1, column=1, columnspan=2)
website_entry.focus()

username_label = Label(window)
username_label.config(text="Email/Username")
username_label.grid(row=2, column=0)

username_entry = Entry(window)
username_entry.config(width=35)
username_entry.grid(sticky="w", row=2, column=1, columnspan=2)
username_entry.insert(0, "yehoshua.kahan@gmail.com")

password_label = Label(window)
password_label.config(text="Password")
password_label.grid(row=3, column=0, columnspan=1)

password_entry = Entry(window)
password_entry.config(width=35)
password_entry.grid(sticky="w", row=3, column=1, columnspan=2)

password_button = Button(window)
password_button.config(text="Generate Password", width=40, command=lambda: create_random_password())
password_button.grid(sticky="e", row=4, column=0, columnspan=3)

add_button = Button(window)
add_button.config(text="Add To Database", width=40, command=lambda: save_or_cancel())
add_button.grid(sticky="e", row=5, column=0, columnspan=3)

window.mainloop()
