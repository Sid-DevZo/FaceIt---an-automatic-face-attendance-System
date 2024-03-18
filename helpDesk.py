from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2

class Help:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1366x768+0+0")
        self.root.title("Face Recognition System")
        
        
        title_lbl=Label(self.root,text="HELP DESK",font=("times new roman",27,"bold"),bg="skyblue",fg="blue")
        title_lbl.place(x=0,y=0,width=1366,height=45)
        
        img1=Image.open(r"images\help2.png")
        img1=img1.resize((1366,723),Image.Resampling.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img1)
        
        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=55,width=1366,height=723)
        
        title_lbl=Label(self.root,text="Email : biswassid212@gmail.com",font=("times new roman",20,"bold"),bg="violet",fg="black")
        title_lbl.place(x=550,y=220)


if __name__ == "__main__":
    root=Tk()
    obj = Help(root)
    root.mainloop()     