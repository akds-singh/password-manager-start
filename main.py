import json
import tkinter as tk
from tkinter import messagebox
import random


# -----------------------------Search Email Password------------------------------#
def search():
    # get the entry text from email entry filed
    website_entry_data = website_entry.get()
    print(website_entry_data)
    # check weather the value get from above is available in Json file:
    try:
        with open('data.json', 'r') as file:
            data_dict = json.load(file)
    except json.decoder.JSONDecodeError:
        messagebox.showerror(title='Oops', message=f'JSON file is empty')
    except FileNotFoundError:
        with open('data.json', 'w') as file:
            pass
    else:
        # print(data_dict)
        if website_entry_data in data_dict.keys():
            email = data_dict[website_entry_data]['email']
            # print(email)
            password = data_dict[website_entry_data]['password']
            # print(password)
            messagebox.showinfo(title='available', message=f'{website_entry_data}\nEmail Id: {email}\nPassword: {password} ')
            # print('available')
        else:
            # print('not available')
            messagebox.showerror(title='Oops', message=f"Email and Password for  '{website_entry_data}' is not available")
        # if id is not available then prompt 'not available'
        # else if available then fetch the is form Json and Prompt the data to user


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def password_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    rand_letters = [random.choice(letters) for num1 in range(nr_letters)]
    rand_numbers = [random.choice(numbers) for num2 in range(nr_symbols)]
    rand_symbols = [random.choice(symbols) for num3 in range(nr_numbers)]

    password_list = rand_letters + rand_numbers + rand_symbols
    random.shuffle(password_list)
    password = ''.join(password_list)

    password_entry.delete(0, 'end')
    password_entry.insert(0, password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    email_txt = email_entry.get()
    website_txt = website_entry.get()
    password_txt = password_entry.get()
    # info = messagebox.showinfo(title='empty filed', message='fill all the entry')
    # print(info)
    data = {website_txt: {'email': email_txt,
                          'password': password_txt,
                          }

            }
    if len(email_txt) and len(website_txt) and len(password_txt):
        want_to_save = messagebox.askyesno(title='ask yes/no', message='Want to save?')
        if want_to_save:
            try:
                with open('data.json', 'r') as file_data:
                    data_dict = json.load(fp=file_data)
            except FileNotFoundError:
                print('FileNotFoundError')
                with open('data.json', 'w') as file_data:
                    json.dump(data, fp=file_data, indent=4)
            except json.decoder.JSONDecodeError:
                print('json.decoder.JSONDecodeError')
                with open('data.json', 'w') as file_data:
                    json.dump(data, fp=file_data, indent=4)
            else:
                data_dict.update(data)
                with open('data.json', 'w') as file_data:
                    json.dump(data_dict, fp=file_data, indent=4)
            finally:
                website_entry.delete(0, 'end')
                password_entry.delete(0, 'end')

    else:
        error = messagebox.showerror(title='Attention!', message='Fill All the Entry')


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
website_entry = tk.Entry(width=33)
website_entry.grid(row=1, column=1, )
website_entry.focus()

email_entry = tk.Entry(width=51, )
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, string='aksky9835@gmail.com')

password_entry = tk.Entry(width=33)
password_entry.grid(row=3, column=1)

# Button Widget --------------------------------------

generate_button = tk.Button(text='Generate Password', command=password_generator)
generate_button.grid(row=3, column=2)

add_button = tk.Button(text="Add", width=43, command=save)
add_button.grid(row=4, column=1, columnspan=2)

search_button = tk.Button(text='Search', width=15, command=search)
search_button.grid(row=1, column=2)
window.mainloop()
