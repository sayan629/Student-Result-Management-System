from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk, messagebox
import sqlite3
class studentClass:
    def __init__(self, root):
        self.root = root
        self.root.title("Result Management System")
        self.root.state('zoomed')
        self.root.config(bg="white")
        self.root.focus_force()
        
    # --- Title ---
        title = Label(
            self.root,
            text="Manage Student Details",
            font=("goudy old style", 28, "bold"),
            bg="#033054",
            fg="white"
        )
        title.place(x=10,y=15,relwidth=0.98,height=35)
        
        # -- Variables ---
        self.var_roll = StringVar()
        self.var_name = StringVar()
        self.var_email = StringVar()
        self.var_gender = StringVar()
        self.var_dob = StringVar()
        self.var_contact = StringVar()
        self.var_course = StringVar()
        self.var_a_date = StringVar()
        self.var_state = StringVar()
        self.var_city = StringVar()
        self.var_pin = StringVar()
        
        
        # --- Widgets ---
        # ------Column 1 ------
        lbl_roll = Label(self.root, text="Roll No.", font=("goudy old style", 15, "bold"), bg="white").place(x=10, y=60)
        lbl_Name = Label(self.root, text="Name", font=("goudy old style", 15, "bold"), bg="white").place(x=10, y=100)
        lbl_Email = Label(self.root, text="Email", font=("goudy old style", 15, "bold"), bg="white").place(x=10, y=140)
        lbl_gender = Label(self.root, text="Gender", font=("goudy old style", 15, "bold"), bg="white").place(x=10, y=180)
        lbl_state = Label(self.root, text="State", font=("goudy old style", 15, "bold"), bg="white").place(x=10, y=220)
        txt_state= Entry(self.root, textvariable=self.var_state, font=("goudy old style", 15, "bold"), bg="lightyellow").place(x=150, y=220, width=150)
        lbl_city = Label(self.root, text="City", font=("goudy old style", 15, "bold"), bg="white").place(x=310, y=220)
        txt_city= Entry(self.root, textvariable=self.var_city, font=("goudy old style", 15, "bold"), bg="lightyellow").place(x=380, y=220, width=100)       
        lbl_pin = Label(self.root, text="Pin", font=("goudy old style", 15, "bold"), bg="white").place(x=500, y=220)
        txt_pin= Entry(self.root, textvariable=self.var_pin, font=("goudy old style", 15, "bold"), bg="lightyellow").place(x=560, y=220, width=120)       
        
        lbl_address = Label(self.root, text="Address", font=("goudy old style", 15, "bold"), bg="white").place(x=10, y=260)
    
        # --- Entry Fields---
        self.txt_roll = Entry(self.root, textvariable=self.var_roll, font=("goudy old style", 15, "bold"), bg="lightyellow")
        self.txt_roll.place(x=150, y=60, width=200)
        
        txt_name = Entry(self.root, textvariable=self.var_name, font=("goudy old style", 15, "bold"), bg="lightyellow").place(x=150, y=100, width=200)
        txt_email = Entry(self.root, textvariable=self.var_email, font=("goudy old style", 15, "bold"), bg="lightyellow").place(x=150, y=140, width=200)
        self.txt_gender = ttk.Combobox(self.root, textvariable=self.var_gender,values =("Select","Male", "Female", "Transgender","Prefer not to say"), font=("goudy old style", 15, "bold"), state = 'readonly',justify=CENTER)
        self.txt_gender.place(x=150, y=180, width=200)
        self.txt_gender.current(0)
        
        
        
        # --- Column 2 ---
        lbl_dob = Label(self.root, text="Date of Birth", font=("goudy old style", 15, "bold"), bg="white").place(x=360, y=60)
        lbl_contact = Label(self.root, text="Contact", font=("goudy old style", 15, "bold"), bg="white").place(x=360, y=100)
        lbl_admission = Label(self.root, text="Admission", font=("goudy old style", 15, "bold"), bg="white").place(x=360, y=140)
        lbl_course = Label(self.root, text="Course", font=("goudy old style", 15, "bold"), bg="white").place(x=360, y=180)

        # --- Entry Fields---
        self.course_list = []
        # function call to update the list
        self.fetch_course()
        txt_dob = Entry(self.root, textvariable=self.var_dob, font=("goudy old style", 15, "bold"), bg="lightyellow").place(x=480, y=60, width=200)
        txt_contact = Entry(self.root, textvariable=self.var_contact, font=("goudy old style", 15, "bold"), bg="lightyellow").place(x=480, y=100, width=200)
        txt_admission = Entry(self.root, textvariable=self.var_a_date, font=("goudy old style", 15, "bold"), bg="lightyellow").place(x=480, y=140, width=200)
        self.txt_course = ttk.Combobox(self.root, textvariable=self.var_course,values =self.course_list, font=("goudy old style", 15, "bold"), state = 'readonly',justify=CENTER)
        self.txt_course.place(x=480, y=180, width=200)
        self.txt_course.set("Select")
        
              
        # ---- Text Field ---
        self.txt_address = Text(self.root, font=("goudy old style", 15, "bold"), bg="lightyellow")
        self.txt_address.place(x=150, y=260,width=540, height=100)

        # --- Buttons ---
        self.btn_add=Button(self.root, text="Save", font=("goudy old style", 15, "bold"), bg="#2196f3", fg="white", cursor="hand2",command=self.add)
        self.btn_add.place(x=150, y=400, width=110, height=40)
        self.btn_update=Button(self.root, text="Update", font=("goudy old style", 15, "bold"), bg="#4caf50", fg="white", cursor="hand2",command=self.update)
        self.btn_update.place(x=270, y=400, width=110, height=40)
        self.btn_delete=Button(self.root, text="Delete", font=("goudy old style", 15, "bold"), bg="#f44336", fg="white", cursor="hand2",command=self.delete)
        self.btn_delete.place(x=390, y=400, width=110, height=40)
        self.btn_clear=Button(self.root, text="Clear", font=("goudy old style", 15, "bold"), bg="#607d8b", fg="white", cursor="hand2",command=self.clear)
        self.btn_clear.place(x=510, y=400, width=110, height=40)
        
        # --- Search Panel ---
        self.var_search = StringVar()
        lbl_search_roll = Label(self.root, text="Roll No.", font=("goudy old style", 15, "bold"), bg="white").place(x=720, y=60)
        txt_search_roll = Entry(self.root, textvariable=self.var_search, font=("goudy old style", 15, "bold"), bg="lightyellow").place(x=870, y=60, width=180)
        btn_search=Button(self.root, text="Search", font=("goudy old style", 15, "bold"), bg="#03a9f4", fg="white", cursor="hand2",command=self.search)
        btn_search.place(x=1070, y=60, width=120, height=28)
        
        # --- Content ---
        self.C_Frame = Frame(self.root, bd=2, relief=RIDGE)
        self.C_Frame.place(x=720, y=100, width=470, height=340)
        
        # --- Scrollbars ---
        scrolly=Scrollbar(self.C_Frame, orient=VERTICAL)
        scrollx=Scrollbar(self.C_Frame, orient=HORIZONTAL)
        
        # --- Table ---
        self.Course_Table = ttk.Treeview(self.C_Frame, columns=("roll", "name", "email", "gender", "dob","contact","admission","course","state","city","pin","address"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        
        
        # Pack Scrollbars
        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)
        
        
        # Configure Scrollbars
        scrollx.config(command=self.Course_Table.xview)
        scrolly.config(command=self.Course_Table.yview)
        
        self.Course_Table.heading("roll", text="Roll No.")
        self.Course_Table.heading("name", text="Name")
        self.Course_Table.heading("email", text="Email")
        self.Course_Table.heading("gender", text="Gender")
        self.Course_Table.heading("dob", text="D.O.B")
        self.Course_Table.heading("contact", text="Contact")
        self.Course_Table.heading("admission", text="Admission")
        self.Course_Table.heading("course", text="Course")
        self.Course_Table.heading("state", text="State")
        self.Course_Table.heading("city", text="City")
        self.Course_Table.heading("pin", text="Pin")
        self.Course_Table.heading("address", text="Address")
        self.Course_Table["show"] = 'headings'
        self.Course_Table.column("roll", width=100)
        self.Course_Table.column("name", width=100)
        self.Course_Table.column("email", width=100)
        self.Course_Table.column("gender", width=100)
        self.Course_Table.column("dob", width=100)
        self.Course_Table.column("contact", width=100)
        self.Course_Table.column("admission", width=100)
        self.Course_Table.column("course", width=100)
        self.Course_Table.column("state", width=100)
        self.Course_Table.column("city", width=100)
        self.Course_Table.column("pin", width=100)
        self.Course_Table.column("address", width=150)
        self.Course_Table.pack(fill=BOTH, expand=1)
        self.Course_Table.bind("<ButtonRelease-1>", self.get_data)
        self.show()
        
        
# ======================================================
    def clear(self):
        self.show()
        self.var_roll.set("")
        self.var_name.set("")
        self.var_email.set("")
        self.var_gender.set("")
        self.var_dob.set("")
        self.var_contact.set("")
        self.var_a_date.set("")
        self.var_course.set("")
        self.var_state.set("")
        self.var_city.set("")
        self.var_pin.set("")
        self.txt_address.delete('1.0', END)
        self.txt_roll.config(state=NORMAL)
        self.var_search.set("")
     
    def delete(self):
        
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
            if self.var_roll.get() == "":
                messagebox.showerror("Error", "Roll Number should be required", parent=self.root)
            else:
                cur.execute("select * from student where roll=?", (self.var_roll.get(),))
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror("Error","Please Select Student from List", parent=self.root)
                else:
                    op = messagebox.askyesno("Confirm", "Do you really want to delete?", parent=self.root)
                    if op == True:
                        cur.execute("delete from student where roll=?", (self.var_roll.get(),))
                        con.commit()
                        messagebox.showinfo("Delete", "Student Deleted Successfully", parent=self.root)
                        self.clear()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")
            
             
        
    def get_data(self, ev):
        self.txt_roll.config(state='readonly')
        r = self.Course_Table.focus()
        content = self.Course_Table.item(r)
        row = content['values']
        self.var_roll.set(row[0])
        self.var_name.set(row[1])
        self.var_email.set(row[2])
        self.var_gender.set(row[3])
        self.var_dob.set(row[4])
        self.var_contact.set(row[5])
        self.var_a_date.set(row[6])
        self.var_course.set(row[7])
        self.var_state.set(row[8])
        self.var_city.set(row[9])
        self.var_pin.set(row[10])
        self.txt_address.delete('1.0', END)
        self.txt_address.insert('1.0', row[11])
        
    def add(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
            if self.var_roll.get() == "":
                messagebox.showerror("Error", "Roll Number should be required", parent=self.root)
            else:
                cur.execute("select * from student where roll=?", (self.var_roll.get(),))
                row = cur.fetchone()
                if row != None:
                    messagebox.showerror("Error", "Roll Number already present, try different", parent=self.root)
                else:
                    cur.execute("insert into student (roll, name, email, gender, dob, contact, admission, course, state, city, pin, address) values(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",(
                        self.var_roll.get(),
                        self.var_name.get(),
                        self.var_email.get(),
                        self.var_gender.get(),
                        self.var_dob.get(), 
                        self.var_contact.get(),
                        self.var_a_date.get(),
                        self.var_course.get(),
                        self.var_state.get(),
                        self.var_city.get(),
                        self.var_pin.get(),
                        self.txt_address.get('1.0', END)
                    )) 
                    con.commit()
                    messagebox.showinfo("Success", "Student added successfully", parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")
            
    def update(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
            if self.var_roll.get() == "":
                messagebox.showerror("Error", "Roll Number should be required", parent=self.root)
            else:
                cur.execute("select * from student where roll=?", (self.var_roll.get(),))
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror("Error", "Select Student from List", parent=self.root)
                else:
                    cur.execute("update  student set name=?, email=?, gender=?, dob=?, contact=?, admission=?, course=?, state=?, city=?, pin=?, address=? where roll=?",(
                        self.var_name.get(),
                        self.var_email.get(),
                        self.var_gender.get(),
                        self.var_dob.get(),
                        self.var_contact.get(),
                        self.var_a_date.get(),
                        self.var_course.get(),
                        self.var_state.get(),
                        self.var_city.get(),
                        self.var_pin.get(),
                        self.txt_address.get('1.0', END),
                        self.var_roll.get()
                    )) 
                    con.commit()
                    messagebox.showinfo("Success", "Student Updated successfully", parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")
            
            
    def show(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
            cur.execute("select * from student")
            rows = cur.fetchall()
            self.Course_Table.delete(*self.Course_Table.get_children())
            for row in rows:
                self.Course_Table.insert('', END, values=row)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")
            
    
    def fetch_course(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
            cur.execute("select name from course")
            rows = cur.fetchall()
            if len(rows)>0:
                for row in rows:
                    self.course_list.append(row[0])
            # print(v)    
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")
    
    
    def search(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()

        try:
            search_value = self.var_search.get().strip()

            cur.execute("SELECT * FROM student WHERE roll=?",(self.var_search.get(),))

            row = cur.fetchone()
            if row!=None:
                self.Course_Table.delete(*self.Course_Table.get_children())
                self.Course_Table.insert('', END, values=row)
            else:
                messagebox.showerror("Error", "No record found", parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")

if __name__ == "__main__":
    root = Tk()
    obj = studentClass(root)
    root.mainloop()