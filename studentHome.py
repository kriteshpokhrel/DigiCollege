from tkinter import *
from teacherSettings import *
from viewClassroom import *
from studentSettings import *
global studentColour
studentColour = "#f2820d"
class sHome:
    def __init__(self, sLogName,sec):
        global sHome1
        self.logName = sLogName
        self.sec = sec
        sHome1= Toplevel()
        sHome1.geometry("640x360")
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


    def gui_1(self,sLogName):

        #header
        textDis = 'Welcome ' + sLogName
        self.tHeader = Label(sHome1, text=textDis, bg=studentColour, fg='white',
                             font=("Sans serif", 16, "bold"), pady=6)  # text add
        self.tHeader.pack(fill=X)  # pack is a must

        # books Issued button
        self.bkIssuedBtnIcon = PhotoImage(file = "button_booksIssued.png")
        self.bkIssuedBtn = Button(sHome1, image = self.bkIssuedBtnIcon, borderwidth = 0,command = self.booksIssued)
        self.bkIssuedBtn.pack()
        self.bkIssuedBtn.place(x= '62',y= '200')

        # assignment button
        self.asmtBtnIcon = PhotoImage(file = "button_assignmentStudent.png")
        self.asmtBtn = Button(sHome1, image = self.asmtBtnIcon, borderwidth = 0,command = self.asmtStdnt)
        self.asmtBtn.pack()
        self.asmtBtn.place(x= '240',y= '200')

        # book Issued photo
        self.yClrPhoto= PhotoImage(file = "icon_booksIssuedStudent.png")
        yClrPhotoLbl = Label(sHome1, image= self.yClrPhoto)
        yClrPhotoLbl.pack()
        yClrPhotoLbl.place(x= "70", y= "70")

        # assignment photo
        self.asmtPhoto= PhotoImage(file = "icon_asssignmentStudent.png")
        asmtPhotoLbl = Label(sHome1, image= self.asmtPhoto)
        asmtPhotoLbl.pack()
        asmtPhotoLbl.place(x= "250", y= "70")

        # settings button
        self.settingsBtnIcon = PhotoImage(file ="button_settingsStudent.png")
        self.settingsBtn = Button(sHome1, image = self.settingsBtnIcon, borderwidth = 0,command = self.settingsOpen)
        self.settingsBtn.pack()
        self.settingsBtn.place(x= '585',y= '308')


if __name__ == "__main__":
    t1= sHome("","")
    t1
