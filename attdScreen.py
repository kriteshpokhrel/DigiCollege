from tkinter import *
from db_connect import *
from tkinter import messagebox
from tkinter import ttk

global teacherColour
teacherColour = "#069ce5"

class att1:
    def atReg(self):
        i=0
        for self.ithStudent in self.students:
            self.ithStudentName = self.ithStudent[0]
            self.ithStudentID = self.ithStudent[1]
            self.ithStudentAtd  =self.abPr1[i].get()
            i+=1
            print((self.ithStudentName,self.ithStudentID,self.ithStudentAtd))

        self.sec = "5C"
        self.subject = "19CSE45"
        self.date = "gg"
        self.hour = "34"

        if self.sec and self.subject and self.date and self.hour:

            if connection.is_connected():
                cursor = connection.cursor()
                sql = 'SELECT Student_Name, Student_ID from studentSubject where section = "{}" and subject_code ="{}"'\
                            .format(self.sec,self.subject)
                cursor.execute(sql)
                self.students= cursor.fetchall()

                if not self.students:
                    messagebox.showerror("Error", "No students founds registered for this course")

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
                    x1=20
                    y1=100
                    x2=200
                    x3=360
                    self.studentNameLbl = [0,1,2,3,4,5,6,7,8,9]
                    self.sIDLbl1 = [0,1,2,3,4,5,6,7,8,9]
                    self.abPr1 = [0,1,2,3,4,5,6,7,8,9]
                    self.abPsntList = [0,1,2,3,4,5,6,7,8,9]
                    # name lbl
                    self.nameLbl = Label(attSc, text="Student Name: ", font=("Sans Serif", 15,'bold'))
                    self.nameLbl.pack()
                    self.nameLbl.place(x=x1, y=50)

                    # USN Lbl
                    self.sIDLbl = Label(attSc, text="Student ID: ", font=("Sans Serif",15,'bold'))
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
                        self.studentNameLbl[i].place(x=x1, y=y1+i*gap)

                        # ID Label
                        self.sIDLbl1[i] = Label(attSc, text=self.ithStudentID, font=("Sans Serif", 12))
                        self.sIDLbl1[i].pack()
                        self.sIDLbl1[i].place(x=x2, y=y1+i*gap)

                        #Absent Present
                        self.abPr1[i] = StringVar()
                        self.abPr1[i].set("Present")
                        self.abPsntList[i] = ttk.Combobox(attSc, textvariable=self.abPr1[i])
                        self.abPsntList[i]['values'] = ("Present","Absent")
                        self.abPsntList[i].pack()
                        self.abPsntList[i].place(x=x3, y=y1 + i * gap, width=70)


                        i+=1


                    #submit btn
                    self.submitBtnIcn = PhotoImage(file = 'button_submitAttendance.png')
                    self.submitBtn = Button(attSc, image = self.submitBtnIcn,borderwidth = 0, command = self.atReg)
                    self.submitBtn.pack()
                    self.submitBtn.place(x=x2-50,y=y1+ i*gap+10)
                    attSc.mainloop()

v1=att1()
v1