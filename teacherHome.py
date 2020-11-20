from tkinter import *
from Homepage import *
from teacherSettings import *
from viewClassroom import *
from attendanceStudent import *
from assignmentTeacher import *
global teacherColour
teacherColour = "#069ce5"
class tHome:
    def __init__(self, sal,tLogName):
        global tHome1
        self.logName = tLogName
        self.sal = sal
        tHome1= Toplevel()
        tHome1.geometry("640x270")
        tHome1.title("Teacher's Home Page")
        tHome1.resizable(width=FALSE,height=FALSE)
        self.gui_1(tLogName)
        tHome1.mainloop()
    def settingsOpen(self):
        s1= settingsTeacher(self.logName)
        s1
    def classRoom(self):
        if connection.is_connected():
            my_conn = connection.cursor()
            sql = 'SELECT Class_teacherOf from teachers where t_name = "{}"'.format('chempa')
            my_conn.execute(sql)
            wName = my_conn.fetchone()
            print(wName)
            self.sec1= wName[0]
            print(self.sec1)
            if (self.sec1 == "None") or (self.sec1== "none"):
                messagebox.showerror("Error","You have not been appointed as class teacher of any section", parent = tHome1)
            else:
                cl1= vClass(self.logName,self.sec1)
                cl1
    def attendance(self):
        a1= att()
        a1
    def assignment(self):
        as1 = asmt1()
        as1
    def gui_1(self,tLogName):

        #header
        textDis = 'Welcome ' + self.sal + " " + self.logName
        self.tHeader = Label(tHome1, text=textDis, bg=teacherColour, fg='white',
                             font=("Sans serif", 16, "bold"), pady=6)  # text add
        self.tHeader.pack(fill=X)  # pack is a must

        # your class button
        self.yClassBtnIcon = PhotoImage(file = "button_yrClassroom.png")
        self.yClassBtn = Button(tHome1, image = self.yClassBtnIcon, borderwidth = 0,command = self.classRoom)
        self.yClassBtn.pack()
        self.yClassBtn.place(x= '62',y= '200')

        # attendance button
        self.attendanceBtnIcon = PhotoImage(file = "button_attendanceTeacher.png")
        self.attendanceBtn = Button(tHome1, image = self.attendanceBtnIcon, borderwidth = 0,command = self.attendance)
        self.attendanceBtn.pack()
        self.attendanceBtn.place(x= '240',y= '200')


        # assignment button
        self.assnmtBtnIcon = PhotoImage(file = "button_assignmentTeacher.png")
        self.assnmtBtn = Button(tHome1, image = self.assnmtBtnIcon, borderwidth = 0,command = self.assignment)
        self.assnmtBtn.pack()
        self.assnmtBtn.place(x= '418',y= '200')

        # your class photo
        self.yClrPhoto= PhotoImage(file = "icon_yrClassroom.png")
        yClrPhotoLbl = Label(tHome1, image= self.yClrPhoto)
        yClrPhotoLbl.pack()
        yClrPhotoLbl.place(x= "70", y= "70")

        #attendance photo
        self.atdPhoto = PhotoImage(file="icon_attendanceTeacher.png")
        atdLbl = Label(tHome1, image=self.atdPhoto)
        atdLbl.pack()
        atdLbl.place(x="250", y="70")

        #attendance photo
        self.asmtPhoto = PhotoImage(file="icon_assignmentTeacher.png")
        self.asmt = Label(tHome1, image=self.asmtPhoto)
        self.asmt.pack()
        self.asmt.place(x="430", y="70")



        # settings button
        self.settingsBtnIcon = PhotoImage(file ="button_settingsTeacher.png")
        self.settingsBtn = Button(tHome1, image = self.settingsBtnIcon, borderwidth = 0,command = self.settingsOpen)
        self.settingsBtn.pack()
        self.settingsBtn.place(x= '580',y= '50')





if __name__ == "__main__":
    t1= tHome("","")
    t1
