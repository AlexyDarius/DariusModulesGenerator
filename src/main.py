import tkinter as tk
import time
from tkinter import filedialog
from generate_arbo import generate_arbo
from generate_auth_php import generate_auth_php
from generate_login_php import generate_login_php
from generate_checker_php import generate_checker_php
from generate_modules_index_php import generate_modules_index_php

def generate_files():
    directory_path = directory_var.get()
    main_domain = main_domain_entry.get()
    modules_index_title = modules_index_title_entry.get()
    full_body_tag = full_body_tag_entry.get("1.0", "end-1c")

    if all([directory_path, main_domain, modules_index_title, full_body_tag]):
        # Generate tree path
        generate_arbo(directory_path)
        generate_auth_php(directory_path, main_domain)
        generate_login_php(directory_path, modules_index_title, full_body_tag, main_domain)
        generate_checker_php(directory_path, main_domain)
        generate_modules_index_php(directory_path, modules_index_title, full_body_tag, main_domain)

        result_label.config(text="Modules files have been generated.")

        print("\Modules files well generated, don't forget to minify !")
        print("Read readme.txt for implementation.\n")

        app.quit()
    else:
        result_label.config(text="Please provide all required fields.")

def select_directory():
    directory_path = filedialog.askdirectory()
    if directory_path:
        directory_var.set(directory_path)

def modules_index_title_autofill():
    modules_index_title_entry.delete(0, tk.END)
    modules_index_title_entry.insert(0, "Votre interface gestionnaire")

app = tk.Tk()
app.title("Darius Modules Generator")

directory_var = tk.StringVar()

directory_label = tk.Label(app, text="Select Directory:")
directory_label.pack()
directory_entry = tk.Entry(app, textvariable=directory_var, width = 50)
directory_entry.pack()

select_directory_button = tk.Button(app, text="Browse", command=select_directory)
select_directory_button.pack()

main_domain_label = tk.Label(app, text="Enter the main domain (e.g. dariusdev.fr, without www. !) :")
main_domain_label.pack()
main_domain_entry = tk.Entry(app)
main_domain_entry.pack()

modules_index_title_label = tk.Label(app, text="Enter the modules index page title (e.g. DariusDev - Gestion) :")
modules_index_title_label.pack()
modules_index_title_autofill_button = tk.Button(app, text="Autofill", command=modules_index_title_autofill)
modules_index_title_autofill_button.pack()
modules_index_title_entry = tk.Entry(app)
modules_index_title_entry.pack()

full_body_tag_label = tk.Label(app, text="Full Body tag (e.g. <body style=...>) :")
full_body_tag_label.pack()
full_body_tag_entry = tk.Text(app, width=50, height=5)
full_body_tag_entry.pack()

blank_label = tk.Label(app, text="")
blank_label.pack()

generate_button = tk.Button(app, text="Generate", command=generate_files)
generate_button.pack()

result_label = tk.Label(app, text="")
result_label.pack()

app.mainloop()
