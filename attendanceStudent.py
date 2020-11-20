from tkinter import *
import datetime
from tkinter import messagebox
from tkcalendar import *
from db_connect import *
import time
global teacherColour
teacherColour = "#069ce5"
class att:
    def __init__(self):
        global atStdnt
        atStdnt = Toplevel()
        atStdnt.title("Attendance")
        atStdnt.geometry("300x250")
        self.gui_1()
        atStdnt.mainloop()

    def atFinal(self,atd):
        self.atd = atd
        print("inserting attendance")
        if connection.is_connected():
            print("cinneced")
            cur = connection.cursor()
            sql = 'INSERT INTO attendance values("{}","{}","{}","{}","{}","{}")'\
                .format(self.ithStudentName,self.ithStudentID,self.sec,self.subject,self.hour,self.atd)
            cur.execute(sql)
            connection.commit()
            cur.close()
    def attScrn(self):

        self.sec = self.section1.get()
        self.subject = self.sub1.get()
        self.date = self.cal1.get()
        self.hour = self.hr1.get()

        print(self.subject+self.sec+self.date+self.hour)
        if self.sec and self.subject and self.date and self.hour:

            if connection.is_connected():
                cursor = connection.cursor()
                sql = 'SELECT Student_Name, Student_ID from studentSubject where section = "{}" and subject_code ="{}"'\
                    .format(self.sec,self.subject)
                cursor.execute(sql)
                self.students= cursor.fetchall()

                print(len(self.students))
                if not self.students:
                    messagebox.showerror("Error", "No students founds registered for this course",parent = atStdnt)

                else:
                    global attSc
                    attSc = Toplevel()
                    attSc.geometry("320x180")
                    attSc.title("Attendance")
                    x1, x2 = 20, 130
                    y1, gap = 60, 30

                    # header
                    self.tHeader = Label(attSc, text="Attendance", bg=teacherColour, fg='white',
                                         font=("Sans serif", 16, "bold"), pady=6)  # text add
                    self.tHeader.pack(fill=X)  # pack is a must

                    # name lbl
                    self.nameLbl = Label(attSc, text="Student Name: ", font=("Sans Serif", 11))
                    self.nameLbl.pack()
                    self.nameLbl.place(x=x1, y=y1)

                    # USN Lbl
                    self.sIDLbl = Label(attSc, text="Student ID: ", font=("Sans Serif", 11))
                    self.sIDLbl.pack()
                    self.sIDLbl.place(x=x1, y=y1 + gap)

                    '''this is the part of code where everything sucks
                        i cant make for loop to pause until an action is taken
                        may almighty god give me the knowledge to  find a solution for this'''

                    self.ithStudent = self.students[0]
                    self.ithStudentName = self.ithStudent[0]
                    self.ithStudentID = self.ithStudent[1]

                    self.isPresentIcn = PhotoImage(file='button_presentAttendance.png')
                    self.isPresentBtn = Button(attSc, image=self.isPresentIcn, borderwidth=0,
                                                   command =lambda: [ f() for f in [self.atd  ,]])
                    self.isPresentBtn.pack()
                    self.isPresentBtn.place(x=x1 + 40, y=y1 + 2 * gap)

                    # absent btn
                    self.isAbsentIcn = PhotoImage(file='button_absentAttendance.png')
                    self.isAbsentBtn = Button(attSc, image=self.isAbsentIcn, borderwidth=0,
                                                  command=self.atFinal("Absent"))
                    self.isAbsentBtn.pack()
                    self.isAbsentBtn.place(x=x2 + 40, y=y1 + 2 * gap)

                    # Name Label
                    self.studentNameLbl = Label(attSc, text=self.ithStudentName, font=("Sans Serif", 13, 'bold'))
                    self.studentNameLbl.pack()
                    self.studentNameLbl.place(x=x2, y=y1)

                    # ID Label
                    self.sIDLbl1 = Label(attSc, text=self.ithStudentID, font=("Sans Serif", 13, 'bold'))
                    self.sIDLbl1.pack()
                    self.sIDLbl1.place(x=x2, y=y1 + gap)



                    attSc.mainloop()
        else:
            messagebox.showerror("Error","Please enter all fields")
    def gui_1(self):

        x1, x2 = 20, 120
        y1, gapY = 70, 30
        width1 = 160

        #header
        self.tHeader = Label(atStdnt, text="Attendance", bg=teacherColour, fg='white',
                             font=("Sans serif", 16, "bold"), pady=6)  # text add
        self.tHeader.pack(fill=X)  # pack is a must

        # section label
        self.secLbl = Label(atStdnt, text= "Section: ", font = ("Sans Serif",11))
        self.secLbl.pack()
        self.secLbl.place(x=x1,y=y1)

        #Subject lbl
        self.subLbl = Label(atStdnt, text ="Subject Code:", font = ("Sans Serif", 11))
        self.subLbl.pack()
        self.subLbl.place(x=x1,y=y1+gapY)

        #Date Lbl
        self.dateAtd = Label(atStdnt, text = "Date: ", font = ("Sans Serif", 11))
        self.dateAtd.pack()
        self.dateAtd.place(x=x1,y=y1+2*gapY)

        #hour Lbl
        self.hourAtd = Label(atStdnt, text = "Hour", font = ("Sans Serif", 11))
        self.hourAtd.pack()
        self.hourAtd.place(x=x1,y=y1+3*gapY)

        #Section Entry
        self.section1 = Entry(atStdnt)
        self.section1.pack()
        self.section1.place(x=x2,y=y1,width = width1)

        #Subject Entry
        self.sub1 = Entry(atStdnt)
        self.sub1.pack()
        self.sub1.place(x=x2,y=y1+gapY,width = width1)

        # date entry
        d = datetime.date.today()
        self.cal1 = DateEntry(atStdnt, width=12, year=d.year, month=d.month, day=d.day,
                              background=teacherColour, foreground='white', borderwidth=2)
        self.cal1.pack()
        self.cal1.config(date_pattern='yyyy/mm/dd')
        self.cal1.place(x=x2, y=y1+2*gapY)

        # Hour entry
        self.hr1 = Entry(atStdnt)
        self.hr1.pack()
        self.hr1.place(x=x2, y=y1+3*gapY,width = width1)

        #submit Btn
        self.submitBtnIcn = PhotoImage(file = "button_submitTeacherSmall.png")
        self.submitBtn = Button(atStdnt, image = self.submitBtnIcn,borderwidth = 0, command = self.attScrn)
        self.submitBtn.pack()
        self.submitBtn.place(x=x2, y=y1+4*gapY)

if __name__ == "__main__":
    a2= att()
    a2