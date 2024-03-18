from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
import tkinter 
import os
from student import Student
from train import Train
from face_recognition import Face_Recognition
from attendance import Attendance
from helpDesk import Help

class Face_Recognition_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")
        
        
        img=Image.open(r"images\attendance.png")
        img=img.resize((1530,790),Image.Resampling.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)
        
        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=1530,height=790)
        
        title_lbl=Label(f_lbl,text="FACE RECOGNITION ATTENDANCE SYSTEM",font=("times new roman",27,"italic"),bg="white",fg="blue")
        title_lbl.place(x=0,y=0,width=1530,height=42)
        
        # Student Button

        img1=Image.open(r"images\std_dbs.png")  
        img1=img1.resize((180,180),Image.Resampling.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        
        b1_1=Button(f_lbl,image=self.photoimg1,command=self.student_details,cursor="hand2")
        b1_1.place(x=200,y=300,width=180,height=180)
        
        b1_1=Button(f_lbl,text="Student Details",command=self.student_details,cursor="hand2",font=("times new roman",10,"bold"),bg="black",fg="white")
        b1_1.place(x=200,y=300,width=180,height=40)      
      
      
        # Detector Button

        img2=Image.open(r"images\atd_sys.png")  
        img2=img2.resize((180,180),Image.Resampling.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        
        b1_1=Button(f_lbl,image=self.photoimg2,cursor="hand2",command=self.face_data)
        b1_1.place(x=400,y=300,width=180,height=180)
        
        b1_1=Button(f_lbl,text="Face Detector",cursor="hand2",command=self.face_data,font=("times new roman",10,"bold"),bg="black",fg="white")
        b1_1.place(x=400,y=300,width=180,height=40)      
      
      
        # Attendance Button

        img3=Image.open(r"images\atd.png")  
        img3=img3.resize((180,180),Image.Resampling.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        
        b1_1=Button(f_lbl,image=self.photoimg3,cursor="hand2",command=self.attendance_data)
        b1_1.place(x=600,y=300,width=180,height=180)
        
        b1_1=Button(f_lbl,text="Attendance",cursor="hand2",command=self.attendance_data,font=("times new roman",10,"bold"),bg="black",fg="white")
        b1_1.place(x=600,y=300,width=180,height=40)      
      
      
        # Help DEsk Button

        img4=Image.open(r"images\helpdesk.png")  
        img4=img4.resize((180,180),Image.Resampling.LANCZOS)
        self.photoimg4=ImageTk.PhotoImage(img4)
        
        b1_1=Button(f_lbl,image=self.photoimg4,cursor="hand2",command=self.help_data)
        b1_1.place(x=800,y=300,width=180,height=180)
        
        b1_1=Button(f_lbl,text="Help Desk",cursor="hand2",command=self.help_data,font=("times new roman",10,"bold"),bg="black",fg="white")
        b1_1.place(x=800,y=300,width=180,height=40)      
      
      
        # Train data Button

        img5=Image.open(r"images\traindata.png")  
        img5=img5.resize((180,180),Image.Resampling.LANCZOS)
        self.photoimg5=ImageTk.PhotoImage(img5)
        
        b1_1=Button(f_lbl,image=self.photoimg5,cursor="hand2",command=self.train_data)
        b1_1.place(x=1000,y=300,width=180,height=180)
        
        b1_1=Button(f_lbl,text="Train Data",cursor="hand2",command=self.train_data,font=("times new roman",10,"bold"),bg="black",fg="white")
        b1_1.place(x=1000,y=300,width=180,height=40)      
      
      
       # Developer Button

        img6=Image.open(r"images\developer.png")  
        img6=img6.resize((380,150),Image.Resampling.LANCZOS)
        self.photoimg6=ImageTk.PhotoImage(img6)
        
        b1_1=Button(f_lbl,image=self.photoimg6,cursor="hand2")
        b1_1.place(x=200,y=500,width=380,height=180)
        
        b1_1=Button(f_lbl,text="Developer",cursor="hand2",font=("times new roman",10,"bold"),bg="black",fg="white")
        b1_1.place(x=200,y=500,width=380,height=40)      
      
      
        # photos Button

        img7=Image.open(r"images\photos.png")  
        img7=img7.resize((380,180),Image.Resampling.LANCZOS)
        self.photoimg7=ImageTk.PhotoImage(img7)
        
        b1_1=Button(f_lbl,image=self.photoimg7,cursor="hand2",command=self.open_img)
        b1_1.place(x=600,y=500,width=380,height=180)
        
        b1_1=Button(f_lbl,text="Photos",cursor="hand2",command=self.open_img,font=("times new roman",10,"bold"),bg="black",fg="white")
        b1_1.place(x=600,y=500,width=380,height=40)      
      
      
        # Exit Button

        img8=Image.open(r"images\exit.png")  
        img8=img8.resize((180,180),Image.Resampling.LANCZOS)
        self.photoimg8=ImageTk.PhotoImage(img8)
        
        b1_1=Button(f_lbl,image=self.photoimg8,cursor="hand2",command=self.iExit)
        b1_1.place(x=1000,y=500,width=180,height=180)
        
        b1_1=Button(f_lbl,text="Exit",cursor="hand2",command=self.iExit,font=("times new roman",10,"bold"),bg="black",fg="white")
        b1_1.place(x=1000,y=500,width=180,height=40) 
        
        
    def open_img(self):
        os.startfile("data")    
        
    def iExit(self):
        self.iExit=tkinter.messagebox.askyesno("Face Recognition","Are you sure want to exit ",parent=self.root) 
        if self.iExit>0:
            self.root.destroy()
        else:
            return    
               
        
    #  =================Functions Buttons======================
        
    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)     
      
    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)    
        
    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition(self.new_window)
        
    def attendance_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window)
        
    def help_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Help(self.new_window)    
                 
             
        
        
      
if __name__ == "__main__":
    root=Tk()
    obj = Face_Recognition_System(root)
    root.mainloop()     