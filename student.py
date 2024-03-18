from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2

class Student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")
        
        #  ==========Variables===============
        
        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_sem=StringVar()
        self.var_id=StringVar()
        self.var_name=StringVar()
        self.var_regd=StringVar()
        self.var_roll=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_address=StringVar()
        
        img=Image.open(r"C:\Users\SIDDHARTHA\Desktop\DatabaseProject\images\black.png")
        img=img.resize((1530,790),Image.Resampling.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)
        
        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=1530,height=790)
        
        title_lbl=Label(f_lbl,text="FACE RECOGNITION ATTENDANCE SYSTEM",font=("times new roman",27,"bold"),bg="skyblue",fg="blue")
        title_lbl.place(x=0,y=0,width=1530,height=42)
        
        main_frame=Frame(f_lbl,bd=2,bg="white")
        main_frame.place(x=0,y=70,width=1366,height=600)

        # left label frame
        Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="student_details",font=("times new roman",12,"bold"))
        Left_frame.place(x=1,y=20,width=675,height=560)
        
        # current course frame
        
        current_course_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Current Course Information",font=("times new roman",12,"bold"))
        current_course_frame.place(x=3,y=150,width=670,height=110)
        
        # Department
        
        dep_label=Label(current_course_frame,text="Department",font=("times new roman",12,"bold"),bg="white")
        dep_label.grid(row=0,column=0,padx=10,sticky=W)
        
        dep_combo=ttk.Combobox(current_course_frame,textvariable=self.var_dep,font=("times new roman",9,"bold"),state="readonly")
        dep_combo["values"]=("Select Department","CSE","IT","ECE","EE","CE","AEIE")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)
        
        # course
        
        course_label=Label(current_course_frame,text="Course",font=("times new roman",12,"bold"),bg="white")
        course_label.grid(row=0,column=2,padx=10,sticky=W)
        
        course_combo=ttk.Combobox(current_course_frame,textvariable=self.var_course,font=("times new roman",9,"bold"),state="readonly")
        course_combo["values"]=("Select course","BE","ME")
        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)
        
        
         # Year
         
        yr_label=Label(current_course_frame,text="Year",font=("times new roman",12,"bold"),bg="white")
        yr_label.grid(row=1,column=0,padx=10,sticky=W)
        
        yr_combo=ttk.Combobox(current_course_frame,textvariable=self.var_year,font=("times new roman",9,"bold"),state="readonly")
        yr_combo["values"]=("Select Year","1st","2nd","3rd","4th")
        yr_combo.current(0)
        yr_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)
        
        # Semester
         
        sem_label=Label(current_course_frame,text="Semester",font=("times new roman",12,"bold"),bg="white")
        sem_label.grid(row=1,column=2,padx=10,sticky=W)
        
        sem_combo=ttk.Combobox(current_course_frame,textvariable=self.var_sem,font=("times new roman",9,"bold"),state="readonly")
        sem_combo["values"]=("Select Semester","1st","2nd","3rd","4th","5th","6th","7th","8th")
        dep_combo.current(0)
        sem_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)
        
        
        # class student information
        
        class_student_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Class Student Information",font=("times new roman",12,"bold"))
        class_student_frame.place(x=3,y=260,width=670,height=315)
        
        # student ID
        studentID_label=Label(class_student_frame,text="Student ID",font=("times new roman",12,"bold"),bg="white")
        studentID_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)
        
        studentID_entry=ttk.Entry(class_student_frame,textvariable=self.var_id,width=20,font=("times new roman",9,"bold"))
        studentID_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)
        
        # student Name
        student_name_label=Label(class_student_frame,text="Student Name",font=("times new roman",12,"bold"),bg="white")
        student_name_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)
        
        student_name_entry=ttk.Entry(class_student_frame,textvariable=self.var_name,width=20,font=("times new roman",9,"bold"))
        student_name_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)
        
          # Registration number
        Regd_label=Label(class_student_frame,text="Registration",font=("times new roman",12,"bold"),bg="white")
        Regd_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)
        
        Regd_entry=ttk.Entry(class_student_frame,textvariable=self.var_regd,width=20,font=("times new roman",9,"bold"))
        Regd_entry.grid(row=1,column=1,padx=10,pady=5,sticky=W)
        
        
          # Roll Number
        roll_label=Label(class_student_frame,text="Roll No.",font=("times new roman",12,"bold"),bg="white")
        roll_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)
        
        roll_entry=ttk.Entry(class_student_frame,textvariable=self.var_roll,width=20,font=("times new roman",9,"bold"))
        roll_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)
        
          # Gender
        gender_name_label=Label(class_student_frame,text="Gender",font=("times new roman",12,"bold"),bg="white")
        gender_name_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)
        
        gender_combo=ttk.Combobox(class_student_frame,textvariable=self.var_gender,font=("times new roman",9,"bold"),state="readonly")
        gender_combo["values"]=("Select Gender","Male","Female","Others")
        gender_combo.current(0)
        gender_combo.grid(row=2,column=1,padx=2,pady=10,sticky=W)
        
          # Date of Birth
        student_name_label=Label(class_student_frame,text="Date of Birth",font=("times new roman",12,"bold"),bg="white")
        student_name_label.grid(row=2,column=2,padx=10,pady=5,sticky=W)
        
        student_name_entry=ttk.Entry(class_student_frame,textvariable=self.var_dob,width=20,font=("times new roman",9,"bold"))
        student_name_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)
        
          # Phone number
        student_name_label=Label(class_student_frame,text="Phone Number",font=("times new roman",12,"bold"),bg="white")
        student_name_label.grid(row=3,column=0,padx=10,pady=5,sticky=W)
        
        student_name_entry=ttk.Entry(class_student_frame,textvariable=self.var_phone,width=20,font=("times new roman",9,"bold"))
        student_name_entry.grid(row=3,column=1,padx=10,pady=5,sticky=W)
        
          # Email
        student_name_label=Label(class_student_frame,text="Email",font=("times new roman",12,"bold"),bg="white")
        student_name_label.grid(row=3,column=2,padx=10,pady=5,sticky=W)
        
        student_name_entry=ttk.Entry(class_student_frame,textvariable=self.var_email,width=20,font=("times new roman",9,"bold"))
        student_name_entry.grid(row=3,column=3,padx=10,pady=5,sticky=W)
        
          # Address
        student_name_label=Label(class_student_frame,text="Address",font=("times new roman",12,"bold"),bg="white")
        student_name_label.grid(row=4,column=0,padx=10,pady=5,sticky=W)
        
        student_name_entry=ttk.Entry(class_student_frame,textvariable=self.var_address,width=20,font=("times new roman",9,"bold"))
        student_name_entry.grid(row=4,column=1,padx=10,pady=5,sticky=W)
        
                
        
        
          # radio button
        self.var_radiobtn1=StringVar()
        radiobtn1 = ttk.Radiobutton(class_student_frame,variable=self.var_radiobtn1,text="Take Photo Sample",value="Yes")
        radiobtn1.grid(row=5,column=0)
        
      
        radiobtn2 = ttk.Radiobutton(class_student_frame,variable=self.var_radiobtn1,text="No Photo Sample",value="No")
        radiobtn2.grid(row=5,column=1)
        
        #button Frame
        
        btn_frame=Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=200,width=665,height=90)
        
        save_btn=Button(btn_frame,text="Save",command=self.add_data,width=18,font=("times new roman",12,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0)
        
        update_btn=Button(btn_frame,text="Update",width=18,command=self.update_data,font=("times new roman",12,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=1)
        
        delete_btn=Button(btn_frame,text="Delete",width=18,command=self.delete_data,font=("times new roman",12,"bold"),bg="blue",fg="white")
        delete_btn.grid(row=0,column=2)
        
        reset_btn=Button(btn_frame,text="Reset",width=18,command=self.reset_data,font=("times new roman",12,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=3)
        
        btn_frame1=Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame1.place(x=0,y=235,width=1200,height=90)
        
        take_photo_btn=Button(btn_frame1,command=self.generate_dataset,text="Take Photo",width=36,font=("times new roman",12,"bold"),bg="blue",fg="white")
        take_photo_btn.grid(row=0,column=0)
        
        update_photo_btn=Button(btn_frame1,text="Update Photo",width=36,font=("times new roman",12,"bold"),bg="blue",fg="white")
        update_photo_btn.grid(row=0,column=1)
        
        

         # right label frame
        right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="student_details",font=("times new roman",12,"bold"))
        right_frame.place(x=680,y=20,width=670,height=560)
        
        
        
        search_frame=LabelFrame(right_frame,bd=2,bg="white",relief=RIDGE,text="search system",font=("times new roman",12,"bold"))
        search_frame.place(x=5,y=150,width=660,height=110)
        
        search_label=Label(search_frame,text="search by",font=("times new roman",12,"bold"),bg="red",fg="white")
        search_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)
        
        search_combo=ttk.Combobox(search_frame,font=("times new roman",9,"bold"),state="readonly")
        search_combo["values"]=("Select","ROll_No","phone_No")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)
        
        search_entry=ttk.Entry(search_frame,width=20,font=("times new roman",9,"bold"))
        search_entry.grid(row=0,column=2,padx=10,pady=10,sticky=W)
        
        search_btn=Button(search_frame,text="search",width=13,font=("times new roman",12,"bold"),bg="blue",fg="white")
        search_btn.grid(row=0,column=3,padx=4)
        
        search_btn=Button(search_frame,text="show All",width=13,font=("times new roman",12,"bold"),bg="blue",fg="white")
        search_btn.grid(row=0,column=4,padx=4)
        
        
        table_frame=LabelFrame(right_frame,bd=2,relief=RIDGE)
        table_frame.place(x=5,y=210,width=660,height=110)
        
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
        
        self.student_table=ttk.Treeview(table_frame,column=("dep","course","year","sem","id","name","roll","gender","dob","email","phone","address","regd","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)
        
        
        self.student_table.heading("dep",text="Department")
        self.student_table.heading("course",text="Course")
        self.student_table.heading("year",text="Year")
        self.student_table.heading("sem",text="Semester")
        self.student_table.heading("id",text="StudentID")
        self.student_table.heading("name",text="Name")
        self.student_table.heading("roll",text="Roll")
        self.student_table.heading("gender",text="Gender")
        self.student_table.heading("dob",text="DOB")
        self.student_table.heading("email",text="Email")
        self.student_table.heading("phone",text="Phone")
        self.student_table.heading("address",text="Address")
        self.student_table.heading("regd",text="Registration")
        self.student_table.heading("photo",text="PhotoSampleStatus")
        self.student_table["show"]="headings"

        self.student_table.column("dep",width=100)
        self.student_table.column("course",width=100)
        self.student_table.column("year",width=100)
        self.student_table.column("sem",width=100)
        self.student_table.column("id",width=100)
        self.student_table.column("name",width=100)
        self.student_table.column("roll",width=100)
        self.student_table.column("gender",width=100)
        self.student_table.column("email",width=100)
        self.student_table.column("phone",width=100)
        self.student_table.column("address",width=100)
        self.student_table.column("regd",width=100)
        self.student_table.column("photo",width=150)
        
        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()
        
    #  Functions Buttons
        
    def add_data(self):
          if self.var_dep.get()=="Select Department" or self.var_name.get()=="" or self.var_id.get()=="":
            messagebox.showerror("Error","All Fields are required",parent=self.root)
          else:
            try:
             conn=mysql.connector.connect(host="localhost",username="root",password="12345",database="face_recogniser")
             my_cursor=conn.cursor()
             my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",( 
              
                                                                                                      
                                                                        self.var_dep.get(),
                                                                        self.var_course.get(),
                                                                        self.var_year.get(),
                                                                        self.var_sem.get(),
                                                                        self.var_id.get(),
                                                                        self.var_name.get(),
                                                                        self.var_roll.get(),
                                                                        self.var_gender.get(),
                                                                        self.var_dob.get(),
                                                                        self.var_email.get(),
                                                                        self.var_phone.get(),
                                                                        self.var_address.get(),
                                                                        self.var_regd.get(),
                                                                        self.var_radiobtn1.get()
                                                                        
                                                                     ))
                                                   
             
             conn.commit()
             self.fetch_data()
             conn.close()
             messagebox.showinfo("success","Student details has been added successfully",parent=self.root)
            except Exception as es:
              messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)
              
              # =========== fetch data ====================
              
    def  fetch_data(self):
           conn=mysql.connector.connect(host="localhost",username="root",password="12345",database="face_recogniser")
           my_cursor=conn.cursor()
           my_cursor.execute("select * from student")
           data=my_cursor.fetchall()
      
           if len(data) != 0:
             self.student_table.delete(*self.student_table.get_children())
             for i in data:
               self.student_table.insert("",END,values=i)
             conn.commit()  
           conn.close()
        
        # ======= get cursor =========
        
    def get_cursor(self,event=""):
      cursor_focus=self.student_table.focus()
      content=self.student_table.item(cursor_focus)
      data=content["values"]
      
      
      self.var_dep.set(data[0]),
      self.var_course.set(data[1]),
      self.var_year.set(data[2]),
      self.var_sem.set(data[3]),
      self.var_id.set(data[4]),
      self.var_name.set(data[5]),
      self.var_roll.set(data[6]),
      self.var_gender.set(data[7]),
      self.var_dob.set(data[8]),
      self.var_email.set(data[9]),
      self.var_phone.set(data[10]),
      self.var_address.set(data[11]),
      self.var_regd.set(data[12]),
      self.var_radiobtn1.set(data[13])
      
    # ============ update ============       
    def  update_data(self):
          if self.var_dep.get()=="Select Department" or self.var_name.get()=="" or self.var_id.get()=="":
            messagebox.showerror("Error","All Fields are required",parent=self.root)
          else:
            try:
              Update=messagebox.askyesno("Update","Do you want to update this student details",parent=self.root)
              if Update>0:
                conn=mysql.connector.connect(host="localhost",username="root",password="12345",database="face_recogniser")
                my_cursor=conn.cursor()
                my_cursor.execute("update student set Department=%s,Course=%s,Year=%s,Semester=%s,Name=%s,Roll=%s,Gender=%s,DOB=%s,Email=%s,Phone=%s,Address=%s,Registration=%s,PhotoSampleStatus=%s where StudentID=%s",(
                  
                  
                                                                        self.var_dep.get(),
                                                                        self.var_course.get(),
                                                                        self.var_year.get(),
                                                                        self.var_sem.get(),
                                                                        self.var_name.get(),
                                                                        self.var_roll.get(),
                                                                        self.var_gender.get(),
                                                                        self.var_dob.get(),
                                                                        self.var_email.get(),
                                                                        self.var_phone.get(),
                                                                        self.var_address.get(),
                                                                        self.var_regd.get(),
                                                                        self.var_radiobtn1.get(),               
                                                                        self.var_id.get()
                  
                  
                                                                          ))
                
              else:
                if not Update:
                  return
              messagebox.showinfo("Success","Student details successfully update complete",parent=self.root)
              conn.commit()
              self.fetch_data()
              conn.close()
            except Exception as es:
              messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)  
            
            # ================ delete data =========================
            
    def delete_data(self):
      if self.var_id.get()=="":
        messagebox.showerror("Error","Student id must be required",parent=self.root)
      else:
        try:
          delete=messagebox.askyesno("Student Delete Page","Do you want to delete this student",parent=self.root)
          if delete>0:
                conn=mysql.connector.connect(host="localhost",username="root",password="12345",database="face_recogniser")
                my_cursor=conn.cursor()  
                sql="delete from student where StudentID=%s"
                val=(self.var_id.get(),)
                my_cursor.execute(sql,val)
          else:
            if not delete:
              return      
          conn.commit()
          self.fetch_data()
          conn.close()
          messagebox.showinfo("Delete","Successfully deleted student details",parent=self.root)
        except Exception as es:
          messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)
      
      # =============== reset data =====================
      
    def reset_data(self):
      self.var_dep.set("Select Department")
      self.var_course.set("Select Course")
      self.var_year.set("Select Year")
      self.var_sem.set("Select Semester")
      self.var_id.set("")
      self.var_name.set("")
      self.var_roll.set("")
      self.var_gender.set("Male")
      self.var_dob.set("")
      self.var_email.set("")
      self.var_phone.set("")
      self.var_address.set("")
      self.var_regd.set("")
      self.var_radiobtn1.set("")
      
      # ========== generate data set or take photo samples ================
      
      
    def generate_dataset(self):
      if self.var_dep.get()=="Select Department" or self.var_name.get()=="" or self.var_id.get()=="":
          messagebox.showerror("Error","All Fields are required",parent=self.root)
      else:
        try:       
            conn=mysql.connector.connect(host="localhost",username="root",password="12345",database="face_recogniser")
            my_cursor=conn.cursor()
            my_cursor.execute("select * from student")
            myresult=my_cursor.fetchall()
            id = 0
            for x in myresult:
              id=id+1 
            my_cursor.execute("update student set Department=%s,Course=%s,Year=%s,Semester=%s,Name=%s,Roll=%s,Gender=%s,DOB=%s,Email=%s,Phone=%s,Address=%s,Registration=%s,PhotoSampleStatus=%s where StudentID=%s",(
                  
                  
                                                                        self.var_dep.get(),
                                                                        self.var_course.get(),
                                                                        self.var_year.get(),
                                                                        self.var_sem.get(),
                                                                        self.var_name.get(),
                                                                        self.var_roll.get(),
                                                                        self.var_gender.get(),
                                                                        self.var_dob.get(),
                                                                        self.var_email.get(),
                                                                        self.var_phone.get(),
                                                                        self.var_address.get(),
                                                                        self.var_regd.get(),
                                                                        self.var_radiobtn1.get(),               
                                                                        self.var_id.get()==id+1
                  
                                                                   ))
            conn.commit()
            self.fetch_data()
            self.reset_data()
            conn.close()  
            
       # ======== load predifiend data on face frontals from opencv ==========
            face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")            
      
            def face_cropped(img):
              gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
              faces=face_classifier.detectMultiScale(gray,1.3,5)
              # scaling factor = 1.3
              # Minimum Neughbor = 5
              
              for (x,y,w,h) in faces:
                face_cropped=img[y:y+h,x:x+w]
                return face_cropped
              
            cap=cv2.VideoCapture(0)
            img_id=0
            while True:
              ret,my_frame=cap.read()
              if face_cropped(my_frame) is not None:
                img_id=img_id+1
                face=cv2.resize(face_cropped(my_frame),(500,500))
               # face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                file_name_path="data/user."+str(id)+"."+str(img_id)+".jpg"
                cv2.imwrite(file_name_path,face)
                cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),3)
                cv2.imshow("crooped Face",face) 
              
              if cv2.waitKey(1)==13 or int(img_id)==100:
                break
            cap.release()
            cv2.destroyAllWindows() 
            messagebox.showinfo("result","Generating data sets completed !!!")
        except Exception as es:
            messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)
               
      
        
if __name__ == "__main__":
    root=Tk()
    obj = Student(root)
    root.mainloop()     