from tkinter import *
from tkinter import messagebox
import os

# Global variables
screen = None
username = None
password = None
student_username = None
student_password = None
student_screen = None
inventory_management_frame = None
items = []

#copy paste the code here
       
class InventoryManagement(Frame):

        # Creates constructor for main frame of application
    
            def __init__(self):
                Frame.__init__(self)
                self.master.title('ADMIN INVENTORY MANAGEMENT')
                image_icon = PhotoImage(file="logo.png")
                self.master.iconphoto(False, image_icon)
                self.grid()
                self.items = items

                self.itemCount = len(self.items)

        # search feature labels/entry/buttons

                Label(self, text='Search (Item Number): ').grid(row=0,
                                                        column=1, padx=6, pady=20, sticky=E)

                self._box1 = IntVar()
                self._input = Entry(self, width=20, textvariable=self._box1)
                self._input.grid(row=0, column=2, padx=8, pady=20, sticky=W)

                self.btn1 = Button(self, text='Search',
                           command=self.searchInventory)
                self.btn1.grid(row=0, column=3, padx=8, pady=20, sticky=W)

                self.btn2 = Button(self, text='Reset', command=self.clearSearch)
                self.btn2.grid(row=0, column=4, padx=4, pady=20, sticky=W)

        # main text area for inventory display

                self.scroll = Scrollbar(self)
                self.scroll.grid(row=3, column=4)
                self.text = Text(self, width=60, height=10, wrap=WORD,
                         yscrollcommand=self.scroll.set)
                self.text.grid(row=3, column=0, columnspan=5, padx=20, pady=20)
                self.scroll.config(command=self.text.yview)

                Label(self, text="Item Count: \t \t "  + str(self.itemCount)).grid(row=4, column=0, pady=5, sticky=N)

        # labels/entry boxes for new/edit item entry

                Label(self, text='Item Number \t \t').grid(row=6, column=0, padx=6,
                                              pady=6, sticky=W)

                self._box2 = StringVar()
                self._input1 = Entry(self, width=20, textvariable=self._box2)
                self._input1.grid(row=6, column=1, padx=8, pady=10, sticky=E)

                Label(self, text='Item Name \t \t').grid(row=6, column=2, padx=6,
                                            pady=6, sticky=E)

                self._box3 = StringVar()
                self._input = Entry(self, width=20, textvariable=self._box3)
                self._input.grid(row=6, column=3, padx=8, pady=10, sticky=E)

                Label(self, text='On Hand \t \t').grid(row=10, column=0, padx=6,
                                          pady=6, sticky=E)

                self._box4 = StringVar()
                self._input = Entry(self, width=20, textvariable=self._box4)
                self._input.grid(row=10, column=1, padx=8, pady=10, sticky=W)

                Label(self, text='Price ').grid(row=10, column=2, padx=6,
                                        pady=6, sticky=E)

                self._box5 = StringVar()
                self._input = Entry(self, width=20, textvariable=self._box5)
                self._input.grid(row=10, column=3, padx=8, pady=10)

        # buttons for corresponding functions to add/edit/delete items from text area

                self.btn3 = Button(self, text='Add Item', command=self.addItem)
                self.btn3.grid(row=11, column=1, padx=5, pady=20, sticky=W)

                self.btn4 = Button(self, text='Edit Item',
                           command=self.editItem)
                self.btn4.grid(row=11, column=2, padx=5, pady=20, sticky=W)

                self.btn4 = Button(self, text='Delete Item',
                           command=self.deleteItem)
                self.btn4.grid(row=11, column=3, padx=5, pady=20, sticky=W)

        # insert headers into text area and sets focus to Item Number entry box
                self.text.insert(END, 'Item Number' + '\t\t' + 'Item Name'
                         + '\t\t' + 'On Hand' + '\t\t' + 'Price'
                         + '\t\t')
                self.text.insert(END,
                         '------------------------------------------------------------'
                         )
                self.text.configure(state="disabled")
                self._input1.focus_set()
                
                self.logout_btn = Button(self, text = "Logout", bd = 0, font = ("Goudy old style", 12), fg = "#6162FF", bg = "white", command = self.logout).place (x = 500, y = 280)
                self.logout_btn.grid(row=12, column=1, padx=5, pady=20, sticky=W)

            ''' addItem() function inserts headers into text area, grabs values from entry boxes 
        and appends them to a list of dictionaries if entry boxes are not empty.  It then prints
        each item(dictionary) to the text area and clears the entry boxes. '''


            def addItem(self):

                self.text.configure(state="normal")
                self.text.delete(1.0, END)
                self.text.insert(END, 'Item Number' + '\t\t' + 'Item Name'
                         + '\t\t' + 'On Hand' + '\t\t' + 'Price'
                         + '\t\t')
                self.text.insert(END,
                         '------------------------------------------------------------'
                         )

                items = self.items

                iNum = self._box2.get()
                iName = self._box3.get()
                oHand = self._box4.get()
                iPrice = self._box5.get()
    
                if (iNum != '' and iName != '' and oHand != '' and iPrice != ''):
                    record = {
                        0: iNum,
                        1: iName,
                        2: oHand,
                        3: iPrice,
            }
                    items.append(record)

                    for item in items:
                        self.text.insert(END, item[0] + '\t\t' + item[1] + '\t\t'
                                 + item[2] + '\t\t' + item[3] + '\t\t')
                else:
                    self.text.delete(1.0, END)
                    self.text.insert(END, 'Error: One or more fields have been left blank.')

                self._box2.set('')
                self._box3.set('')
                self._box4.set('')
                self._box5.set('')
                self._input1.focus_set()

                self.text.configure(state="disabled")

                return

            ''' searchInventory() function inserts headers into text area, gets value of search box entry and compares to
        list of dictionaries.  If the search box value matches the item number key,
         it inserts the dictionaries values into the text area. '''


            def searchInventory(self):
                self.text.configure(state="normal")
                self.text.delete(1.0, END)
                self.text.insert(END, 'Item Number' + '\t\t' + 'Item Name'
                         + '\t\t' + 'On Hand' + '\t\t' + 'Price'
                         + '\t\t')
                self.text.insert(END,
                         '------------------------------------------------------------'
                         )

                searchVal = str(self._box1.get())

                for item in self.items:
                    if item[0] == searchVal:
                        self.text.insert(END, item[0] + '\t\t' + item[1]
                                 + '\t\t' + item[2] + '\t\t' + item[3]
                                 + '\t\t')

                        self.text.configure(state="disabled")

    # Simple function attached to reset button to clear the search box

            def clearSearch(self):
                self._box1.set('')

            ''' editItem() function clears the entry boxes to prevent errors.  It then grabs the search box value and compares
        to the list of dictionaries.  If the dictionary's item number matches the value it inserts the value of the 
        dictionary into the entry boxes for editing. '''


            def editItem(self):
                self.text.configure(state="normal")
                self._box2.set('')
                self._box3.set('')
                self._box4.set('')
                self._box5.set('')

                items = self.items

                searchVal = str(self._box1.get())

                for item in items:
                    if item[0] == searchVal:
                        self.items.remove(item)
                        self._box2.set(item[0])
                        self._box3.set(item[1])
                        self._box4.set(item[2])
                        self._box5.set(item[3])

                self._box1.set('')
                self._input1.focus_set()

                self.text.configure(state="disabled")


    # Simple function to delete dictionary with item number that matches the search box value

            def deleteItem(self):
                self.text.configure(state="normal")
                self.text.delete(1.0, END)
                self.text.insert(END, 'Item Number' + '\t\t' + 'Item Name'
                         + '\t\t' + 'On Hand' + '\t\t' + 'Price'
                         + '\t\t')
                self.text.insert(END,
                         '------------------------------------------------------------'
                         )

                items = self.items

                searchVal = str(self._box1.get())

                for item in items:
                    if item[0] == searchVal:
                        self.items.remove(item)

                for item in items:
                    self.text.insert(END, item[0] + '\t\t' + item[1] + '\t\t'
                             + item[2] + '\t\t' + item[3] + '\t\t')

                self._box1.set('')
                self.text.configure(state="disabled")
            
            def logout(self):
                # Add any additional logout logic if needed
                messagebox.showinfo("Logout", "Admin logout successful!")
                self.master.destroy()  # Close the inventory management frame
                main_screen()
                
