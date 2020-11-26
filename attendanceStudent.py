from tkinter import *
import datetime
from tkinter import messagebox
from tkcalendar import *
from db_connect import *
from attdScreen import *
import time
global teacherColour
teacherColour = "#069ce5"
class att:
    def __init__(self,fTname,tID):
        self.fTname = fTname
        self.tID = tID
        global atStdnt
        atStdnt = Toplevel()
        atStdnt.title("Attendance")
        atStdnt.geometry("300x250")
        self.gui_1()
        atStdnt.mainloop()


    def atReg(self):
        i=0
        for self.ithStudent in self.students:
            self.ithStudentName = self.ithStudent[0]
            self.ithStudentID = self.ithStudent[1]
            self.ithStudentAtd  =self.abPr1[i].get()
            i+=1

            #sql write
            if connection.is_connected():
                cur = connection.cursor()
                sql = 'INSERT INTO attendance values("{}","{}","{}","{}","{}","{}","{}")' \
                    .format(self.ithStudentName, self.ithStudentID, self.sec, self.subject, self.hour, self.ithStudentAtd,self.fTname)
                cur.execute(sql)
                connection.commit()
                cur.close()

        messagebox.showinfo("Done","Attendance has been registered",parent = attSc)
        attSc.destroy()


    def attScrn(self):
        self.sec = self.section1.get()
        self.subject = self.sub1.get()
        self.date = self.cal1.get()
        self.hour = self.hr1.get()
        print(self.sec,self.sub1,self.date,self.hour)

        if self.sec and self.subject and self.date and self.hour:

            if connection.is_connected():

                cursor = connection.cursor(buffered=TRUE)
                sql = 'SELECT Teacher_Name, Teacher_ID, Subject_Code from teacherSubject where Teacher_ID = "{}" and Subject_code ="{}"' \
                    .format(self.tID,self.subject)
                cursor.execute(sql)
                self.isReg = cursor.fetchall()
                if not self.isReg:
                    messagebox.showerror("Error","You have not registered for this course",parent = atStdnt)
                else:

                    sql = 'SELECT Student_Name, Student_ID from studentSubject where section = "{}" and subject_code ="{}"' \
                        .format(self.sec, self.subject)
                    cursor.execute(sql)
                    self.students = cursor.fetchall()

                    if not self.students:
                        messagebox.showerror("Error", "No students founds registered for this course",parent = atStdnt)

                    else:
                        global attSc
                        attSc = Toplevel()
                        attSc.geometry("500x300")
                        attSc.title("Attendance")
                        x1, x2 = 20, 130
                        y1, gap = 60, 30

                        # header
                        self.tHeader = Label(attSc, text="Attendance", bg=teacherColour, fg='white',
                                             font=("Sans serif", 16, "bold"), pady=6)  # text add
                        self.tHeader.pack(fill=X)  # pack is a must

                        gap = 40
                        x1 = 20
                        y1 = 100
                        x2 = 200
                        x3 = 360
                        self.studentNameLbl = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
                        self.sIDLbl1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
                        self.abPr1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
                        self.abPsntList = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
                        # name lbl
                        self.nameLbl = Label(attSc, text="Student Name: ", font=("Sans Serif", 15, 'bold'))
                        self.nameLbl.pack()
                        self.nameLbl.place(x=x1, y=50)

                        # USN Lbl
                        self.sIDLbl = Label(attSc, text="Student ID: ", font=("Sans Serif", 15, 'bold'))
                        self.sIDLbl.pack()
                        self.sIDLbl.place(x=x2, y=50)

                        i = 0
                        for self.ithStudent in self.students:
                            self.ithStudentName = self.ithStudent[0]
                            self.ithStudentID = self.ithStudent[1]
                            print(self.ithStudentName, self.ithStudentID)

                            # Name Label
                            self.studentNameLbl[i] = Label(attSc, text=self.ithStudentName, font=("Sans Serif", 12))
                            self.studentNameLbl[i].pack()
                            self.studentNameLbl[i].place(x=x1, y=y1 + i * gap)

                            # ID Label
                            self.sIDLbl1[i] = Label(attSc, text=self.ithStudentID, font=("Sans Serif", 12))
                            self.sIDLbl1[i].pack()
                            self.sIDLbl1[i].place(x=x2, y=y1 + i * gap)

                            # Absent Present
                            self.abPr1[i] = StringVar()
                            self.abPr1[i].set("Present")
                            self.abPsntList[i] = ttk.Combobox(attSc, textvariable=self.abPr1[i])
                            self.abPsntList[i]['values'] = ("Present", "Absent")
                            self.abPsntList[i].pack()
                            self.abPsntList[i].place(x=x3, y=y1 + i * gap, width=70)

                            i += 1

                        # submit btn
                        self.submitBtnIcn = PhotoImage(file='button_submitAttendance.png')
                        self.submitBtn = Button(attSc, image=self.submitBtnIcn, borderwidth=0, command=self.atReg)
                        self.submitBtn.pack()
                        self.submitBtn.place(x=x2 - 50, y=y1 + i * gap + 10)
                        attSc.mainloop()
        else:
            messagebox.showerror("Error","Please fill all details",parent = atStdnt)
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
    a2= att("Chempa","")
    a2