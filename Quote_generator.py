from tkinter import *
import requests
import random
from PIL import Image,ImageTk

class sample_quote:

    def __init__(self,master):

        self.master=master
        self.master.title("Quote Generator")
        self.master.geometry("1000x600")
        img=ImageTk.PhotoImage(Image.open("logo.png"))
        self.master.imlab=Label(self.master,image=img)
        self.master.imlab.pack()
        self.quote_label=Label(self.master,wraplength=800,font=("Courier New",14))
        self.quote_label.configure(text="")
        self.quote_label.pack(ipadx=20,ipady=20,padx=20,pady=20)

        self.generate_quote_button=Button(self.master,text='Generate!',command=self.generate,width=30,font=("Courier New",14),bg="#0c20f7",activebackground="#2839f7",fg="white",activeforeground="white")
        self.generate_quote_button.pack()
        self.master.mainloop()

    def generate(self):
        self.quote_label.configure(text="")
        quote_json=requests.get("http://api.quotable.io/random").json()
        quote="{}\n\nBy: {}".format(quote_json['content'],quote_json['author'])
        self.quote_label.configure(text=quote)

    
if __name__=="__main__":
    root=Tk()
    app=sample_quote(root)
