import tkinter as tk
import time
from tkinter import filedialog
from generate_arbo import generate_arbo
from generate_auth_php import generate_auth_php

def generate_files():
    directory_path = directory_var.get()
    main_domain = main_domain_entry.get()

    if all([directory_path, main_domain]):
        # Generate tree path
        generate_arbo(directory_path)
        generate_auth_php(directory_path, main_domain)

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

blank_label = tk.Label(app, text="")
blank_label.pack()

generate_button = tk.Button(app, text="Generate", command=generate_files)
generate_button.pack()

result_label = tk.Label(app, text="")
result_label.pack()

app.mainloop()
