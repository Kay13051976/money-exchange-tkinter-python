from tkinter import *
from tkinter import ttk
root = Tk()
root.title("Money Exchange")
root.geometry("450x350+600+500")


money = IntVar()
Label(text="Currency From BTH",padx=10,font=30).grid(row=0,sticky=W)
et1=Entry(font = 30,width=30,textvariable=money)
et1.grid(row=0,column=1)

choice = StringVar(value="Select Currency")
Label(text="Currency To",padx=10,font=30).grid(row=1,sticky=W)
combo=ttk.Combobox(width=30,font=30,textvariable=choice)
combo["value"]=("EUR","JPY","USD","GBP")
combo.grid(row=1,column=1)

# output

Label(text="Amount",padx=10,font=30).grid(row=2,sticky=W)
et2=Entry(font = 30,width=30)
et2.grid(row=2,column=1)

def calculate():
    amount=money.get()
    currency=choice.get()

    if currency == "EUR":
        et2.delete(0,END)
        result = ((amount*0.026),"EUR")
        et2.insert(0,result)
    elif currency == "JPY":
         result = ((amount*3,486),"JPY")
         et2.insert(0,result)
    elif currency == "USD":
         result = ((amount*0.031),"USD")
         et2.insert(0,result)
    elif currency == "GBP":
         result = ((amount*0.023),"GBP")
         et2.insert(0,result)
    else:
        et2.delete(0,END)
        result = "Error"
        et2.insert(0,result)

def deleteText():
    et1.delete(0,END)
    et2.delete(0,END)

     
        
Button(text="Calculate",font="30",width=15,command=calculate).grid(row=3,column=1,sticky=W)
Button(text="Clear",font=30,width="15",command=deleteText).grid(row=3,column=1,sticky=E)
root.mainloop()