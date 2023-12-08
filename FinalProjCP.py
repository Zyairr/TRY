from tkinter import *
from tkinter import messagebox
import os
from datetime import datetime

root=Tk()
root.title("bsushop.in")
root.geometry("1360x1000")
Heading=LabelFrame(root,bd=2,relief="groove",bg="light yellow")
Heading.place(x=0,y=0,width=1380,height=55)
image_logo=PhotoImage(file = "bsu logo.png")
image_logo_1=PhotoImage(image_logo)


polo_image=PhotoImage(file = "polo.png")
blouse_image=PhotoImage(file = "blouse.png")

pants_image=PhotoImage(file = "pants.png")
skirt_image=PhotoImage(file = "skirt.png")

tumbler_1_image=PhotoImage(file = "tumbler_1.png")
tumbler_2_image=PhotoImage(file = "tumbler_2.png")
tumbler_3_image=PhotoImage(file = "tumbler_3.png")

#Tops Variables
clicked_polo=StringVar()
clicked_polo.set("Php.200")
clicked_blouse=StringVar()
clicked_blouse.set("Php.250")
tops_list=[]
#bottoms Variables
clicked_pants=StringVar()
clicked_pants.set("Php.180")
clicked_skirt=StringVar()
clicked_skirt.set("Php.150")
bottoms_list=[]
#Collections Variables
clicked_tumbler_1=StringVar()
clicked_tumbler_1.set("Php.80")
clicked_tumbler_2=StringVar()
clicked_tumbler_2.set("Php.50")
clicked_tumbler_3=StringVar()
clicked_tumbler_3.set("Php.120")
collections_list=[]

name=Label(Heading,text="BSU Shop",font="arial 20 bold italic",bg="red",fg="black").grid(row=0,column=1)
tagline=Label(Heading,text="Shopping made easier!",font="magneto 16 italic",fg="white",bg="maroon").grid(row=0,column=2,padx=280)
Products_frame=LabelFrame(root,bd=2,relief="groove",text="Products",font="arial 16 bold",fg="dark blue")
Products_frame.place(x=310,y=60,width=1040,height=620)
label_logo=Label(Products_frame,image=image_logo,bd=2).place(x=250,y=100)
label_enjoy=Label(Products_frame,text="Enjoy Shopping",font="castellar 20 bold").place(x=370,y=370)
Button_frame=LabelFrame(root,bd=2,relief="groove")
Button_frame.place(x=2,y=60,width=300,height=380)
def save_invoice(text):
    op=messagebox.askyesno("Invoice Saving Confirmation","Do you want to save the invoice in a file?")
    if op:
        t=datetime.now()
        s=str(t.day)+str(t.month)+str(t.year)+str(t.hour)+str(t.minute)+str(t.second)
        f=open("Invoices/"+s+".txt","w")
        f.write(text)
        f.close()
        messagebox.showinfo("Invoice Saving Status","Invoice is saved successfully as a text document with name "+s+".txt")
    else:
        messagebox.showinfo("Invoice Saving Status","The invoice is not saved into a file.")
def HideAllFrames():
    for widget in Products_frame.winfo_children():
        widget.destroy()
def Spaces(n,s1=" "):
    s=""
    for i in range(n):
        s+=s1
    return s