def open_inventory_management():
    global inventory_management_frame

    # Check if the inventory management frame is already open
    if inventory_management_frame is not None:
        return

    # Create the inventory management frame
    inventory_management_frame = InventoryManagement()
    inventory_management_frame.mainloop()

    # Set inventory_management_frame to None when the frame is closed
    inventory_management_frame = None
  
class StudentShoppingFrame(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.master.title('BSU SHOPPING PLATFORM')
        image_icon = PhotoImage(file="logo.png")
        self.master.iconphoto(False, image_icon)
        self.grid()
        self.items = items

        Label(self, text= "BSU SHOPPING PLATFORM", font = ("Impact", 30, "bold"), fg = "#6162FF").grid(row=0, column=1, padx=400, pady=20, sticky=E)
        
        # Create a Listbox to display available items
        self.item_listbox = Listbox(self, width=60, height=10)
        self.item_listbox.grid(row=1, column=0, columnspan=5, padx=50, pady=20)
        
        # Populate the Listbox with available items
        self.populate_item_listbox()
        
        self.order_btn = Button(self, text='Order Item', command=self.order_item)
        self.order_btn.grid(row=15, column=1, padx=5, pady=20, sticky=W)
        
        self.student_logout_btn = Button(self, text = "Logout", bd = 0, font = ("Goudy old style", 12), bg = "#6162FF", fg = "white", cursor ="hand2", command = self.student_logout).place (x = 40, y = 280, width = 180, height = 40)
        self.student_logout_btn.grid(row=12, column=1, padx=5, pady=20, sticky=W)

    def populate_item_listbox(self):
        # Clear the Listbox
        self.item_listbox.delete(0, END)

        # Insert headers into the Listbox
        self.item_listbox.insert(END, 'Item Number' + '\t\t' + 'Item Name'
                                 + '\t\t' + 'On Hand' + '\t\t' + 'Price')

        self.item_listbox.insert(END,
                                 '------------------------------------------------------------')

        
        # Insert available items into the Listbox
        for index, item in enumerate(self.items):
            self.item_listbox.insert(END, item[0] + '\t\t' + item[1] + '\t\t'
                                     + item[2] + '\t\t' + item[3])
            order_button = Button(self, text='Order', command=lambda i=index: self.order_item(i))
            order_button.grid(row=index + 3, column=4, padx=5)
        
        self.item_listbox.configure(state="disabled")
        
    def order_item(self, item_index):
        selected_item = self.items[item_index]

        # Check if there are items on hand
        if selected_item[2] > 0:
            selected_item[2] -= 1  # Decrement on_hand
            messagebox.showinfo("Order Placed", f"You have ordered {selected_item[1]}")
            self.populate_item_listbox()  # Refresh the Listbox
        else:
            messagebox.showinfo("Out of Stock", "This item is currently out of stock.")

    
    def student_logout(self):
        # Add any additional logout logic if needed
        messagebox.showinfo("Logout", "Student logout successful!")
    
        # Hide the current frame
        self.grid_forget()
    
        # Show the main screen again
        main_screen_ref.iconify()  # Iconify (minimize) the main screen
        main_screen_ref.deiconify()  # Deiconify (restore) the main screen
        
def student_shopping():
    root = Toplevel()
    root.geometry("1199x600+100+50")
    root.resizable(False, False)

    # Create an instance of StudentShoppingFrame
    student_shopping_frame = StudentShoppingFrame(master=root)
    student_shopping_frame.mainloop()
    
def login():
    user=username.get()
    code=password.get()

    if user == "zy" and code == "password":
        messagebox.showinfo("Success", "Admin login successful!")
        screen.destroy()
        open_inventory_management()
    elif user == "" and code == "":
        messagebox.showerror("Error", "Username and password cannot be empty")
    
    elif user == "":
        messagebox.showerror("Error", "Username cannot be empty")
    
    elif code == "":
        messagebox.showerror("Error", "Password cannot be empty")

    elif user != "zy" and code != "password":
        messagebox.showerror("Error", "Invalid Username or Password")
    
    elif user != "zy":
        messagebox.showerror("Error", "Invalid Username")

    elif code!= "password":
        messagebox.showerror("Error", "Invalid Password")
        
        
def student_login():
    student_user = student_username.get()
    student_code = student_password.get()

    if student_user == "student" and student_code == "password":
        messagebox.showinfo("Success", "Student login successful!")
        screen.iconify()
        student_shopping()
    elif student_user == "" and student_code == "":
        messagebox.showerror("Error", "Username and password cannot be empty")
    
    elif student_user == "":
        messagebox.showerror("Error", "Username cannot be empty")
    
    elif student_code == "":
        messagebox.showerror("Error", "Password cannot be empty")

    elif student_user != "admin" and student_code != "admin":
        messagebox.showerror("Error", "Invalid Username or Password")
    
    elif student_user != "admin":
        messagebox.showerror("Error", "Invalid Username")

    elif student_code!= "admin":
        messagebox.showerror("Error", "Invalid Password")

def main_screen():
    global main_screen_ref, screen, username, password
    
    #login
    screen = Tk()
    screen.geometry("1199x600+100+50")
    screen.resizable(0,0)

    #background image
    bg = PhotoImage(file = "background.png")
    bg_label = Label(screen, image = bg).place(x = 0, y = 0, relwidth = 1, relheight = 1)
    
    #icon
    image_icon = PhotoImage(file= "logo.png")
    screen.iconphoto(False, image_icon)
    screen.title("BATANGAS STATE UNIVERSITY")

    mainframe = Frame( bg = "white")
    mainframe.place( x = 330, y = 150, width = 500, height = 400)

    lblTitle = Label(text= "BSU SHOP ADMIN LOGIN", font = ("Impact", 30, "bold"), fg = "#6162FF", bg = "white").place(x = 360, y = 180)
    lblsubtitle = Label(text = "Login Here:", font = ("Goudy old style", 15, "bold"), fg = "#1d1d1d", bg = "white").place (x = 380, y = 250)

    
    Label (mainframe, text = "Username:", font = ("Goudy old style", 15, "bold"), fg = "black", bg = "white").place(x = 90, y = 140)
    Label (mainframe, text = "Password:", font = ("Goudy old style", 15, "bold"), fg = "black", bg = "white").place (x = 90, y = 210)

    username = StringVar()
    password = StringVar()

    entry_username = Entry (mainframe, textvariable= username, width= 12, bd = 2, font = ("arial", 20))
    entry_username.place (x = 90, y =170, width = 320, height = 35)

    entry_password = Entry (mainframe, textvariable= password, width= 12, bd = 2, font = ("arial", 20), show = "*")
    entry_password.place (x = 90, y =240, width = 320, height = 35)

    #buttons
    Button(mainframe, text = "Login", bd = 0, font = ("Goudy old style", 12), bg = "#6162FF", fg = "white", cursor ="hand2", command = login).place (x = 90, y = 320, width = 180, height = 40)

    Button(mainframe, text = "Student Login", bd = 0, font = ("Goudy old style", 12), fg = "#6162FF", bg = "white", command = student_login_screen).place (x = 310, y = 280)
    Button(mainframe, text = "Exit", bd = 0, font = ("Goudy old style", 12), fg = "#6162FF", bg = "white", command = screen.destroy).place (x = 90, y = 280)

    main_screen_ref = screen
    
    screen.mainloop()
    
def student_login_screen():

    global student_screen
    global student_username
    global student_password
    
     #background image
    bg = PhotoImage(file = "background.png")
    bg_label = Label(screen, image = bg).place(x = 0, y = 0, relwidth = 1, relheight = 1)

    #icon
    image_icon = PhotoImage(file= "logo.png")
    screen.iconphoto(False, image_icon)
    screen.title("BATANGAS STATE UNIVERSITY")

    mainframe = Frame( bg = "white")
    mainframe.place( x = 330, y = 150, width = 500, height = 400)

    lblTitle = Label(text= "BSU SHOP STUDENT LOGIN", font = ("Impact", 30, "bold"), fg = "#6162FF", bg = "white").place(x = 360, y = 180)
    lblsubtitle = Label(text = "Login Here:", font = ("Goudy old style", 15, "bold"), fg = "#1d1d1d", bg = "white").place (x = 380, y = 250)

    Label (mainframe, text = "Username:", font = ("Goudy old style", 15, "bold"), fg = "black", bg = "white").place(x = 90, y = 140)
    Label (mainframe, text = "Password:", font = ("Goudy old style", 15, "bold"), fg = "black", bg = "white").place (x = 90, y = 210)

    student_username = StringVar()
    student_password = StringVar()

    student_entry_username = Entry (mainframe, textvariable= student_username, width= 12, bd = 2, font = ("arial", 20))
    student_entry_username.place (x = 90, y =170, width = 320, height = 35)

    student_entry_password = Entry (mainframe, textvariable= student_password, width= 12, bd = 2, font = ("arial", 20), show = "*")
    student_entry_password.place (x = 90, y =240, width = 320, height = 35)

    #buttons
    Button(mainframe, text = "Login", bd = 0, font = ("Goudy old style", 12), bg = "#6162FF", fg = "white", cursor ="hand2", command = student_login).place (x = 90, y = 320, width = 180, height = 40)
    
    Button(mainframe, text = "Exit", bd = 0, font = ("Goudy old style", 12), fg = "#6162FF", bg = "white", command = screen.destroy).place (x = 90, y = 280)
    
    mainloop()

main_screen()


