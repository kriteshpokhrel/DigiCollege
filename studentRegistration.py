from tkinter import *
from tkinter import ttk
from tkcalendar import DateEntry
from Homepage import *
from db_connect import *
from tkinter import messagebox
global studentColour
studentColour = "#f2820d"


# class teacherRegistration:
# def m1(self):
class studentReg:
    def __init__(self):
        global sReg
        sReg = Toplevel()
        sReg.geometry("500x550")
        sReg.resizable(width=FALSE, height=FALSE)
        sReg.title("Student Registration")
        self.gui_1()
        sReg.mainloop()

    def sqlRegisterStdnt(self):
        pwd3 = self.pwd1.get()
        pwd4 = self.pwd2.get()
        if pwd3 == pwd4:
            sal = self.salLbl1.get()
            name = self.name1.get()
            id = self.id1.get()
            dept = self.dept1.get()
            sec = self.sec1.get()
            dob = self.cal.get()
            cno = self.cno1.get()
            addr = self.addr1.get()
            email = self.email1.get()
            ###SQL COMMAND HERE
            if not (sal and name and id and dept and dob and cno and addr and email):
                messagebox.showwarning("Fields Empty", "Please enter all the fields.")
            else:

                ###SQL COMMAND HERE
                mySql_insert_query = 'INSERT INTO students VALUES ("{}","{}","{}","{}","{}","{}","{}","{}","{}","{}")'.format(
                    sal, name, id, dept, sec, dob, cno, addr, email, pwd4)
                cursor = connection.cursor()
                cursor.execute(mySql_insert_query)
                connection.commit()
                sReg.destroy()
                messagebox.showinfo("Registration Complete", "Thank you for your registration!")

        else:
            messagebox.showinfo("Password Error", "Passwords do not match!")

    def gui_1(self):
        # registration header text
        self.regHeader = Label(sReg, text="Student Registration", bg=studentColour, fg='white',
                               font=("Sans serif", 18, "bold"),
                               pady=8)  # text add
        self.regHeader.pack(fill=X)  # pack is a must
        width1 = 240
        x1, x2 = 45, 165
        y1 = 160
        gap = 35
        fsizeLbl = 11
        # Prompt
        self.nameLbl = Label(sReg, text="Please enter your basic details. ", font=("Sans Serif", 18))
        self.nameLbl.pack()
        self.nameLbl.place(x=85, y=65)

        # Salutanion Lbl
        self.nameLbl = Label(sReg, text="Salutation: ", font=("Sans Serif", 10))
        self.nameLbl.pack()
        self.nameLbl.place(x=x1, y=132)

        # Name Lbl
        self.nameLbl = Label(sReg, text="Name: ", font=("Sans Serif", fsizeLbl))
        self.nameLbl.pack()
        self.nameLbl.place(x=x1, y=y1)

        # student ID
        self.tIdLbl = Label(sReg, text="Student ID: ", font=("Sans Serif", fsizeLbl))
        self.tIdLbl.pack()
        self.tIdLbl.place(x=x1, y=y1 + gap)

        # Department     set as list
        self.deptLbl = Label(sReg, text="Department: ", font=("Sans Serif", fsizeLbl))
        self.deptLbl.pack()
        self.deptLbl.place(x=x1, y=y1 + 2 * gap)

        # Section
        self.secLbl = Label(sReg, text="Section: ", font=("Sans Serif", fsizeLbl))
        self.secLbl.pack()
        self.secLbl.place(x=x1, y=y1 + 3 * gap)

        # DOB
        self.dobLbl = Label(sReg, text="Date of Birth: ", font=("Sans Serif", fsizeLbl))
        self.dobLbl.pack()
        self.dobLbl.place(x=x1, y=y1 + 4 * gap)

        # Contact No
        self.cnoLbl = Label(sReg, text="Contact No: ", font=("Sans Serif", fsizeLbl))
        self.cnoLbl.pack()
        self.cnoLbl.place(x=x1, y=y1 + 5 * gap)

        # Address
        self.addrLbl = Label(sReg, text="Address: ", font=("Sans Serif", fsizeLbl))
        self.addrLbl.pack()
        self.addrLbl.place(x=x1, y=y1 + 6 * gap)

        # email Lbl
        self.emailLbl = Label(sReg, text="Email: ", font=("Sans Serif", fsizeLbl))
        self.emailLbl.pack()
        self.emailLbl.place(x=x1, y=y1 + 7 * gap)

        # Pwd1 Lbl
        self.pwdLbl1 = Label(sReg, text="Password: ", font=("Sans Serif", fsizeLbl))
        self.pwdLbl1.pack()
        self.pwdLbl1.place(x=x1, y=y1 + 8 * gap)

        # Pwd2 Lbl
        self.pwdLbl2 = Label(sReg, text="Re-enter Password: ", font=("Sans Serif", 9))
        self.pwdLbl2.pack()
        self.pwdLbl2.place(x=x1, y=y1 + 9 * gap)

        # salutaion list
        self.salLbl1 = StringVar()
        self.salLbl1.set("Mrs.")
        self.sal1 = ttk.Combobox(sReg, textvariable=self.salLbl1)
        self.sal1['values'] = ('Mrs.', 'Mr.', 'Ms.', 'Dr.')
        self.sal1.pack()
        self.sal1.place(x=x2, y=130, width=50)

        # Name text field
        self.name1 = Entry(sReg)
        self.name1.pack()
        self.name1.place(x=x2, y=y1, width=width1)

        # Teacher ID text field
        self.id1 = Entry(sReg)
        self.id1.pack()
        self.id1.place(x=x2, y=y1 + gap, width=width1)

        # Dept list field
        self.deptLbl1 = StringVar()
        self.deptLbl1.set("CSE")
        self.dept1 = ttk.Combobox(sReg, textvariable=self.deptLbl1)
        self.dept1['values'] = ('CSE', 'ISE', 'ECE', 'ME', 'EE')
        self.dept1.pack()
        self.dept1.place(x=x2, y=y1 + 2 * gap, width=70)

        # Sec text field
        self.sec1 = Entry(sReg)
        self.sec1.pack()
        self.sec1.place(x=x2, y=y1 + 3 * gap, width=width1)

        # DOB field
        self.cal = DateEntry(sReg, width=12, year=2020, month=11, day=18,
                             background=studentColour, foreground='white', borderwidth=2)
        self.cal.pack()
        self.cal.place(x=x2, y=y1 + 4 * gap)

        # Contact no text field
        self.cno1 = Entry(sReg)
        self.cno1.pack()
        self.cno1.place(x=x2, y=y1 + 5 * gap, width=width1)

        # Addr text field
        self.addr1 = Entry(sReg)
        self.addr1.pack()
        self.addr1.place(x=x2, y=y1 + 6 * gap, width=width1)

        # Email text field
        self.email1 = Entry(sReg)
        self.email1.pack()
        self.email1.place(x=x2, y=y1 + 7 * gap, width=width1)

        def showHideState():
            if var1.get():
                self.pwd1.config(show="")
                self.pwd2.config(show="")

            else:
                self.pwd1.config(show="*")
                self.pwd2.config(show="*")

        # Password text field
        self.pwd1 = Entry(sReg, show="*")
        self.pwd1.pack()
        self.pwd1.place(x=x2, y=y1 + 8 * gap, width=width1)

        # Password text field
        self.pwd2 = Entry(sReg, show="*")
        self.pwd2.pack()
        self.pwd2.place(x=x2, y=y1 + 9 * gap, width=width1)

        # showPassword Box
        var1 = IntVar()
        chk = Checkbutton(sReg, text="Show", variable=var1, command=showHideState)
        chk.pack()
        chk.place(x=x2 + width1 + 10, y=y1 + 8 * gap)

        # Student register  button
        StudensRegisterBtn = PhotoImage(file='button_confRegStudent.png')
        self.StudensRegisterButton = Button(sReg, image=StudensRegisterBtn, borderwidth=0,
                                            command=self.sqlRegisterStdnt)
        self.StudensRegisterButton.pack()
        self.StudensRegisterButton.place(x=x2, y=510)

        sReg.mainloop()


if __name__ == "__main__":
    sReg1 = studentReg()
    sReg1
