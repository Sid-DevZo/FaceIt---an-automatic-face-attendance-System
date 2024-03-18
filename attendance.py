from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
from tkinter import filedialog
import mysql.connector
import cv2
import os
import csv


mydata=[]
class Attendance:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")
        
        #============  Variable ======================
        
        self.var_atten_id=StringVar()
        self.var_atten_roll=StringVar()
        self.var_atten_name=StringVar()
        self.var_atten_dep=StringVar()
        self.var_atten_time=StringVar()
        self.var_atten_date=StringVar()
        self.var_atten_attendance=StringVar()
        
        
        img=Image.open(r"C:\Users\SIDDHARTHA\Desktop\DatabaseProject\images\uit1.png")
        img=img.resize((1530,790),Image.Resampling.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)
        
        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=1530,height=790)
        
        title_lbl=Label(f_lbl,text="FACE RECOGNITION ATTENDANCE SYSTEM",font=("times new roman",27,"bold"),bg="skyblue",fg="blue")
        title_lbl.place(x=0,y=0,width=1530,height=42)
        
        main_frame=Frame(f_lbl,bd=2,bg="white")
        main_frame.place(x=0,y=70,width=1366,height=600)


        Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="student_details",font=("times new roman",12,"bold"))
        Left_frame.place(x=1,y=20,width=675,height=560)
        

        
        # class student information
        
        class_student_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Class Student Information",font=("times new roman",12,"bold"))
        class_student_frame.place(x=3,y=260,width=670,height=315)
        
        # student ID
        AttendanceID_label=Label(class_student_frame,text="Attendance ID",font=("times new roman",12,"bold"),bg="white")
        AttendanceID_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)
        
        studentID_entry=ttk.Entry(class_student_frame,width=20,textvariable=self.var_atten_id,font=("times new roman",9,"bold"))
        studentID_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)
        
        # roll
        ROll_label=Label(class_student_frame,text="Roll",font=("times new roman",12,"bold"),bg="white")
        ROll_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)
        
        ROll_entry=ttk.Entry(class_student_frame,width=20,textvariable=self.var_atten_roll,font=("times new roman",9,"bold"))
        ROll_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)
        
        
        
          # name
        Name_label=Label(class_student_frame,text="Name",font=("times new roman",12,"bold"),bg="white")
        Name_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)
        
        Name_entry=ttk.Entry(class_student_frame,width=20,textvariable=self.var_atten_name,font=("times new roman",9,"bold"))
        Name_entry.grid(row=1,column=1,padx=10,pady=5,sticky=W)
        
        
          # dept
        department_label=Label(class_student_frame,text="Department",font=("times new roman",12,"bold"),bg="white")
        department_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)
        
        department_entry=ttk.Entry(class_student_frame,width=20,textvariable=self.var_atten_dep,font=("times new roman",9,"bold"))
        department_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)
        
           # Date
        date_label=Label(class_student_frame,text="Date",font=("times new roman",12,"bold"),bg="white")
        date_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)
        
        date_entry=ttk.Entry(class_student_frame,width=20,textvariable=self.var_atten_date,font=("times new roman",9,"bold"))
        date_entry.grid(row=2,column=1,padx=10,pady=5,sticky=W)
        
         # time
        time_label=Label(class_student_frame,text="Time",font=("times new roman",12,"bold"),bg="white")
        time_label.grid(row=2,column=2,padx=10,pady=5,sticky=W)
        
        time_entry=ttk.Entry(class_student_frame,width=20,textvariable=self.var_atten_time,font=("times new roman",9,"bold"))
        time_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)
        
        
        
        
          # attendance status
        AttendanceStatus_label=Label(class_student_frame,text="Attendance Status",font=("times new roman",12,"bold"),bg="white")
        AttendanceStatus_label.grid(row=3,column=0,padx=10,pady=5,sticky=W)
        
        AttendanceStatus_combo=ttk.Combobox(class_student_frame,textvariable=self.var_atten_attendance,font=("times new roman",9,"bold"),state="readonly")
        AttendanceStatus_combo["values"]=("Select","Present","Absent")
        AttendanceStatus_combo.current(0)
        AttendanceStatus_combo.grid(row=3,column=1,padx=2,pady=10,sticky=W)
        
        
         
        #button Frame
        
        btn_frame=Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=200,width=665,height=90)
        
        save_btn=Button(btn_frame,text="Import CSV",command=self.importCSV,width=18,font=("times new roman",12,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0)
        
        update_btn=Button(btn_frame,text="Export CSV",command=self.exportCSV,width=18,font=("times new roman",12,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=1)
        
        delete_btn=Button(btn_frame,text="Delete",width=18,font=("times new roman",12,"bold"),bg="blue",fg="white")
        delete_btn.grid(row=0,column=2)
        
        reset_btn=Button(btn_frame,text="Reset",width=18,command=self.reset_data,font=("times new roman",12,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=3)
        
         # right label frame
        right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="student_details",font=("times new roman",12,"bold"))
        right_frame.place(x=680,y=20,width=670,height=560)
        
        
        table_frame=LabelFrame(right_frame,bd=2,relief=RIDGE)
        table_frame.place(x=5,y=210,width=660,height=110)
        
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
        
        self.AttendanceReportTable=ttk.Treeview(table_frame,column=("AttendanceID","Roll","Name","Dep","date","time","Status"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)
        
        
        self.AttendanceReportTable.heading("AttendanceID",text="AttendanceID")
        self.AttendanceReportTable.heading("Roll",text="Roll")
        self.AttendanceReportTable.heading("Name",text="Name")
        self.AttendanceReportTable.heading("Dep",text="Departmen")
        self.AttendanceReportTable.heading("date",text="date")
        self.AttendanceReportTable.heading("time",text="time")
        self.AttendanceReportTable.heading("Status",text="Status")
        
        self.AttendanceReportTable["show"]="headings"
       
        self.AttendanceReportTable.column("AttendanceID",width=100)
        self.AttendanceReportTable.column("Roll",width=100)
        self.AttendanceReportTable.column("Name",width=100)
        self.AttendanceReportTable.column("Dep",width=100)
        self.AttendanceReportTable.column("date",width=100)
        self.AttendanceReportTable.column("time",width=100)
        self.AttendanceReportTable.column("Status",width=150)
       
        self.AttendanceReportTable.pack(fill=BOTH,expand=1)
        
        self.AttendanceReportTable.bind("<ButtonRelease>",self.get_cursor)
       
       
        #================= fetch data =================
        
    def fetchData(self,rows):
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        for i in rows:
            self.AttendanceReportTable.insert("",END,values=i)
                
    def importCSV(self):
        global mydata
        mydata.clear()
        fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*csv"),("All File","*.*")),parent=self.root)
        with open(fln) as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetchData(mydata)      
            
            
    def exportCSV(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("No Data","No Data found to export",parent=self.root)
                return False
            fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*csv"),("All File","*.*")),parent=self.root)            
            with open(fln,mode="w",newline="") as myfile:
                exp_write=csv.writer(myfile,delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Data Export","Your data exported to"+os.path.basename(fln)+"Successfully")
        except Exception as es:
            messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)            
                        
    def get_cursor(self,event=""):
        cursor_row=self.AttendanceReportTable.focus()
        content=self.AttendanceReportTable.item(cursor_row)
        rows=content['values']
        self.var_atten_id.set(rows[0])
        self.var_atten_roll.set(rows[1])
        self.var_atten_name.set(rows[2])
        self.var_atten_dep.set(rows[3])
        self.var_atten_time.set(rows[4])
        self.var_atten_date.set(rows[5])
        self.var_atten_attendance.set(rows[6])
        
    def reset_data(self):
        self.var_atten_id.set("")
        self.var_atten_roll.set("")
        self.var_atten_name.set("")
        self.var_atten_dep.set("")
        self.var_atten_time.set("")
        self.var_atten_date.set("")
        self.var_atten_attendance.set("")
        
            
            
        
       
   
        
if __name__ == "__main__":
    root=Tk()
    obj = Attendance(root)
    root.mainloop()           