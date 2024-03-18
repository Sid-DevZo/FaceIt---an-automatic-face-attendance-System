from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np 

class Train:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1366x768+0+0")
        self.root.title("Face Recognition System")
        
        title_lbl=Label(self.root,text="Train Data Set",font=("times new roman",35,"bold"),bg="white",fg="darkgreen")
        title_lbl.place(x=0,y=0,width=1366,height=45)
        
         # 1st image
        img1=Image.open(r"images\td1.png")
        img1=img1.resize((1366,335),Image.Resampling.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img1)
        
        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=45,width=1366,height=335)
        
        # 2nd image
        img2=Image.open(r"images\td2.png")
        img2=img2.resize((1366,726),Image.Resampling.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img2)
        
        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=0,y=440,width=1366,height=328)
        
         
        #  button
        
        b1_1=Button(self.root,text="TRAIN DATA",command=self.train_classifier,cursor="hand2",font=("times new roman",15,"bold"),bg="black",fg="white")
        b1_1.place(x=0,y=380,width=1366,height=60)
        
    def train_classifier(self):
        data_dir=("data")
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]
        
        
        faces=[]
        ids=[]
        
        for image in path:
            img=Image.open(image).convert('L')  # Gray Scale image
            imageNp=np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])
            
            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training",imageNp)
            cv2.waitKey(1)==13
        ids=np.array(ids)
        
        
        # =========== Train the classiifier and save =========
        
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training datasets completed !!")   


if __name__ == "__main__":
    root=Tk()
    obj = Train(root)
    root.mainloop()             
        