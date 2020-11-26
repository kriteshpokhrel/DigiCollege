from tkinter import *
from Homepage import *
from tkcalendar import DateEntry
import datetime
from db_connect import *
from tkinter import messagebox
global teacherColour
teacherColour = "#069ce5"

class asmt1:
    def __init__(self, logName,tID):
        self.logName = logName
        self.tID = tID
        global asst
        asst = Toplevel()
        asst.title('Assignment')
        asst.geometry("550x320")
        asst.resizable(width=FALSE,height=FALSE)
        self.gui_1()
        asst.mainloop()

    def asmtFinal(self):
        astSub = self.subject1.get()
        astName = self.sName1.get()
        astSec = self.sec1.get()
        astLink = self.astLk1.get()
        astDate = self.cal1.get_date()
        astRem = self.rem1.get()
        astTeacher = self.logName

        if connection.is_connected():
            mycursor = connection.cursor()
            sql = 'SELECT * from teachersubject where Teacher_name = "{}" and Teacher_ID = "{}" and Subject_Code = "{}"'.format(self.logName,
                                                                                                           self.tID,astSub)
            mycursor.execute(sql)
            wName = mycursor.fetchall()
            if not wName:
                messagebox.showinfo("Error", "You have not registered for this subject", parent=asst)
            else:
                if astSub and astName and astSec and astLink and astDate and astRem and astTeacher:
                    if connection.is_connected():
                        conn = connection.cursor()
                        sql = 'INSERT INTO assignment values("{}","{}","{}","{}","{}","{}","{}")'.format(astSub,astName,astSec,astLink,astDate,astRem,astTeacher)
                        conn.execute(sql)
                        connection.commit()
                        messagebox.showinfo("Done","Assignment updated.",parent = asst)
                else:
                    messagebox.showerror("Error","Please enter all fields.", parent = asst)

    def endAsmt(self):
        endSub = self.delSubject1.get()
        endDate = self.cal1.get_date()

        conn = connection.cursor()
        sql = 'SELECT * FROM assignment WHERE Assignment_Subject = "{}" and Asst_Sub_Date = "{}"'.format(
            endSub,endDate)
        res = conn.execute(sql)
        asstAll = conn.fetchall()
        print(endSub, endDate)
        if not asstAll:
            messagebox.showerror("Error","Please enter correct data.",parent=asstView)
        else:

            conn = connection.cursor()
            sql = 'DELETE FROM assignment where Assignment_Subject = "{}" and Asst_Sub_Date = "{}"'.format(endSub,endDate)
            conn.execute(sql)
            connection.commit()
            messagebox.showinfo("Done", "Assignment submission ended.", parent=asstView)

    def viewAsmt(self):

        conn = connection.cursor()
        sql = 'SELECT * FROM assignment WHERE Teacher = "{}"'.format(
            self.logName)
        res = conn.execute(sql)
        asstAll = conn.fetchall()
        print(asstAll)
        if asstAll:
            global asstView
            asstView = Toplevel()
            asstView.title('Assignment View')
            asstView.geometry("930x400")

            # frame
            self.frame1 = Frame(asstView)
            self.frame1.pack(side=TOP, fill=X)

            # header
            self.tHeader = Label(self.frame1, text="Assignment View", bg=teacherColour, fg='white',
                                 font=("Sans serif", 16, "bold"), pady=6)  # text add
            self.tHeader.pack(fill=X)  # pack is a must

            # btm frame
            btmFrame = Frame(asstView)
            btmFrame.pack(fill=X)
            btmFrame.place(y=50)
            # list assignments
            details = ["Subject", "Name", "Section", "Link", "Due_Date", "Remarks", "Teacher"]
            i = 0
            width1 = ["15", "25", "10", "35", "15", "30", "20"]
            # creating headings
            for j in range(len(details)):
                e = Entry(btmFrame, width=width1[j], bg=teacherColour)
                e.grid(row=i, column=j)
                e.insert(END, details[j])
            i += 1
            # inserting datasframe1
            for asstOne in asstAll:
                for j in range(len(asstOne)):
                    e = Entry(btmFrame, width=width1[j], bg='white')
                    e.grid(row=i, column=j)
                    e.insert(END, asstOne[j])
                i += 1

            # bottom frame
            btmFrame = Frame(asstView)
            btmFrame.pack(side= BOTTOM)
            ipa1=30
            # subject lbl
            self.subLbl = Label(btmFrame, text="Subject Code: ", font=("Sans Serif", 11))
            self.subLbl.grid(row =1,column = 1)

            # due date lbl
            self.dueDateLbl = Label(btmFrame, text="Due date:", font=("Sans Serif", 11))
            self.dueDateLbl.grid(row =2,column = 1)
            #self.dueDateLbl.place(x=400)

            #end submission btn
            self.endAsmtBtn = PhotoImage(file="button_endSubmission.png")
            self.endBtnLbl = Button(btmFrame, image=self.endAsmtBtn, borderwidth=0, command=self.endAsmt)
            self.endBtnLbl.grid(row =3,column=2)

            # subject Entry
            self.delSubject1 = Entry(btmFrame)
            self.delSubject1.grid(row=1, column =2)

            # date Entry
            d = datetime.date.today()
            self.cal1 = DateEntry(btmFrame, width=12, year=d.year, month=d.month, day=d.day,
                                  background=teacherColour, foreground='white', borderwidth=2)
            self.cal1.grid(row=2,column =2,pady=10)
            self.cal1.config(date_pattern='yyyy-mm-dd')

            asstView.mainloop()

        else:
            messagebox.showerror("Not found","You have not given any assignments",parent = asst)

    def gui_1(self):
        # header
        self.tHeader = Label(asst, text="Assignment", bg=teacherColour, fg='white',
                             font=("Sans serif", 16, "bold"), pady=6)  # text add
        self.tHeader.pack(fill=X)  # pack is a must

        x1, x2 = 20, 160
        y1, gap = 60, 30
        width1 = 200
        print("60")
        # subject lbl
        self.subLbl = Label(asst, text="Subject Code: ", font=("Sans Serif", 11))
        self.subLbl.pack()
        self.subLbl.place(x=x1, y=y1)

        # name lbl
        self.nameLbl = Label(asst, text="Assignment Name: ", font=("Sans Serif", 11))
        self.nameLbl.pack()
        self.nameLbl.place(x=x1, y=y1+gap)

        # section lbl
        self.sectionLbl = Label(asst, text="Section: ", font=("Sans Serif", 11))
        self.sectionLbl.pack()
        self.sectionLbl.place(x=x1, y=y1+2*gap)

        # assignment link lbl
        self.astLkLbl = Label(asst, text="Assignment Link: ", font=("Sans Serif", 11))
        self.astLkLbl.pack()
        self.astLkLbl.place(x=x1, y=y1 + 3 * gap)

        # due date lbl
        self.dueDateLbl = Label(asst, text="Due date:", font=("Sans Serif", 11))
        self.dueDateLbl.pack()
        self.dueDateLbl.place(x=x1, y=y1+4*gap)

        # remarks lbl
        self.reamarksLbl = Label(asst, text="Remarks", font=("Sans Serif", 11))
        self.reamarksLbl.pack()
        self.reamarksLbl.place(x=x1, y=y1+5*gap)

        #subjct Entry
        self.subject1 = Entry(asst)
        self.subject1.pack()
        self.subject1.place(x=x2,y=y1,width = width1)

        #name Entry
        self.sName1 = Entry(asst)
        self.sName1.pack()
        self.sName1.place(x=x2,y=y1+gap,width = width1)

        #section Entry
        self.sec1 = Entry(asst)
        self.sec1.pack()
        self.sec1.place(x=x2,y=y1+2*gap,width = width1)

        #asst link Entry
        self.astLk1 = Entry(asst)
        self.astLk1.pack()
        self.astLk1.place(x=x2,y=y1+3*gap,width = width1)

        # date entry
        d = datetime.date.today()
        self.cal1 = DateEntry(asst, width=12, year=d.year, month=d.month, day=d.day,
                              background=teacherColour, foreground='white', borderwidth=2)
        self.cal1.pack()
        self.cal1.config(date_pattern='yyyy-mm-dd')
        self.cal1.place(x=x2, y=y1 + 4 * gap)

        #remarks Entry
        self.rem1 = Entry(asst)
        self.rem1.pack()
        self.rem1.place(x=x2,y=y1+5*gap,width = width1)

        #submit button
        self.submitBtn = PhotoImage(file = "button_submitTeacherSmall.png")
        self.submitBtnLbl =Button(asst, image = self.submitBtn, borderwidth = 0,command = self.asmtFinal)
        self.submitBtnLbl.pack()
        self.submitBtnLbl.place(x=x2,y=y1+6*gap)

        #viewAllAsst button
        self.viewAllAsmtBtn = PhotoImage(file = "button_viewYourAssignments.png")
        self.submitBtnLbl =Button(asst, image = self.viewAllAsmtBtn, borderwidth = 0,command = self.viewAsmt)
        self.submitBtnLbl.pack()
        self.submitBtnLbl.place(x=2*x2,y=y1+7*gap+10)

if __name__ == "__main__" :
    v1= asmt1("Chempa")
    v1