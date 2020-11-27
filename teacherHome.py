from tkinter import *
from Homepage import *
from teacherSettings import *
from viewClassroom import *
from attendanceStudent import *
from assignmentTeacher import *
from teacherSubject import *

global teacherColour
teacherColour = "#069ce5"
class tHome:
    def __init__(self, sal,tLogName,tID):
        global tHome1
        self.logName = tLogName
        self.sal = sal
        self.tID= tID
        self.fTname = self.sal + " "+ self.logName
        tHome1= Toplevel()
        tHome1.geometry("480x480")
        tHome1.title("Teacher's Home Page")
        tHome1.resizable(width=FALSE,height=FALSE)
        self.gui_1(tLogName)
        tHome1.mainloop()
    def settingsOpen(self):
        s1= settingsTeacher(self.sal,self.logName,self.tID)
        s1
    def classRoom(self):
        if connection.is_connected():
            my_conn = connection.cursor()
            sql = 'SELECT Class_teacherOf from teachers where t_name = "{}" and t_id = "{}" '.format(self.logName,self.tID)
            my_conn.execute(sql)
            wName = my_conn.fetchone()
            self.sec1= wName[0]
            if (self.sec1 == "None") or (self.sec1 == "none"):
                messagebox.showerror("Error","You have not been appointed as class teacher of any section", parent = tHome1)
            else:
                cl1= vClass(self.logName,self.sec1,self.tID)
                cl1
    def attendance(self):
        a1= att(self.fTname,self.tID)
        a1
    def assignment(self):
        as1 = asmt1(self.logName,self.tID)
        as1
    def subjects(self):
        sub1= teacherSub(self.logName,self.tID)
        sub1
    def gui_1(self,tLogName):

        #header
        textDis = 'Welcome ' + self.sal + " " + self.logName
        self.tHeader = Label(tHome1, text=textDis, bg=teacherColour, fg='white',
                             font=("Sans serif", 16, "bold"), pady=6)  # text add
        self.tHeader.pack(fill=X)  # pack is a must

        x1Icn,x2Icn=70,270
        x1Btn,x2Btn=62,260
        y1Icn,y2Icn=70,260
        y1Btn,y2Btn = 200,390
        # your class button
        self.yClassBtnIcon = PhotoImage(file = "button_yrClassroom.png")
        self.yClassBtn = Button(tHome1, image = self.yClassBtnIcon, borderwidth = 0,command = self.classRoom)
        self.yClassBtn.pack()
        self.yClassBtn.place(x= x1Btn,y= y1Btn)

        # attendance button
        self.attendanceBtnIcon = PhotoImage(file = "button_attendanceTeacher.png")
        self.attendanceBtn = Button(tHome1, image = self.attendanceBtnIcon, borderwidth = 0,command = self.attendance)
        self.attendanceBtn.pack()
        self.attendanceBtn.place(x= x2Btn,y= y1Btn)


        # assignment button
        self.assnmtBtnIcon = PhotoImage(file = "button_assignmentTeacher.png")
        self.assnmtBtn = Button(tHome1, image = self.assnmtBtnIcon, borderwidth = 0,command = self.assignment)
        self.assnmtBtn.pack()
        self.assnmtBtn.place(x= x1Btn,y= y2Btn )

        # subjects button
        self.subBtnIcon = PhotoImage(file = "button_subjectsTeacher.png")
        self.subBtn = Button(tHome1, image = self.subBtnIcon, borderwidth = 0,command = self.subjects)
        self.subBtn.pack()
        self.subBtn.place(x= x2Btn,y= y2Btn )

        # your class photo
        self.yClrPhoto= PhotoImage(file = "icon_yrClassroom.png")
        yClrPhotoLbl = Label(tHome1, image= self.yClrPhoto)
        yClrPhotoLbl.pack()
        yClrPhotoLbl.place(x= x1Icn, y= y1Icn)

        #attendance photo
        self.atdPhoto = PhotoImage(file="icon_attendanceTeacher.png")
        atdLbl = Label(tHome1, image=self.atdPhoto)
        atdLbl.pack()
        atdLbl.place(x=x2Icn, y=y1Icn)

        #assignment photo
        self.asmtPhoto = PhotoImage(file="icon_assignmentTeacher.png")
        self.asmt = Label(tHome1, image=self.asmtPhoto)
        self.asmt.pack()
        self.asmt.place(x=x1Icn, y=y2Icn)

        #subjects photo
        self.subPhoto = PhotoImage(file="icon_subTeacher.png")
        self.sub = Label(tHome1, image=self.subPhoto)
        self.sub.pack()
        self.sub.place(x=x2Icn, y=y2Icn)

        # settings button
        self.settingsBtnIcon = PhotoImage(file ="button_settingsTeacher.png")
        self.settingsBtn = Button(tHome1, image = self.settingsBtnIcon, borderwidth = 0,command = self.settingsOpen)
        self.settingsBtn.pack()
        self.settingsBtn.place(x= x2Icn+150,y= '50')

if __name__ == "__main__":
    t1= tHome("","","")
    t1
