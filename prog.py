import tkinter as tk 
from tkinter import simpledialog

number = tk.simpledialog.askinteger("Hello!", "Input your number: ")
number_str = str(number)
digit_count = len(number_str)
resulting_var = ""

while digit_count >= 1:
    digit_position = digit_count - 1
    specific_digit = number_str[digit_position]
    digit_count = digit_count - 1
    resulting_var + " " + specific_digit

print(resulting_var)