def TopsCall():
    HideAllFrames()
    Tops_Label=Label(Products_frame,text="Tops",font="times 15 bold",fg="black",bg="beige").grid(row=0,column=0,padx=20)
    lf_polo=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_polo.place(x=5,y=35,width=180,height=280)
    lf_blouse=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_blouse.place(x=210,y=35,width=180,height=280)
    label_polo=Label(lf_polo,image=polo_image,bd=2).grid(row=0,column=0)
    label_blouse=Label(lf_blouse,image=blouse_image,bd=2).place(x=5, y=248)
    name_polo=Label(lf_polo,text="Polo",font="arial 9").place(x=5, y=248)
    name_blouse=Label(lf_blouse,text="Blouse",font="arial 9",justify="center").place(x=5, y=248)
    label_qty_polo=Label(lf_polo,text="Size:",bd=1,font="arial 9",justify="left").place(x=5,y=218)
    label_qty_blouse=Label(lf_blouse,text="Size:",bd=1,font="arial 9",justify="left").place(x=5,y=218)
    options_polo=["Small - Php.200", "Medium - Php.250"]
    options_blouse=["Small - Php.250","Medium - Php.300"]
    global clicked_polo,clicked_blouse,tops_list
    drop_polo=OptionMenu(lf_polo, clicked_polo, *options_polo).place(x=48, y=212)
    drop_blouse=OptionMenu(lf_blouse,clicked_blouse,*options_blouse).place(x=48,y=212)
    def TopsPrice(s):
        s1=""
        for i in range(len(s)-1,0,-1):
            if s[i]!='.':
                s1=s1+s[i]
            else:
                break
        return int(s1[::-1])
    def TopsQty(s):
        s1=""
        for i in range(len(s)):
            s1=s1+s[i]
            if s[i]=='S' or s[i]=='M':
                break
        return s1
    def AddG1():
        global tops_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            tops_list.append(["Polo", TopsPrice(clicked_polo.get()), TopsQty(clicked_polo.get()), Spaces(40 - len("Polo"))])
            messagebox.showinfo("Product Status","Polo ("+clicked_polo.get()+") is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","Polo ("+clicked_polo.get()+") is not added to the cart.")
    def AddG2():
        global tops_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            tops_list.append(["Blouse", TopsPrice(clicked_blouse.get()),
                                 TopsQty(clicked_blouse.get()), Spaces(40 - len("Blouse"))])
            messagebox.showinfo("Product Status","Blouse ("+clicked_blouse.get()+") is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","Blouse ("+clicked_blouse.get()+") is not added to the cart.")
    add_polo=Button(lf_polo, text="Add Item", bg="green", fg="white", font="times 9 bold", command=AddG1).place(x=60, y=245)
    add_blouse=Button(lf_blouse, text="Add Item", bg="green", fg="white", font="times 9 bold", command=AddG2).place(x=60, y=245)
    
def BottomsCall():
    HideAllFrames()
    Pants_Label=Label(Products_frame, text="Bottoms", font="times 15 bold", fg="black", bg="beige").grid(row=0, column=0, padx=10)
    lf_pants=LabelFrame(Products_frame, bd=2, relief="groove")
    lf_pants.place(x=5, y=35, width=200, height=280)
    lf_skirt=LabelFrame(Products_frame, bd=2, relief="groove")
    lf_skirt.place(x=210, y=35, width=200, height=280)
    label_pants=Label(lf_pants, image=pants_image, bd=2, justify="center").grid(row=0, column=0)
    label_skirt=Label(lf_skirt, image=skirt_image, bd=2, justify="center").grid(row=0, column=0)
    name_pants=Label(lf_pants, text="Pants", font="arial 9", justify="center").place(x=5, y=248)
    name_skirt=Label(lf_skirt, text="Skirt", font="arial 9", justify="center").place(x=5, y=248)
    label_clr_pants=Label(lf_pants, text="Size:", bd=1, font="arial 9", justify="left").place(x=5, y=218)
    label_clr_skirt=Label(lf_skirt, text="Size:", bd=1, font="arial 9", justify="left").place(x=5, y=218)
    options_pants=["Small - Php.180", "Medium - Php.200"]
    options_skirt=["Small - Php.150", "Medium - Php.180"]
    global clicked_pants,clicked_blouse,bottoms_list
    drop_pants=OptionMenu(lf_pants, clicked_pants, *options_pants).place(x=48, y=212)
    drop_skirt=OptionMenu(lf_skirt, clicked_skirt, *options_skirt).place(x=48, y=212)
    def AddE1():
        global bottoms_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            bottoms_list.append(["Pants","",clicked_pants.get(),Spaces(40-len("Pants"))])
            messagebox.showinfo("Product Status","Pants ("+clicked_pants.get()+") is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","Pants ("+clicked_pants.get()+") is not added to the cart.")
    def AddE2():
        global bottoms_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            bottoms_list.append(["Skirt","",clicked_skirt.get(),Spaces(40-len("Skirt"))])
            messagebox.showinfo("Product Status","Skirt ("+clicked_skirt.get()+") is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","Skirt ("+clicked_skirt.get()+") is not added to the cart.")
    add_pants=Button(lf_pants, text="Add Item", bg="green", fg="white", font="times 9 bold", command=AddE1).place(x=60, y=245)
    add_skirt=Button(lf_skirt, text="Add Item", bg="green", fg="white", font="times 9 bold", command=AddE2).place(x=60, y=245)

