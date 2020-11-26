from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from Homepage import *
from tkcalendar import DateEntry
import datetime
from db_connect import *

global teacherColour
teacherColour = "#069ce5"
class teacherReg:
    def __init__(self):
        global tReg
        tReg = Toplevel()
        tReg.geometry("500x550")
        tReg.resizable(width=FALSE, height=FALSE)
        tReg.title("Teacher Registration")
        self.gui_1()
        tReg.mainloop()

    def sqlRegisterTchr(self):
        pwd3 = self.pwd1.get()
        pwd4 = self.pwd2.get()
        if pwd3 == pwd4:
            sal = self.salLbl1.get()
            name = self.name1.get()
            id = self.id1.get()
            dept = self.dept1.get()
            dob = self.cal.get()
            cno = self.cno1.get()
            addr = self.addr1.get()
            email = self.email1.get()
            if not (sal and name and id and dept and dob and cno and addr and email):
                messagebox.showwarning("Fields Empty", "Please enter all the fields.")
            else:

                ###SQL COMMAND HERE
                mySql_insert_query = 'INSERT INTO teachers VALUES ("{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}")' \
                    .format(sal, name, id, dept, "None", dob, cno, addr, email, pwd4,"None")
                cursor = connection.cursor()
                cursor.execute(mySql_insert_query)
                connection.commit()
                tReg.destroy()
                messagebox.showinfo("Registration Complete", "Thank you for your registration!")

        else:
            messagebox.showinfo("Password Error", "Passwords do not match!")

    def gui_1(self):
        # registration header text 
        self.regHeader = Label(tReg, text="Teacher/Staff Registration", bg=teacherColour, fg='white',
                               font=("Sans serif", 18, "bold"), pady=8)  # text add
        self.regHeader.pack(fill=X)  # pack is a must
        width1 = 240
        x1, x2 = 45, 165
        y1 = 160
        gap = 35
        fsizeLbl = 11
        # Prompt
        self.nameLbl = Label(tReg, text="Please enter your basic details. ", font=("Sans Serif", 18))
        self.nameLbl.pack()
        self.nameLbl.place(x=85, y=65)

        # Salutanion Lbl
        self.nameLbl = Label(tReg, text="Salutation: ", font=("Sans Serif", 10))
        self.nameLbl.pack()
        self.nameLbl.place(x=x1, y=132)
        # Name Lbl
        self.nameLbl = Label(tReg, text="Name: ", font=("Sans Serif", fsizeLbl))
        self.nameLbl.pack()
        self.nameLbl.place(x=x1, y=y1)

        # Teacher ID
        self.tIdLbl = Label(tReg, text="Teacher ID: ", font=("Sans Serif", fsizeLbl))
        self.tIdLbl.pack()
        self.tIdLbl.place(x=x1, y=y1 + gap)

        # Department     set as list
        self.deptLbl = Label(tReg, text="Department: ", font=("Sans Serif", fsizeLbl))
        self.deptLbl.pack()
        self.deptLbl.place(x=x1, y=y1 + 2 * gap)

        # DOB
        self.dobLbl = Label(tReg, text="Date of Birth: ", font=("Sans Serif", fsizeLbl))
        self.dobLbl.pack()
        self.dobLbl.place(x=x1, y=y1 + 3 * gap)

        # Contact No
        self.cnoLbl = Label(tReg, text="Contact No: ", font=("Sans Serif", fsizeLbl))
        self.cnoLbl.pack()
        self.cnoLbl.place(x=x1, y=y1 + 4 * gap)

        # Address
        self.addrLbl = Label(tReg, text="Address: ", font=("Sans Serif", fsizeLbl))
        self.addrLbl.pack()
        self.addrLbl.place(x=x1, y=y1 + 5 * gap)

        # email Lbl
        self.emailLbl = Label(tReg, text="Email: ", font=("Sans Serif", fsizeLbl))
        self.emailLbl.pack()
        self.emailLbl.place(x=x1, y=y1 + 6 * gap)

        # Pwd1 Lbl
        self.pwdLbl1 = Label(tReg, text="Password: ", font=("Sans Serif", fsizeLbl))
        self.pwdLbl1.pack()
        self.pwdLbl1.place(x=x1, y=y1 + 7 * gap)

        # Pwd2 Lbl
        self.pwdLbl2 = Label(tReg, text="Re-enter Password: ", font=("Sans Serif", 9))
        self.pwdLbl2.pack()
        self.pwdLbl2.place(x=x1, y=y1 + 8 * gap)

        # salutaion list
        self.salLbl1 = StringVar()
        self.salLbl1.set("Mrs.")
        self.sal1 = ttk.Combobox(tReg, textvariable=self.salLbl1)
        self.sal1['values'] = ('Mrs.', 'Mr.', 'Ms.', 'Dr.')
        self.sal1.pack()
        self.sal1.place(x=x2, y=130, width=50)

        # Name text field
        self.name1 = Entry(tReg)
        self.name1.pack()
        self.name1.place(x=x2, y=y1, width=width1)

        # Teacher ID text field
        self.id1 = Entry(tReg)
        self.id1.pack()
        self.id1.place(x=x2, y=y1 + gap, width=width1)

        # Dept list field
        self.deptLbl1 = StringVar()
        self.deptLbl1.set("CSE")
        self.dept1 = ttk.Combobox(tReg, textvariable=self.deptLbl1)
        self.dept1['values'] = ('CSE', 'ISE', 'ECE', 'ME', 'EE', 'Library')
        self.dept1.pack()
        self.dept1.place(x=x2, y=y1 + 2 * gap, width=70)

        # DOB field
        d = datetime.date.today()
        self.cal = DateEntry(tReg, width=12, year=2000, month=d.month, day=d.day,
                             background=teacherColour, foreground='white', borderwidth=2)
        self.cal.pack()
        self.cal.config(date_pattern='dd/mm/yyyy')
        self.cal.place(x=x2, y=y1 + 3 * gap)

        # Contact no text field
        self.cno1 = Entry(tReg)
        self.cno1.pack()
        self.cno1.place(x=x2, y=y1 + 4 * gap, width=width1)

        # Addr text field
        self.addr1 = Entry(tReg)
        self.addr1.pack()
        self.addr1.place(x=x2, y=y1 + 5 * gap, width=width1)

        # Email text field
        self.email1 = Entry(tReg)
        self.email1.pack()
        self.email1.place(x=x2, y=y1 + 6 * gap, width=width1)

        def showHideState():
            if var1.get():
                self.pwd1.config(show="")
                self.pwd2.config(show="")

            else:
                self.pwd1.config(show="*")
                self.pwd2.config(show="*")

        # Password text field
        self.pwd1 = Entry(tReg, show="*")
        self.pwd1.pack()
        self.pwd1.place(x=x2, y=y1 + 7 * gap, width=width1)

        # Password text field
        self.pwd2 = Entry(tReg, show="*")
        self.pwd2.pack()
        self.pwd2.place(x=x2, y=y1 + 8 * gap, width=width1)

        # showPassword Box
        var1 = IntVar()
        chk = Checkbutton(tReg, text="Show", variable=var1, command=showHideState)
        chk.pack()
        chk.place(x=x2 + width1 + 10, y=y1 + 7 * gap)

        # teacher register  button
        teacherRegisterBtn = PhotoImage(file='button_confRegTeacher.png')
        self.teacherRegisterButton = Button(tReg, image=teacherRegisterBtn, borderwidth=0, command=self.sqlRegisterTchr)
        self.teacherRegisterButton.pack()
        self.teacherRegisterButton.place(x=x2, y=470)
        tReg.mainloop()

if __name__ == "__main__":
    v1 = teacherReg()
    v1.gui_1()
