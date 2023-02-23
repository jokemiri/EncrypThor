from tkinter import *
from tkinter import messagebox
import base64
import os

def decrypt():
    password = code.get()

    if password == "1234":
        screen2=Toplevel(screen)    #encrypted message window
        screen2.title("Decrypted Message")  ##encrypted message window title
        screen2.geometry("400x200") #encrypted message window dimensions
        screen2.configure(bg='#00bd56') #encrypted message window background color
        screen2.resizable(False, False)

        #main window icon
        decrypt_window_icon = PhotoImage(file='decrypt_window_icon.png')
        screen2.iconphoto(False, decrypt_window_icon)

        report = text1.get(1.0, END)
        decode_message = report.encode("ascii")
        base64_bytes = base64.b64decode(decode_message)
        decrypt = base64_bytes.decode("ascii")

        screen2_label = Label(screen2, text='DECRYPTED', font="Calibri 20", fg='white', bg='#00bd56').place(x=10, y=0)
        text2 = Text(screen2, font='Robote 10', bg= 'white', relief=GROOVE, wrap=WORD, bd=0)
        text2.place(x=10, y=40, width=300, height=150)
   
        text2.insert(END, decrypt)
        
    elif password == "":
        messagebox.showerror("EncrypThor", "Please enter decryption password")

    elif password != "1234":
        messagebox.showerror("EncrypThor","Incorrect decryption password")


def encrypt():      #encrypted message screen function
    password = code.get()

    if password == "1234":
        screen1=Toplevel(screen)    #encrypted message window
        screen1.title("Encrypted Message")  ##encrypted message window title
        screen1.geometry("400x200") #encrypted message window dimensions
        screen1.configure(bg='#ed3833') #encrypted message window background color
        screen1.resizable(False, False)

        #main window icon
        encrypt_window_icon = PhotoImage(file='encrypt_window_icon.png')
        screen1.iconphoto(False, encrypt_window_icon)

        report = text1.get(1.0, END)
        encode_message = report.encode("ascii")
        base64_bytes = base64.b64encode(encode_message)
        encrypt = base64_bytes.decode("ascii")

        screen1_label = Label(screen1, text='ENCRYPTED', font="Calibri 20", fg='white', bg='#ed3833').place(x=10, y=0)
        text2 = Text(screen1, font='Robote 10', bg= 'white', relief=GROOVE, wrap=WORD, bd=0)
        text2.place(x=10, y=40, width=300, height=150)
   
        text2.insert(END, encrypt)

    elif password == "":
        messagebox.showerror("EncrypThor", "Please enter encryption password")

    elif password != "1234":
        messagebox.showerror("EncrypThor","Incorrect encryption password")


        


def main_window():

    global screen
    global code
    global text1

    screen = Tk()
    screen.geometry("375x400")
    screen.resizable(False, False)
    screen.configure(bg='#3e605a')

    #main window logo
    logo = PhotoImage(file='logo.png')
    Label(screen, image=logo, bg='#3e605a').place(x=0, y=0)

    #main window icon
    main_window_icon = PhotoImage(file='main_window_icon.png')
    screen.iconphoto(False, main_window_icon)
    screen.title("EncrypThor")

    def reset():
        code.set("")
        text1.delete(1.0,END)


    message_prompt = Label(text="Enter message to be encrypted/decrypted here.", fg='white', bg='#3e605a', width=50, font=("Calibri", 12)).place(x=8, y=50)
    text1 = Text(font=("Californian FB", 20), bg='white', relief=GROOVE, wrap=WORD, bd=0)
    text1.place(x=10, y=70, width=355, height=100)

    password_prompt = Label(text="Enter password to encrypt/decrypt message", fg='white', bg='#3e605a', font=("Calibri", 12)).place(x=15, y=178)
    
    code = StringVar()
    password_entry = Entry(textvariable=code, width=19, bd=0, font=("Arial", 25), show="*").place(x=15, y=200)

    encrypt_button = Button(text="ENCRYPT", height=2, width=23, bg='#ed3833', fg='white', bd=0, command=encrypt).place(x=10, y=250)
    decrypt_button = Button(text="DECRYPT", height=2, width=23, bg='#00bd56', fg='white', bd=0, command=decrypt).place(x=200, y=250)
    reset_button = Button(text="RESET", height=2, width=50, bg='#1089ff', fg='white', bd=0, command=reset).place(x=10, y=300)
    screen.mainloop()

main_window()

