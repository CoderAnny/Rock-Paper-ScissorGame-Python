from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox as msg
import random


root = Tk()
root.title("----- Rock Paper Scissor -----")
root.state("zoomed")
root.update()

# ========= This Function Shows Winner ======= #


def checkIfWin(user_input):
    u = user_input.lower()
    r = 'Rock'.lower()
    p = 'Paper'.lower()
    s = 'Scissor'.lower()

    machine_choice = random.choice(['Rock', 'Paper', 'Scissor'])
    m = machine_choice.lower()

    if u == m:
        msg.showinfo("Games Result!!", "----- Match Tied -----")
    elif u == r and m == p:
        msg.showinfo("Games Result!!", "----- Computer Wins -----")
    elif u == r and m == s:
        msg.showinfo("Games Result!!", "----- You Wins -----")
    elif u == p and m == r:
        msg.showinfo("Games Result!!", "----- You Wins -----")
    elif u == p and m == s:
        msg.showinfo("Games Result!!", "----- Computer Wins -----")
    elif u == s and m == r:
        msg.showinfo("Games Result!!", "----- Computer Wins -----")
    elif u == s and m == p:
        msg.showinfo("Games Result!!", "----- You Wins -----")


# ======= HEADER FRAME CREATION STARTS ======= #
header = Frame(root,bg="#000")
h = Label(header,text="ROCK - PAPER - SCISSOR GAME",bg="#000",fg="#fff",font=('Vernda',25,'bold')).pack(ipady=15)
header.place(x=0,y=0,width=root.winfo_width())

# ======= HEADER FRAME CREATION ENDS ======= #


Img1 = Image.open("Images/rockImg.jpg")
new_img = Img1.resize((200, 200), Image.ANTIALIAS)
rock_img = ImageTk.PhotoImage(new_img)

Img2 = Image.open("Images/paperimg.jpg")
new_img = Img2.resize((200, 200), Image.ANTIALIAS)
paper_img = ImageTk.PhotoImage(new_img)

Img3 = Image.open("Images/scissorImg.jpg")
new_img = Img3.resize((200, 200), Image.ANTIALIAS)
scissor_img = ImageTk.PhotoImage(new_img)

b1 = Button(root, cursor="hand2", image=rock_img,
            command=lambda: checkIfWin('Rock'))
b1.place(x=400, y=250)
b2 = Button(root, cursor="hand2", image=paper_img,
            command=lambda: checkIfWin('Paper'))
b2.place(x=600, y=250)
b3 = Button(root, cursor="hand2", image=scissor_img,
            command=lambda: checkIfWin('Scissor'))
b3.place(x=800, y=250)

root.config(bg="#000")
root.mainloop()
