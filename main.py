import tkinter as tk
from tkinter import messagebox


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    email_txt = email_entry.get()
    website_txt = website_entry.get()
    password_txt = password_entry.get()
    # info = messagebox.showinfo(title='empty filed', message='fill all the entry')
    # print(info)

    if len(email_txt) and len(website_txt) and len(password_txt):
        want_to_save = messagebox.askyesno(title='ask yes/no', message='Want to save?')
        if want_to_save:
            with open('data.txt', 'a') as file:
                file.write(f'{email_txt} | {website_txt} | {password_txt}\n')

            website_entry.delete(0, 'end')
            email_entry.delete(0, 'end')
            password_entry.delete(0, 'end')
    else:
        error = messagebox.showerror(title='Attention!', message='Fill All the Entry')
        print(error)


# ---------------------------- UI SETUP ------------------------------- #


window = tk.Tk()
window.config(padx=50, pady=50)

# Canvas Widget------------------------------------
canvas = tk.Canvas(width=200, height=200)
image_logo = tk.PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=image_logo)
# canvas.create_line(10, 5, 200, 50)
canvas.grid(row=0, column=1)

# Label Widget---------------------------------------
website_label = tk.Label(text='Website:', font=('Arial', 10, 'bold'))
website_label.grid(row=1, column=0, )

email_username_label = tk.Label(text='Email/Username:', font=('Arial', 10, 'bold'))
email_username_label.grid(row=2, column=0)

password_label = tk.Label(text='Password:', font=('Arial', 10, 'bold'))
password_label.grid(row=3, column=0)

# Entry Widget---------------------------------------
text = 'akash'
website_entry = tk.Entry(width=51, )
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()

email_entry = tk.Entry(width=51, )
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, string='aksky9835@gmail.com')

password_entry = tk.Entry(width=33)
password_entry.grid(row=3, column=1)

# Button Widget --------------------------------------

generate_button = tk.Button(text='Generate Password')
generate_button.grid(row=3, column=2)

add_button = tk.Button(text="Add", width=43, command=save)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