def CollectionsCall():
    HideAllFrames()
    Collections_Label=Label(Products_frame, text="Collections", font="times 15 bold", fg="black", bg="beige").grid(row=0, column=0, padx=10)
    lf_tumbler_1=LabelFrame(Products_frame, bd=2, relief="groove")
    lf_tumbler_1.place(x=5, y=35, width=200, height=280)
    lf_tumbler_2=LabelFrame(Products_frame, bd=2, relief="groove")
    lf_tumbler_2.place(x=210, y=35, width=200, height=280)
    lf_tumbler_3=LabelFrame(Products_frame, bd=2, relief="groove")
    lf_tumbler_3.place(x=415, y=35, width=200, height=280)
    label_tumbler_1=Label(lf_tumbler_1, image=tumbler_1_image, bd=2, justify="center").grid(row=0, column=0)
    label_tumbler_2=Label(lf_tumbler_2, image=tumbler_2_image, bd=2, justify="center").grid(row=0, column=0, padx=7)
    label_tumbler_3=Label(lf_tumbler_3, image=tumbler_3_image, bd=2, justify="center").grid(row=0, column=0)
    name_tumbler_1=Label(lf_tumbler_1, text="White Tumbler", font="arial 9", justify="center").place(x=5,y=248)
    name_tumbler_2=Label(lf_tumbler_2, text="Mug", font="arial 9", justify="center").place(x=5, y=248)
    name_tumbler_3=Label(lf_tumbler_3, text="Black Tumbler", font="arial 9", justify="center").place(x=5, y=248)
    price_tumbler_1=Label(lf_tumbler_1, text="Price: Php.120", font="arial 9 bold").place(x=5, y=218)
    price_tumbler_2=Label(lf_tumbler_2, text="Price: Php.50", font="arial 9 bold").place(x=5, y=218)
    price_tumbler_3=Label(lf_tumbler_3, text="Price: Php.120", font="arial 9 bold").place(x=5, y=218)
    def AddC1():
        global collections_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            collections_list.append(["White Tumbler",Spaces(40-len("White Tumbler"))])
            messagebox.showinfo("Product Status","White Tumbler is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","White Tumbler is not added to the cart.")
    def AddC2():
        global collections_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            collections_list.append(["Mug",160,"160",Spaces(40-len("Mug"))])
            messagebox.showinfo("Product Status","Mug is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","Mug is not added to the cart.")
    def AddC3():
        global collections_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            collections_list.append(["Black Tumbler",550,"550",Spaces(40-len("Black Tumbler"))])
            messagebox.showinfo("Product Status","Black Tumbler is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status"," Black Tumbler is not added to the cart.")

    add_tumbler_1=Button(lf_tumbler_1, text="Add Item", bg="green", fg="white", font="times 9 bold", command=AddC1).place(x=98, y=245)
    add_tumbler_2=Button(lf_tumbler_2, text="Add Item", bg="green", fg="white", font="times 9 bold", command=AddC2).place(x=68, y=245)
    add_tumbler_3=Button(lf_tumbler_3, text="Add Item", bg="green", fg="white", font="times 9 bold", command=AddC3).place(x=98, y=245)

