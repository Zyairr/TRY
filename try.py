from tkinter import *
from tkinter import messagebox
from inventory import Admin
import os


def login():
    user=username.get()
    code=password.get()

    if user == "zy" and code == "password":
        new_win = Toplevel (Admin)
        new_obj = Admin (new_win)

#copy paste the code here


    elif user == "" and code == "":
        messagebox.showerror("Error", "Username and password cannot be empty")
    
    elif user == "":
        messagebox.showerror("Error", "Username cannot be empty")
    
    elif code == "":
        messagebox.showerror("Error", "Password cannot be empty")

    elif user != "admin" and code != "admin":
        messagebox.showerror("Error", "Invalid Username or Password")
    
    elif user != "admin":
        messagebox.showerror("Error", "Invalid Username")

    elif code!= "admin":
        messagebox.showerror("Error", "Invalid Password")

    

    





def main_screen():

    global screen
    global username
    global password
    


    #login
    screen = Tk()
    screen.geometry("1280x720+150+80")
    screen.configure(bg = "#d7dae2")
    screen.resizable(0,0)

    #background image
    bg = PhotoImage(file = "background.png")
    bg_label = Label(screen, image = bg).place(x = 0, y = 0, relwidth = 1, relheight = 1)
    

    #icon
    image_icon = PhotoImage(file= "logo.png")
    screen.iconphoto(False, image_icon)
    screen.title("BATANGAS STATE UNIVERSITY")

    lblTitle = Label(text= "BSU SHOP LOGIN", font = ("arial", 50, "bold"), fg = "black", bg = "#d7dae2")
    lblTitle.pack (padx = 30, pady = 50)

    #border
    bordercolor = Frame(screen, bg = "red", width = 800, height = 400)
    bordercolor.pack()

    mainframe = Frame(bordercolor, bg = "#d7dae2", width = 800, height = 400)
    mainframe.pack (padx = 10, pady = 10)

    Label (mainframe, text = "Username:", font = ("arial", 30, "bold"), bg = "#d7dae2").place (x = 100, y = 50)
    Label (mainframe, text = "Password:", font = ("arial", 30, "bold"), bg = "#d7dae2").place (x = 100, y = 150)

    username = StringVar()
    password = StringVar()

    entry_username = Entry (mainframe, textvariable= username, width= 12, bd = 2, font = ("arial", 30))
    entry_username.place (x = 400, y = 50)

    entry_password = Entry (mainframe, textvariable= password, width= 12, bd = 2, font = ("arial", 30), show = "*")
    entry_password.place (x = 400, y = 150)

    #buttons
    Button(mainframe, text = "Login", height = "2", width = 23, bg = "#ed3833", fg = "white", bd = 0, command = login). place (x= 100, y =250)
    Button(mainframe, text = "Exit", height = "2", width = 23, bg = "#00bd56", fg = "white", bd = 0, command = screen.destroy). place (x= 500, y =250)

















    screen.mainloop()
root = Tk
main_screen()


