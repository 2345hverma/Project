#importing all required file 
from tkinter import *
from tkinter import messagebox
import base64
import os
# By this function we are doing decrption
def decrypt():
     password = code.get()
# here we are checking the password if password is correct it decrpt the data
     if password == "1234":
          screen2 = Toplevel(screen)
          screen2.title("decryption")
          screen2.geometry("400x200")
          screen2.configure(bg="#00bd56")

          message = text1.get(1.0, END)
          decode_message = message.encode("ascii")
          base64_bytes = base64.b64decode(decode_message)
          decrypt = base64_bytes.decode("ascii")

          Label(screen2, text="DECRYPT", font="arial", fg="white", bg="#00bd56").place(x=10, y=10)
          text2 = Text(screen2, font="Rpbote 10", bg="white", relief=GROOVE, wrap=WORD, bd=0)
          text2.place(x=10, y=40, width=380, height=150)

          text2.insert(END, decrypt)
# if password is wrong or invalid it will create an another window
     elif password == "":
          messagebox.showerror("encryption", "Input Password")

     elif password != "1234":
          messagebox.showerror("encryption", "Input Password")

# By this function we are doing encrption
def encrypt():
     password=code.get()
# again we are checking the password
     if password=="1234":
          screen1=Toplevel(screen)
          screen1.title("encryption")
          screen1.geometry("400x200")
          screen1.configure(bg="#ed3833")

          message=text1.get(1.0,END)
          encode_message=message.encode("ascii")
          base64_bytes=base64.b64encode(encode_message)
          encrypt=base64_bytes.decode("ascii")

          Label(screen1,text="ENCRYPT",font="arial",fg="white",bg="#ed3833").place(x=10,y=10)
          text2=Text(screen1,font="Rpbote 10", bg="white",relief=GROOVE,wrap=WORD,bd=0)
          text2.place(x=10,y=40,width=380,height=150)

          text2.insert(END,encrypt)
# if password is wrong or invalid it will create an another window
     elif password=="":
          messagebox.showerror("encryption","Input Password")

     elif password!="1234":
          messagebox.showerror("encryption","Input Password")
# Here we are creating a UI for Encipher and Decipher
def main_screen():
     global screen
     global code
     global text1

     screen=Tk()
     screen.geometry("375x398")

     screen.title("PctApp")
# by this function we reset the input
     def reset():
          code.set("")
          text1.delete(1.0,END)


# In this section we are adding a different different feilds in the UI
     Label(text="Enter text for encryption and decrption", fg="black", font=("calbri", 13)).place(x=10, y=10)
     text1=Text(font="Robote 20",bg="white",relief=GROOVE,wrap=WORD,bd=0)
     text1.place(x=10,y=50,width=355,height=100)
     Label(text="Enter secret for encryption and decrption", fg="black", font=("calbri", 13)).place(x=10, y=170)
     code = StringVar()
     Entry(textvariable=code,width=19,bd=0,font=("arial",25),show="*").place(x=10,y=200)
     Button(text="ENCRYPT",height="2",width=23,bg="#ed3833",fg="white",bd=0).place(x=10,y=250)
     Button(text="ENCRYPT", height="2", width=23, bg="#ed3833", fg="white", bd=0,command=encrypt).place(x=10, y=250)
     Button(text="DECRYPT", height="2", width=23, bg="#00bd56", fg="white", bd=0,command=decrypt).place(x=200, y=250)
     Button(text="RESET", height="2", width=50, bg="#1089ff", fg="white", bd=0,command=reset).place(x=10, y=350)



     screen.mainloop()


main_screen()