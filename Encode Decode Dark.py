from tkinter import *
import base64

# Initialize window
root = Tk()
root.geometry('500x300')
root.resizable(0, 0)
root.title("Nawin's Secret - Message Encode and Decode")

# Dark theme colors
bg_color = '#222222'
fg_color = '#ffffff'
entry_bg_color = '#333333'
button_bg_color = '#555555'
button_fg_color = '#ffffff'

# Set window background color
root.configure(bg=bg_color)

# Label styles
label_style = 'arial 20 bold'
result_label_style = 'arial 10 bold'

# Variables
Text = StringVar()
private_key = StringVar()
mode = StringVar()
Result = StringVar()

# Function to encode
def Encode(key, message):
    enc = []
    for i in range(len(message)):
        key_c = key[i % len(key)]
        enc.append(chr((ord(message[i]) + ord(key_c)) % 256))
    return base64.urlsafe_b64encode("".join(enc).encode()).decode()

# Function to decode
def Decode(key, message):
    dec = []
    message = base64.urlsafe_b64decode(message).decode()
    for i in range(len(message)):
        key_c = key[i % len(key)]
        dec.append(chr((256 + ord(message[i]) - ord(key_c)) % 256))
    return "".join(dec)

# Function to set mode
def Mode():
    if mode.get() == 'E':
        Result.set(Encode(private_key.get(), Text.get()))
    elif mode.get() == 'D':
        Result.set(Decode(private_key.get(), Text.get()))
    else:
        Result.set('Invalid Mode')

# Function to exit window
def Exit():
    root.destroy()

# Function to reset
def Reset():
    Text.set("")
    private_key.set("")
    mode.set("")
    Result.set("")

# MESSAGE label
Label(root, font=label_style, text='ENCODE DECODE', fg=fg_color, bg=bg_color).pack()
Label(root, font=label_style, text='Nawin Hides', fg=fg_color, bg=bg_color).pack(side=BOTTOM)
Label(root, font='arial 12 bold', text='MESSAGE', fg=fg_color, bg=bg_color).place(x=60, y=60)
Entry(root, font='arial 10', textvariable=Text, bg=entry_bg_color, fg=fg_color).place(x=290, y=60)

# KEY label
Label(root, font='arial 12 bold', text='KEY', fg=fg_color, bg=bg_color).place(x=60, y=90)
Entry(root, font='arial 10', textvariable=private_key, bg=entry_bg_color, fg=fg_color).place(x=290, y=90)

# MODE label
Label(root, font='arial 12 bold', text='MODE(E-Encode, D-Decode)', fg=fg_color, bg=bg_color).place(x=60, y=120)
Entry(root, font='arial 10', textvariable=mode, bg=entry_bg_color, fg=fg_color).place(x=290, y=120)

# RESULT label
Entry(root, font=result_label_style, textvariable=Result, bg=entry_bg_color, fg=fg_color).place(x=290, y=150)

# RESULT button
Button(root, font='arial 10 bold', text='RESULT', padx=2, bg=button_bg_color, fg=button_fg_color, command=Mode).place(x=60, y=150)

# RESET button
Button(root, font='arial 10 bold', text='RESET', padx=2, width=6, command=Reset, bg=button_bg_color, fg=button_fg_color).place(x=80, y=190)

# EXIT button
Button(root, font='arial 10 bold', text='EXIT', width=6, command=Exit, bg=button_bg_color, fg=button_fg_color, padx=2, pady=2).place(x=180, y=190)

root.mainloop()
