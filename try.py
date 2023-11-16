from tkinter import *
from tkinter import messagebox
import os


def login():
    user=username.get()
    code=password.get()

    if user == "zy" and code == "password":
        new_win = Toplevel (InventoryManagement)
        new_obj = InventoryManagement (new_win)

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


root = Tk()

class InventoryManagement(Frame):

    # Creates constructor for main frame of application

    def __init__(self):
        Frame.__init__(self)
        self.master.title('Inventory Management')
        self.grid()
        self.items = []
        root.geometry("650x450")
        root.resizable (False, False)

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

        # Lines 40 - 45 is the main text area for inventory display

        self.scroll = Scrollbar(self)
        self.scroll.grid(row=3, column=4)
        self.text = Text(self, width=60, height=10, wrap=WORD,
                         yscrollcommand=self.scroll.set)
        self.text.grid(row=3, column=0, columnspan=5, padx=20, pady=20)
        self.scroll.config(command=self.text.yview)

        Label(self, text="Item Count: " + str(self.itemCount)).grid(row=4, column=0, pady=5, sticky=N)

        # Lines 49 - 75 are labels/entry boxes for new/edit item entry

        Label(self, text='Item Number ').grid(row=6, column=0, padx=6,
                                              pady=6, sticky=W)

        self._box2 = StringVar()
        self._input1 = Entry(self, width=20, textvariable=self._box2)
        self._input1.grid(row=6, column=1, padx=8, pady=10, sticky=E)

        Label(self, text='Item Name ').grid(row=6, column=2, padx=6,
                                            pady=6, sticky=E)

        self._box3 = StringVar()
        self._input = Entry(self, width=20, textvariable=self._box3)
        self._input.grid(row=6, column=3, padx=8, pady=10, sticky=E)

        Label(self, text='On Hand ').grid(row=10, column=0, padx=6,
                                          pady=6, sticky=E)

        self._box4 = StringVar()
        self._input = Entry(self, width=20, textvariable=self._box4)
        self._input.grid(row=10, column=1, padx=8, pady=10, sticky=W)

        Label(self, text='Price ').grid(row=10, column=2, padx=6,
                                        pady=6, sticky=E)

        self._box5 = StringVar()
        self._input = Entry(self, width=20, textvariable=self._box5)
        self._input.grid(row=10, column=3, padx=8, pady=10)

        # Lines 79 - 88 are buttons for corresponding functions to add/edit/delete items from text area

        self.btn3 = Button(self, text='Add Item', command=self.addItem)
        self.btn3.grid(row=11, column=1, padx=5, pady=20, sticky=W)

        self.btn4 = Button(self, text='Edit Item',
                           command=self.editItem)
        self.btn4.grid(row=11, column=2, padx=5, pady=20, sticky=W)

        self.btn4 = Button(self, text='Delete Item',
                           command=self.deleteItem)
        self.btn4.grid(row=11, column=3, padx=5, pady=20, sticky=W)

        # Lines 91 - 98 inserts headers into text area and sets focus to Item Number entry box
        self.text.insert(END, 'Item Number' + '\t\t' + 'Item Name'
                         + '\t\t' + 'On Hand' + '\t\t' + 'Price'
                         + '\t\t')
        self.text.insert(END,
                         '------------------------------------------------------------'
                         )
        self.text.configure(state="disabled")
        self._input1.focus_set()

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

def main():
    InventoryManagement().mainloop()


main()




root = Tk
main_screen()


