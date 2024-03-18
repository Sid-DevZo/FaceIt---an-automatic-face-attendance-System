from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from time import strftime
from datetime import datetime
import mysql.connector
import os
from student import Student
import cv2
from train import Train

class Face_Recognition:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1366x768+0+0")
        self.root.title("Face Recognition ")
        
        
        title_lbl=Label(self.root,text="FACE RECOGNITION",font=("times new roman",27,"bold"),bg="darkgreen",fg="white")
        title_lbl.place(x=0,y=0,width=1366,height=45)
        
          # 1st image
        img1=Image.open(r"images\face1.png")
        img1=img1.resize((683,726),Image.Resampling.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img1)
        
        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=45,width=683,height=726)
        
        # 2nd image
        img2=Image.open(r"images\face2.png")
        img2=img2.resize((683,726),Image.Resampling.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img2)
        
        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=683,y=45,width=683,height=726)
        
        
        
        # button
        b1_1=Button(f_lbl,text="Face Recognition",cursor="hand2",command=self.face_recog,font=("times new roman",10,"bold"),bg="red",fg="white")
        b1_1.place(x=248,y=540,width=200,height=50) 
        
        
        #================= Attendeance  ===================
        
    def mark_attendance(self,i,r,n,d):
        with open("Sid.csv","r+",newline="\n") as f:
            myDataList=f.readlines()
            name_list=[]
            for line in myDataList:
                Entry=line.split((","))
                name_list.append(Entry[0])
            if((i not in name_list) and (r not in name_list) and (n not in name_list) and (d not in name_list)):
                now=datetime.now()
                d1=now.strftime("%d/%m/%Y")
                dtString=now.strftime("%H:%M:%S")
                f.writelines(f"\n{i},{r},{n},{d},{dtString},{d1},Preset")            
                
                
                
    #================ face  recognition ====================== 
        
        
    def face_recog(self):
        def draw_boundary(img,classifier,scaleFactor,minNeighbours,color,text,clf):
            gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features=classifier.detectMultiScale(gray_image,scaleFactor,minNeighbours)
            
            
            coord=[]
            
            for (x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                id,predict=clf.predict(gray_image[y:y+h,x:x+w])
                confidence=int((100*(1-predict/300))) 
                
                conn=mysql.connector.connect(host="localhost",username="root",password="12345",database="face_recogniser")
                my_cursor=conn.cursor() 
                
                my_cursor.execute("select Name from student where StudentID="+str(id))
                n=my_cursor.fetchone()
                n="+".join(n)
                
                my_cursor.execute("select Roll from student where StudentID="+str(id))
                r=my_cursor.fetchone()
                r="+".join(r)
                
                my_cursor.execute("select Department from student where StudentID="+str(id))
                d=my_cursor.fetchone()
                d="+".join(d)
                
                
                my_cursor.execute("select StudentID from student where StudentID="+str(id))
                i=my_cursor.fetchone()
                i="+".join(i)
                
        
                
                if confidence>77:
                    cv2.putText(img,f"ID:{i}",(x,y-75),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Roll:{r}",(x,y-40),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Department:{d}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    self.mark_attendance(i,r,n,d)   
                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(img,"Unknown Face",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    
                coord=[x,y,w,h]
                
            return coord
        
        
        def recognize(img,clf,faceCascade):
            coord=draw_boundary(img,faceCascade,1.1,10,(255,25,255),"Face",clf)
            return img
        
        faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")
        
        
        video_cap=cv2.VideoCapture(0)
        
        while True:
            ret,img=video_cap.read()
            img=recognize(img,clf,faceCascade)
            cv2.imshow("Welcome TO Face Recognizer",img)
            
            if cv2.waitKey(1)==13:
                break
        video_cap.release()
        cv2.destroyAllWindows()    
        
    

if __name__ == "__main__":
    root=Tk()
    obj = Face_Recognition(root)
    root.mainloop()             