Tops_button=Button(Button_frame, text="Tops", font="times 20 bold", width=17, bd=6, bg="cadetblue", fg="white", activebackground="light blue", command=TopsCall)
Tops_button.grid(row=0, column=0, padx=5, pady=5)
Bottoms_button=Button(Button_frame, text="Bottoms", font="times 20 bold", width=17, bd=6, bg="cadetblue", fg="white", activebackground="light blue", command=BottomsCall)
Bottoms_button.grid(row=1, column=0, padx=5, pady=5)
Collections_button=Button(Button_frame, text="Collections", font="times 20 bold", width=17, bd=6, bg="cadetblue", fg="white", activebackground="light blue", command=CollectionsCall)
Collections_button.grid(row=2, column=0, padx=5, pady=5)

Coupon_frame=LabelFrame(root,bd=2,relief="groove",text="Vouchers!!!",fg="black",font="arial 16 bold")
Coupon_frame.place(x=2,y=450,width=300,height=230)
Coupon_1=Label(Coupon_frame,text="Get 15% Off on your purchase(upto Php.500)",font="times 12",fg="white",bg="red")
Coupon_2=Label(Coupon_frame,text="Get 10% Off on your purchase(upto Php.750)",font="times 12",fg="white",bg="red")
Coupon_3=Label(Coupon_frame,text="Get 5% Off on your purchase(upto Php.1000)",font="times 12",fg="white",bg="red")
Coupon_1.grid(row=0,column=0,padx=10,pady=17)
Coupon_2.grid(row=1,column=0,padx=10,pady=17)
Coupon_3.grid(row=2,column=0,padx=10,pady=17)
def Bill():
    op=messagebox.askyesno("Bill Generation Confirmation","Products cannot be added or removed during bill generation. Are you sure that you have finished shopping?")
    if op:
        Products_frame.destroy()
        Button_frame.destroy()
        Coupon_frame.destroy()
        bill_gen_button.destroy()
        tops_price=0
        bottoms_price=0
        collections_price=0
        for i in range(len(tops_list)):
            tops_price+= tops_list[i][1]
        for i in range(len(bottoms_list)):
            bottoms_price+= bottoms_list[i][1]
        for i in range(len(collections_list)):
            collections_price+= collections_list[i][1]
        total_price=tops_price+bottoms_price+collections_price
        discount=[0,0,0]
        if 0.15*total_price<500:
            discount[0]=0.15*total_price
        else:
            discount[0]=500
        if 0.1*total_price<750:
            discount[1]=0.1*total_price
        else:
            discount[1]=750
        if 0.05*total_price<1000:
            discount[2]=0.05*total_price
        else:
            discount[2]=1000
        max_discount=max(discount)
        if max_discount==discount[0]:
            suggest=Label(root,bd=1,text="Suggested : 15% Off upto Php.500",font="times 12",fg="blue").place(x=545,y=480)
        elif max_discount==discount[1]:
            suggest=Label(root,bd=1,text="Suggested : 10% Off upto Php.750",font="times 12",fg="blue").place(x=545,y=480)
        else:
            suggest=Label(root,bd=1,text="Suggested : 5% Off upto Php.1000",font="times 12",fg="blue").place(x=545,y=480)
        def GenBill(d,choice):
            bill_area=LabelFrame(root,bd=2,relief="groove")
            bill_area.place(x=305,y=80,width=750,height=600)
            bill_title=Label(bill_area,text="INVOICE",font="arial 15 bold",bd=4,relief="groove").pack(fill=X)
            scroll_y=Scrollbar(bill_area,orient=VERTICAL)
            bill_txt_area=Text(bill_area,yscrollcommand=scroll_y.set)
            scroll_y.pack(side=RIGHT,fill=Y)
            scroll_y.config(command=bill_txt_area.yview)
            bill_txt_area.pack(fill=BOTH,expand=1)
            bill_txt_area.insert(END,Spaces(40)+"BSU Shop\n"+Spaces(90,'*')+"\n")
            if len(tops_list)>0:
                bill_txt_area.insert(END,"TOPS Product(s)\n\nProduct Name"+Spaces(28)+"Price"+Spaces(25)+"Quantity\n")
                for i in tops_list:
                    bill_txt_area.insert(END,i[0]+i[3]+"Php."+str(i[1])+Spaces(27-len(str(i[1])))+i[2]+"\n")
                bill_txt_area.insert(END,"\nTotal Tops Price : Php."+str(tops_price)+"\n"+Spaces(90,'*')+"\n")
            if len(bottoms_list)>0:
                bill_txt_area.insert(END,"Bottoms Product(s)\n\nProduct Name"+Spaces(28)+"Price"+Spaces(25)+"Colour\n")
                for i in bottoms_list:
                    bill_txt_area.insert(END,i[0]+i[4]+"Php."+i[2]+Spaces(27-len(i[2]))+i[3]+"\n")
                bill_txt_area.insert(END,"\nTotal Bottoms Price : Php."+str(bottoms_price)+"\n"+Spaces(90,'*')+"\n")
            if len(collections_list)>0:
                bill_txt_area.insert(END,"Collections(s)\n\nProduct Name"+Spaces(28)+"Price\n")
                for i in collections_list:
                    bill_txt_area.insert(END,i[0]+i[3]+"Php."+i[2]+"\n")
                bill_txt_area.insert(END,"\nTotal Collections Price : Php."+str(collections_price)+"\n"+Spaces(90,'*')+"\n")
            if choice==1:
                bill_txt_area.insert(END,"\nCoupon Applied : 15% Off upto Php.500")
            elif choice==2:
                bill_txt_area.insert(END,"\nCoupon Applied : 10% Off upto Php.750")
            else:
                bill_txt_area.insert(END,"\nCoupon Applied : 5% Off upto Php.1000")
            bill_txt_area.insert(END,"\nDiscount Offered : Php."+str(d))
            bill_txt_area.insert(END,"\nTotal Price(after discount) = Php."+str(total_price-d))
            save_button=Button(root,text="Save Invoice",font="times 20 bold",bd=6,bg="skyblue",width=10,fg="white",command=lambda:save_invoice(bill_txt_area.get("1.0",END)))
            save_button.place(x=1120,y=600)
            
        Coupon_frame_2=LabelFrame(root,bd=2,relief="groove",text="Apply a Coupon",fg="green",font="arial 16 bold").place(x=500,y=150,width=380,height=300)
        Coupon_apply1=Button(Coupon_frame_2,text="15% Off upto Php.500",font="times 20 bold",width=17,bd=6,bg="cadetblue",fg="white",activebackground="light blue",command=lambda:GenBill(discount[0],1))
        Coupon_apply1.place(x=540,y=190)
        Coupon_apply2=Button(Coupon_frame_2,text="10% Off upto Php.750",font="times 20 bold",width=17,bd=6,bg="cadetblue",fg="white",activebackground="light blue",command=lambda:GenBill(discount[1],2))
        Coupon_apply2.place(x=540,y=280)
        Coupon_apply3=Button(Coupon_frame_2,text="5% Off upto Php.1000",font="times 20 bold",width=17,bd=6,bg="cadetblue",fg="white",activebackground="light blue",command=lambda:GenBill(discount[2],3))
        Coupon_apply3.place(x=540,y=370)
    else:
        messagebox.showinfo("Bill Generation Confirmation","You can continue shopping now.")
bill_gen_button=Button(Heading,bd=4,text="Proceed to Checkout",font="times 17 bold",bg="skyblue",fg="white",activebackground="purple",command=Bill)
bill_gen_button.grid(row=0,column=3)
root.mainloop()
        
        