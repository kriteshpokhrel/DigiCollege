from tkinter import *
from teacherSettings import *
from viewClassroom import *
from studentSettings import *
from studentSubject import *
global studentColour
studentColour = "#f2820d"
class sHome:
    def __init__(self, sLogName,sec,sID):
        global sHome1
        self.logName = sLogName
        self.sec = sec
        self.sID =sID
        sHome1= Toplevel()
        sHome1.geometry("480x480")
        sHome1.title("Students Home Page")
        sHome1.resizable(width=FALSE,height=FALSE)
        self.gui_1(sLogName)
        sHome1.mainloop()
    def settingsOpen(self):
        s1= settingsStudent(self.logName)
        s1
    def booksIssued(self):
        #sql
        global listBDB
        listIsBook = Toplevel()
        listIsBook.geometry('1100x500')
        listIsBook.title("Books Issued")
        listIsBook.resizable(width=FALSE,height=FALSE)

        # frame1
        frame1 = Frame(listIsBook)
        frame1.pack(side=TOP, fill=X)
        # DB header
        dbHeader = Label(frame1, text="Books Issued", bg=studentColour, fg='white',
                         font=("Sans serif", 20, "bold"), pady=10)  # text add
        dbHeader.pack(fill=X)  # pack is a must

        # frame1
        frame2 = Frame(listIsBook)
        frame2.pack(fill=X)
        frame2.place(y=120)

        # DB SQL
        conn = connection.cursor()
        sql = 'SELECT * FROM booksIssued where Student_Name = "{}"'.format(self.logName)
        res = conn.execute(sql)
        ww = conn.fetchall()
        i = 1
        print(ww)
        totalBooksIssued = len(ww)
        details = ["BookName", "BookID", "Student_Name","Student_ID", "Issue_date", "Return_Date","Remarks"]
        # display total books
        print(totalBooksIssued)
        if totalBooksIssued ==0:
            listIsBook.destroy()
            messagebox.showerror("Error","No books have been issued",parent = sHome1)
        else:
            totBooksLbl = Label(listIsBook, text='Total Books Issued: ' + str(totalBooksIssued), font=('bold', 15))
            totBooksLbl.pack()
            totBooksLbl.place(x=10, y=65)
            i = 0
            width1 = ["50", "15", "30","15", "15","15","50"]
            # creating headings
            for j in range(len(details)):
                e = Entry(frame2, width=width1[j], bg=studentColour)
                e.grid(row=i, column=j)
                e.insert(END, details[j])
            i += 1
            # inserting datas
            j=0
            for books in ww:
                for j in range(len(books)):
                    e = Entry(frame2, width=width1[j], bg='white')
                    e.grid(row=i, column=j)
                    e.insert(END, books[j])
                i += 1
            listIsBook.mainloop()

    def asmtStdnt(self):
        global asmtStdnt1
        asmtStdnt1 = Toplevel()
        asmtStdnt1.geometry('930x300')
        asmtStdnt1.title("Assignments")
        asmtStdnt1.resizable(width=FALSE,height=FALSE)
        # top Frame
        topFrame = Frame(asmtStdnt1)
        topFrame.pack(side=TOP, fill=X)
        # header
        self.tHeader = Label(topFrame, text="Assignments", bg=studentColour, fg='white',
                             font=("Sans serif", 16, "bold"), pady=6)  # text add
        self.tHeader.pack(fill=X)  # pack is a must

        # btm frame
        btmFrame = Frame(asmtStdnt1)
        btmFrame.pack(fill=X)
        btmFrame.place(y=50)
        conn = connection.cursor()
        sql = 'SELECT * FROM assignment WHERE Section = "{}"'.format(
            self.sec)
        res = conn.execute(sql)
        asmtLst = conn.fetchall()

        details = ["Subject", "Name", "Section", "Link", "Due_Date", "Remarks", "Teacher"]
        i = 0
        width1 = ["15", "25", "10", "35", "15", "30", "20"]
        # creating headings
        for j in range(len(details)):
            e = Entry(btmFrame, width=width1[j], bg=studentColour)
            e.grid(row=i, column=j)
            e.insert(END, details[j])
        i += 1
        # inserting datasframe1,pc
        for asmt in asmtLst:
            for j in range(len(asmt)):
                e = Entry(btmFrame, width=width1[j], bg='white')
                e.grid(row=i, column=j)
                e.insert(END, asmt[j])
            i += 1

        asmtStdnt1.mainloop()
    def changeView(self):
        atdnSdt1.destroy()
        global atdnSdt2
        atdnSdt2 = Toplevel()
        atdnSdt2.geometry("300x200")
        atdnSdt2.title("Attendance")
        atdnSdt2.resizable(width=FALSE,height=FALSE)
        # top Frame
        topFrame = Frame(atdnSdt2)
        topFrame.pack(side=TOP, fill=X)
        # header
        textDis = " Attendance"
        self.sHeaderAtd = Label(topFrame, text=textDis, bg=studentColour, fg='white',
                                font=("Sans serif", 16, "bold"), pady=6)  # text add
        self.sHeaderAtd.pack(fill=X)  # pack is a must

        conn = connection.cursor()

        # extract attendance
        sql = 'SELECT Subject_ID, Status, count(*) from attendance WHERE Student_Name = "{}" and Student_ID ="{}" GROUP BY Status,Subject_ID' \
            .format(self.logName, self.sID)
        res = conn.execute(sql)
        ww = conn.fetchall()
        print(ww)
        details = ["Subject_ID", "Status", "Count"]
        i = 0
        width1 = ["20", "20", "10"]

        #creating frames for insertion  btm frame
        btmFrame = Frame(atdnSdt2)
        btmFrame.pack(fill=X)
        btmFrame.place(y=50)
        conn = connection.cursor()
        print(self.logName, self.sID)

        # creating headings
        for j in range(len(details)):
            e = Entry(btmFrame, width=width1[j], bg=studentColour)
            e.grid(row=i, column=j)
            e.insert(END, details[j])
        i += 1
        # inserting datasframe1,pc
        for atdSub in ww:
            for j in range(len(atdSub)):
                e = Entry(btmFrame, width=width1[j], bg='white')
                e.grid(row=i, column=j)
                e.insert(END, atdSub[j])
            i += 1

        atdnSdt2.mainloop()

    def atdnceStdnt(self):
        global atdnSdt1
        atdnSdt1 = Toplevel()
        atdnSdt1.geometry("540x400")
        atdnSdt1.title("Attendance")
        atdnSdt1.resizable(width=FALSE,height=FALSE)
        # top Frame
        topFrame = Frame(atdnSdt1)
        topFrame.pack(side=TOP, fill=X)
        # header
        textDis = " Attendance"
        self.sHeaderAtd = Label(topFrame, text=textDis, bg=studentColour, fg='white',
                             font=("Sans serif", 16, "bold"), pady=6)  # text add
        self.sHeaderAtd.pack(fill=X)  # pack is a must

        # btm frame
        btmFrame = Frame(atdnSdt1)
        btmFrame.pack(fill=X)
        btmFrame.place(y=50)
        conn = connection.cursor()
        # btm frame
        realBtmFrame = Frame(atdnSdt1)
        realBtmFrame.pack(fill=X,side=BOTTOM)
        conn = connection.cursor()
        print(self.logName, self.sID)

        #Change View button
        self.chgViewIcn =PhotoImage(file = "button_changeViewAttendance.png")
        self.chgViewIcBtn =Button(realBtmFrame, image = self.chgViewIcn,borderwidth = 0,command = self.changeView)
        self.chgViewIcBtn.pack()

        #extract attendance
        sql = 'SELECT Subject_ID, Attendance_Hour, Status, By_Teacher FROM attendance WHERE Student_Name = "{}" and Student_ID ="{}"'\
            .format(self.logName,self.sID)
        res = conn.execute(sql)
        ww = conn.fetchall()
        print(ww)
        details = ["Subject_ID","Hour","Status","By_Teacher"]
        i = 0
        width1 = ["20", "15", "15", "20"]
        # creating headings
        for j in range(len(details)):
            e = Entry(btmFrame, width=width1[j], bg=studentColour)
            e.grid(row=i, column=j)
            e.insert(END, details[j])
        i += 1
        # inserting datasframe1,pc
        for atdHstry in ww:
            for j in range(len(atdHstry)):
                e = Entry(btmFrame, width=width1[j], bg='white')
                e.grid(row=i, column=j)
                e.insert(END, atdHstry[j])
            i += 1


        atdnSdt1.mainloop()

    def stdntSub(self):
        s1= studentSub(self.logName,self.sec,self.sID)
        s1
    def gui_1(self,sLogName):

        #header
        textDis = 'Welcome ' + sLogName
        self.tHeader = Label(sHome1, text=textDis, bg=studentColour, fg='white',
                             font=("Sans serif", 18, "bold"), pady=8)  # text add
        self.tHeader.pack(fill=X)  # pack is a must

        x1Icn,x2Icn=70,270
        x1Btn,x2Btn=62,260
        y1Icn,y2Icn=70,260
        y1Btn,y2Btn = 200,390

        # books Issued button
        self.bkIssuedBtnIcon = PhotoImage(file = "button_booksIssued.png")
        self.bkIssuedBtn = Button(sHome1, image = self.bkIssuedBtnIcon, borderwidth = 0,command = self.booksIssued)
        self.bkIssuedBtn.pack()
        self.bkIssuedBtn.place(x= x1Btn,y= y1Btn)

        # assignment button
        self.asmtBtnIcon = PhotoImage(file = "button_assignmentStudent.png")
        self.asmtBtn = Button(sHome1, image = self.asmtBtnIcon, borderwidth = 0,command = self.asmtStdnt)
        self.asmtBtn.pack()
        self.asmtBtn.place(x= x1Btn,y= y2Btn)

        # attendance button
        self.atdnceBtnIcon = PhotoImage(file = "button_attendanceStudent.png")
        self.atdnceBtn = Button(sHome1, image = self.atdnceBtnIcon, borderwidth = 0,command = self.atdnceStdnt)
        self.atdnceBtn.pack()
        self.atdnceBtn.place(x= x2Btn,y= y1Btn )

        # subjects button
        self.subBtnIcon = PhotoImage(file = "button_subjectsStudent.png")
        self.subBtn = Button(sHome1, image = self.subBtnIcon, borderwidth = 0,command = self.stdntSub)
        self.subBtn.pack()
        self.subBtn.place(x= x2Btn,y= y2Btn )


        # book Issued photo
        self.yClrPhoto= PhotoImage(file = "icon_booksIssuedStudent.png")
        yClrPhotoLbl = Label(sHome1, image= self.yClrPhoto)
        yClrPhotoLbl.pack()
        yClrPhotoLbl.place(x= x1Icn,y= y1Icn )

        # assignment photo
        self.asmtPhoto= PhotoImage(file = "icon_asssignmentStudent.png")
        asmtPhotoLbl = Label(sHome1, image= self.asmtPhoto)
        asmtPhotoLbl.pack()
        asmtPhotoLbl.place(x= x1Icn, y= y2Icn)

        #attendance photo
        self.atdncePhoto = PhotoImage(file ='icon_attendanceStudent.png')
        atdncePhotoLbl =Label(sHome1, image = self.atdncePhoto)
        atdncePhotoLbl.pack()
        atdncePhotoLbl.place(x=x2Icn, y=y1Icn)

        #subject photo
        self.subPhoto = PhotoImage(file ='icon_subStudent.png')
        subPhotoLbl =Label(sHome1, image = self.atdncePhoto)
        subPhotoLbl.pack()
        subPhotoLbl.place(x=x2Icn, y=y2Icn)

        # settings button
        self.settingsBtnIcon = PhotoImage(file ="button_settingsStudent.png")
        self.settingsBtn = Button(sHome1, image = self.settingsBtnIcon, borderwidth = 0,command = self.settingsOpen)
        self.settingsBtn.pack()
        self.settingsBtn.place(x=x2Icn+150, y='60')


if __name__ == "__main__":
    t1= sHome("Kritesh Pokhrel","5C","123")
    t1
