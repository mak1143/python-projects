
import tkinter as tk
from tkinter import filedialog

def save_as():
    text = text_area.get("1.0", "end-1c")
    save_location = filedialog.asksaveasfilename(defaultextension=".txt")
    with open(save_location, "w") as file:
        file.write(text)

root = tk.Tk()
root.title("Simple Text Editor")

text_area = tk.Text(root)
text_area.pack(expand=True, fill='both')

save_button = tk.Button(root, text="Save", command=save_as)
save_button.pack()

root.mainloop()
