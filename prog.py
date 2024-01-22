import tkinter as tk 
from tkinter import simpledialog

number = tk.simpledialog.askinteger("Hello!", "Input your number: ")
reverse_number_string = str(number)[::-1]
digit_count = len(reverse_number_string)

while digit_count >= 1:
    digit_position = digit_count - 1
    print(reverse_number_string[digit_position])
    digit_count = digit_count - 1