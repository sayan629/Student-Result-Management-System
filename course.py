from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
class CourseClass:
    def __init__(self, root):
        self.root = root
        self.root.title("Result Management System")
        self.root.state('zoomed')
        self.root.config(bg="white")
        self.root.focus_force()
        
    # --- Title ---
        title = Label(
            self.root,
            text="Manage Course Details",
            font=("goudy old style", 28, "bold"),
            bg="#033054",
            fg="white"
        )
        title.place(x=10,y=15,relwidth=0.98,height=35)
        
        # -- Variables ---
        self.var_course_name = StringVar()
        self.var_duration = StringVar()
        self.var_charges = StringVar()
        
        # --- Widgets ---
        lbl_course_name = Label(self.root, text="Course Name", font=("goudy old style", 15, "bold"), bg="white").place(x=10, y=60)
        lbl_duration = Label(self.root, text="Duration", font=("goudy old style", 15, "bold"), bg="white").place(x=10, y=100)
        lbl_charges = Label(self.root, text="Charges", font=("goudy old style", 15, "bold"), bg="white").place(x=10, y=140)
        lbl_description = Label(self.root, text="Description", font=("goudy old style", 15, "bold"), bg="white").place(x=10, y=180)
        
        # --- Entry Fields---
        self.txt_course_name = Entry(self.root, textvariable=self.var_course_name, font=("goudy old style", 15, "bold"), bg="lightyellow")
        self.txt_course_name.place(x=150, y=60, width=200)
        
        txt_duration = Entry(self.root, textvariable=self.var_duration, font=("goudy old style", 15, "bold"), bg="lightyellow").place(x=150, y=100, width=200)
        txt_charges = Entry(self.root, textvariable=self.var_charges, font=("goudy old style", 15, "bold"), bg="lightyellow").place(x=150, y=140, width=200)
        self.txt_description = Text(self.root, font=("goudy old style", 15, "bold"), bg="lightyellow")
        self.txt_description.place(x=150, y=180,width=500, height=130)

        # --- Buttons ---
        self.btn_add=Button(self.root, text="Save", font=("goudy old style", 15, "bold"), bg="#2196f3", fg="white", cursor="hand2")
        self.btn_add.place(x=150, y=400, width=110, height=40)
        self.btn_update=Button(self.root, text="Update", font=("goudy old style", 15, "bold"), bg="#4caf50", fg="white", cursor="hand2")
        self.btn_update.place(x=270, y=400, width=110, height=40)
        self.btn_delete=Button(self.root, text="Delete", font=("goudy old style", 15, "bold"), bg="#f44336", fg="white", cursor="hand2")
        self.btn_delete.place(x=390, y=400, width=110, height=40)
        self.btn_clear=Button(self.root, text="Clear", font=("goudy old style", 15, "bold"), bg="#607d8b", fg="white", cursor="hand2")
        self.btn_clear.place(x=510, y=400, width=110, height=40)
        
        # --- Search Panel ---
        self.var_search = StringVar()
        lbl_search_courseName = Label(self.root, text="Course Name", font=("goudy old style", 15, "bold"), bg="white").place(x=720, y=60)
        txt_search_courseName = Entry(self.root, textvariable=self.var_search, font=("goudy old style", 15, "bold"), bg="lightyellow").place(x=870, y=60, width=180)
        btn_search=Button(self.root, text="Search", font=("goudy old style", 15, "bold"), bg="#03a9f4", fg="white", cursor="hand2").place(x=1070, y=60, width=120, height=28)
        
        # --- Content ---
        self.C_Frame = Frame(self.root, bd=2, relief=RIDGE)
        self.C_Frame.place(x=720, y=100, width=470, height=340)
        
        # --- Scrollbars ---
        scrolly=Scrollbar(self.C_Frame, orient=VERTICAL)
        scrollx=Scrollbar(self.C_Frame, orient=HORIZONTAL)
        
        # --- Table ---
        self.Course_Table = ttk.Treeview(self.C_Frame, columns=("cid", "name", "duration", "charges", "description"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        
        
        # Pack Scrollbars
        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)
        
        
        # Configure Scrollbars
        scrollx.config(command=self.Course_Table.xview)
        scrolly.config(command=self.Course_Table.yview)
        
        self.Course_Table.heading("cid", text="Course ID")
        self.Course_Table.heading("name", text="Name")
        self.Course_Table.heading("duration", text="Duration")
        self.Course_Table.heading("charges", text="Charges")
        self.Course_Table.heading("description", text="Description")
        self.Course_Table["show"] = 'headings'
        self.Course_Table.column("cid", width=100)
        self.Course_Table.column("name", width=100)
        self.Course_Table.column("duration", width=100)
        self.Course_Table.column("charges", width=100)
        self.Course_Table.column("description", width=150)

        self.Course_Table.pack(fill=BOTH, expand=1)
        
        
        
if __name__ == "__main__":
    root = Tk()
    obj = CourseClass(root)
    root.mainloop()
