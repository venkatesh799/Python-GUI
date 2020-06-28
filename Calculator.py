import tkinter as tk
window=tk.Tk()
#window.geometry("400x600")
window.title("Calculator")
window.configure(bg="#4097DE")
ans=tk.Entry(master=window,width=20,borderwidth=5,font=('Helvetica',10,"bold"))
ans.grid(row=0,column=0,columnspan=2,pady=5,padx=0)

def button_clicked(number):
    ans.insert(tk.END,number)

def calculate():
    try:
        temp=eval(ans.get())
        ans.delete(0,tk.END)
        ans.insert(0,temp)
    except:
        ans.delete(0,tk.END)
        ans.insert(0,"ERROR")
    
def clear():
    ans.delete(0,tk.END)
def delete_one():
    ans.delete(len(ans.get())-1,tk.END)
back=tk.Button(master=window,text="⌫",height=3,width=5,command=delete_one,fg="black",font=("Helvetica",12,"bold"))
back.grid(row=0,column=2,padx=5,pady=5)

button1=tk.Button(master=window,text="1",height=3,width=5,command=lambda:button_clicked("1"),bg="white",fg="black",font=("Helvetica",12,"bold"))
button1.grid(row=1,column=0,padx=2,pady=2,sticky="nsew")

button2=tk.Button(master=window,text="2",height=3,width=5,command=lambda:button_clicked("2"),bg="white",fg="black",font=("Helvetica",12,"bold"))
button2.grid(row=1,column=1,padx=2,pady=2,sticky="nsew")

button3=tk.Button(master=window,text="3",height=3,width=5,command=lambda:button_clicked("3"),bg="white",fg="black",font=("Helvetica",12,"bold"))
button3.grid(row=1,column=2,padx=2,pady=2,sticky="nsew")

button4=tk.Button(master=window,text="4",height=3,width=5,command=lambda:button_clicked("4"),bg="white",fg="black",font=("Helvetica",12,"bold"))
button4.grid(row=2,column=0,padx=2,pady=2,sticky="nsew")

button5=tk.Button(master=window,text="5",height=3,width=5,command=lambda:button_clicked("5"),bg="white",fg="black",font=("Helvetica",12,"bold"))
button5.grid(row=2,column=1,padx=2,pady=2,sticky="nsew")

button6=tk.Button(master=window,text="6",height=3,width=5,command=lambda:button_clicked("6"),bg="white",fg="black",font=("Helvetica",12,"bold"))
button6.grid(row=2,column=2,padx=2,pady=2,sticky="nsew")

button7=tk.Button(master=window,text="7",height=3,width=5,command=lambda:button_clicked("7"),bg="white",fg="black",font=("Helvetica",12,"bold"))
button7.grid(row=3,column=0,padx=2,pady=2,sticky="nsew")

button8=tk.Button(master=window,text="8",height=3,width=5,command=lambda:button_clicked("8"),bg="white",fg="black",font=("Helvetica",12,"bold"))
button8.grid(row=3,column=1,padx=2,pady=2,sticky="nsew")

button9=tk.Button(master=window,text="9",height=3,width=5,command=lambda:button_clicked("9"),bg="white",fg="black",font=("Helvetica",12,"bold"))
button9.grid(row=3,column=2,padx=2,pady=2,sticky="nsew")

button0=tk.Button(master=window,text="0",height=3,width=5,command=lambda:button_clicked("0"),bg="white",fg="black",font=("Helvetica",12,"bold"))
button0.grid(row=4,column=0,padx=2,pady=2,sticky="nsew")


minus=tk.Button(master=window,text="-",height=3,width=5,command=lambda:button_clicked("-"),bg="white",fg="black",font=("Helvetica",12,"bold"))
minus.grid(row=4,column=1,padx=2,pady=2,sticky="nsew")

divide=tk.Button(master=window,text="/",height=3,width=5,command=lambda:button_clicked("/"),bg="white",fg="black",font=("Helvetica",12,"bold"))
divide.grid(row=4,column=2,padx=2,pady=2,sticky="nsew")


equal=tk.Button(master=window,text="=",height=3,width=5,command=lambda:calculate(),bg="white",fg="black",font=("Helvetica",12,"bold"))
equal.grid(row=5,column=0,padx=2,pady=2,sticky="nsew")

multiplication=tk.Button(master=window,text="*",height=3,width=5,command=lambda:button_clicked("*"),bg="white",fg="black",font=("Helvetica",13,"bold"))
multiplication.grid(row=5,column=1,padx=2,pady=2,sticky="nsew")

plus=tk.Button(master=window,text="+",height=3,width=5,command=lambda:button_clicked("+"),bg="white",fg="black",font=("Helvetica",12,"bold"))
plus.grid(row=5,column=2,rowspan=2,padx=2,pady=2,sticky="nsew")

clear=tk.Button(master=window,text="C",height=3,width=5,command=clear,bg="white",fg="black",font=("Helvetica",12,"bold"))
clear.grid(row=6,column=0,columnspan=2,padx=2,pady=2,sticky="nsew")