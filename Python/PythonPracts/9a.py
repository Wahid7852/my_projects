import tkinter as tk

root = tk.Tk()

# Using the `config` method to configure a label
label = tk.Label(root, text="Hello, World!")
label.config(bg="red", font=("Times", 18))
label.pack()

root.mainloop()
