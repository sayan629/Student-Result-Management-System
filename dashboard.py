from tkinter import *
from PIL import Image, ImageTk
from course import CourseClass
from student import studentClass
from result import resultClass

class RMS:
    def __init__(self, root):
        self.root = root
        self.root.title("Result Management System")
        self.root.state('zoomed')
        self.root.config(bg="white")

        # ======================================================
        # Logo
        # ======================================================
        logo = Image.open("images/logo.png")
        logo = logo.resize((60, 60), Image.LANCZOS)
        self.logo_dash = ImageTk.PhotoImage(logo)

        # ======================================================
        # Title
        # ======================================================
        title = Label(
            self.root,
            text="   Result Management System",
            image=self.logo_dash,
            compound=LEFT,
            font=("goudy old style", 28, "bold"),
            bg="#033054",
            fg="white",
            anchor="center"
        )

        title.place(x=0, y=0, relwidth=1, height=80)

        # ======================================================
        # Menu Frame
        # ======================================================
        M_Frame = LabelFrame(
            self.root,
            text="Menus",
            font=("times new roman", 18, "bold"),
            bg="white",
            bd=4,
            relief=RIDGE
        )

        M_Frame.place(x=10, y=90, relwidth=0.985, height=100)

        # ======================================================
        # Buttons
        # ======================================================
        btn_font = ("goudy old style", 16, "bold")

        btn_width = 180
        btn_height = 45
        gap = 20

        buttons = [
            ("Course", self.add_course),
            ("Student", self.add_student),
            ("Result", self.add_result),
            ("View Results", None),
            ("Logout", None),
            ("Exit", self.root.destroy)
        ]

        x = 20

        for text, cmd in buttons:
            btn = Button(
                M_Frame,
                text=text,
                font=btn_font,
                bg="#033054",
                fg="white",
                cursor="hand2",
                bd=2,
                relief=RIDGE,
                command=cmd
            )

            btn.place(
                x=x,
                y=20,
                width=btn_width,
                height=btn_height
            )

            x += btn_width + gap

        # ======================================================
        # Background Image
        # ======================================================
        self.bg_img = Image.open("images/bg.png")
        self.bg_img = self.bg_img.resize((700, 320), Image.LANCZOS)

        self.bg_img_tk = ImageTk.PhotoImage(self.bg_img)

        self.lbl_bg = Label(
            self.root,
            image=self.bg_img_tk,
            bg="white",
            bd=0
        )
        self.lbl_bg.place(x=520, y=220)

        # ======================================================
        # Dashboard Boxes
        # ======================================================
        box_width = 280
        box_height = 100
        gap = 40
        start_x = 350
        y_pos = 570

        # ===== Total Courses =====
        self.lbl_course = Label(
            self.root,
            text="Total Courses\n[ 0 ]",
            font=("goudy old style", 20, "bold"),
            bd=10,
            relief=RIDGE,
            bg="#e43b06",
            fg="white"
        )

        self.lbl_course.place(
            x=start_x,
            y=y_pos,
            width=box_width,
            height=box_height
        )

        # ===== Total Students =====
        self.lbl_student = Label(
            self.root,
            text="Total Students\n[ 0 ]",
            font=("goudy old style", 20, "bold"),
            bd=10,
            relief=RIDGE,
            bg="#0676ad",
            fg="white"
        )

        self.lbl_student.place(
            x=start_x + box_width + gap,
            y=y_pos,
            width=box_width,
            height=box_height
        )

        # ===== Total Results =====
        self.lbl_result = Label(
            self.root,
            text="Total Results\n[ 0 ]",
            font=("goudy old style", 20, "bold"),
            bd=10,
            relief=RIDGE,
            bg="#038074",
            fg="white"
        )

        self.lbl_result.place(
            x=start_x + (box_width + gap) * 2,
            y=y_pos,
            width=box_width,
            height=box_height
        )

        # ======================================================
        # Footer
        # ======================================================
        footer = Label(
            self.root,
            text="SRMS - Result Management System | Developed by Sayan\nContact us for any Technical Issue: 8972866768",
            font=("goudy old style", 12),
            bg="#262626",
            fg="white"
        )

        footer.pack(side=BOTTOM, fill=X)

    def add_course(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = CourseClass(self.new_win)
    
    def add_student(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = studentClass(self.new_win)
    
    def add_result(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = resultClass(self.new_win)
# ==========================================================
# Main
# ==========================================================
if __name__ == "__main__":
    root = Tk()
    obj = RMS(root)
    root.mainloop()