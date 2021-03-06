from tkinter import *
from db_connect import *
from tkinter import messagebox
from teacherHome import *
from Homepage import *
from digiFaceTeacher import *
global teacherColour
teacherColour = "#069ce5"

class settingsTeacher:
    def __init__(self,sal, tLogName,tID):
        global settings1
        self.tLogName = tLogName
        self.tID = tID
        self.sal = sal
        settings1 = Toplevel()
        settings1.title("Settings")
        settings1.geometry("310x280")
        settings1.resizable(width=FALSE, height= FALSE)
        self.gui_1()
        settings1.mainloop()

    def changePwd1(self):
        curPwd = self.cPwd1.get()
        newPwd1 = self.nPwd1.get()
        newPwd2 = self.nPwd2.get()
        if connection.is_connected():
            mycursor = connection.cursor()
            sql = 'SELECT * from teachers where t_name = "{}" and Password = "{}" and T_ID = "{}"'.format(self.tLogName, curPwd,self.tID)
            mycursor.execute(sql)
            wName = mycursor.fetchall()
            if not wName:
                messagebox.showinfo("Password Error", "Please enter correct current Password", parent=chgPwd)

            else:
                # if success
                if newPwd1 == newPwd2:
                    if newPwd1 != curPwd:

                        ###SQL COMMAND HERE
                        mySql_insert_query = 'UPDATE teachers SET password = "{}" WHERE T_Name = "{}" and T_ID ="{}"'.format(
                            newPwd1, self.tLogName,self.tID)
                        cursor = connection.cursor()
                        cursor.execute(mySql_insert_query)
                        connection.commit()
                        chgPwd.destroy()
                        messagebox.showinfo("Password Change Complete", "Password Changed successfully.", parent=chgPwd)
                    else:
                        messagebox.showinfo("Password Error", "New and old passwords cannot be same", parent=chgPwd)

                else:
                    messagebox.showinfo("Password Error", "Passwords do not match", parent=chgPwd)

            mycursor.close()
        else:
            print("DBMS not connected")

    def changePassword(self):
        global chgPwd
        chgPwd = Toplevel()
        chgPwd.geometry("450x230")
        chgPwd.title("Change Password")
        # header
        chPwdHeader = Label(chgPwd, text="Change Password", bg=teacherColour, fg='white',
                            font=("Sans serif", 16, "bold"), pady=7)  # text add
        chPwdHeader.pack(fill=X)  # pack is a must

        x1, x2 = 20, 145
        y1, gap = 70, 35
        width1 = 220
        # Current Password
        self.curPwLbl = Label(chgPwd, text="Current Password: ", font=("Sans Serif", 10))
        self.curPwLbl.pack()
        self.curPwLbl.place(x=x1, y=y1)

        # New Password
        self.newPwLbl = Label(chgPwd, text="New  Password: ", font=("Sans Serif", 10))
        self.newPwLbl.pack()
        self.newPwLbl.place(x=x1, y=y1 + gap)

        # Confirm Password
        self.cfNewPwLbl = Label(chgPwd, text="Confirm Password: ", font=("Sans Serif", 10))
        self.cfNewPwLbl.pack()
        self.cfNewPwLbl.place(x=x1, y=y1 + 2 * gap)

        # Current Password text field
        self.cPwd1 = Entry(chgPwd)
        self.cPwd1.pack()
        self.cPwd1.place(x=x2, y=y1, width=width1)

        def showHideState():
            if var1.get():
                self.nPwd1.config(show="")
                self.nPwd2.config(show="")

            else:
                self.nPwd1.config(show="*")
                self.nPwd2.config(show="*")

        # New Password text field
        self.nPwd1 = Entry(chgPwd, show="*")
        self.nPwd1.pack()
        self.nPwd1.place(x=x2, y=y1 + gap, width=width1)

        # Confirm New Password text field
        self.nPwd2 = Entry(chgPwd, show="*")
        self.nPwd2.pack()
        self.nPwd2.place(x=x2, y=y1 + 2 * gap, width=width1)

        # change pwd button
        self.changePwdBtnIcon1 = PhotoImage(file="button_confPwdTeacher.png")
        self.changePwdBtn = Button(chgPwd, image=self.changePwdBtnIcon1, borderwidth=0, command=self.changePwd1)
        self.changePwdBtn.pack()
        self.changePwdBtn.place(x=x2, y=y1 + 2 * gap + 30)

        # showPassword Box
        var1 = IntVar()
        chk = Checkbutton(chgPwd, text="Show", variable=var1, command=showHideState)
        chk.pack()
        chk.place(x=x2 + width1 + 10, y=y1 + 2 * gap)

        chgPwd.mainloop()

    def cTeacher(self):
        self.secNew = self.enterSec.get()
        mySql_insert_query = 'UPDATE teachers SET Class_teacherOf = "{}" WHERE T_Name = "{}" and T_ID = "{}"'.format(
            self.secNew, self.tLogName,self.tID)
        cursor = connection.cursor()
        cursor.execute(mySql_insert_query)
        connection.commit()
        if (self.secNew != "None") and (self.secNew != "none"):
            messagebox.showinfo("Success", "You have been appointed as class teacher of {}.".format(self.secNew),
                                parent=appotCt)
        else:
            messagebox.showinfo("Success", "Class teacher removed.", parent=appotCt)
        appotCt.destroy()

    def apptCt(self):
        global appotCt
        appotCt = Toplevel()
        appotCt.geometry("280x130")
        appotCt.title("Class Teacher Appoint")
        # header
        self.apptHeader = Label(appotCt, text="Appoint as Class Teacher", bg=teacherColour, fg='white',
                                font=("Sans serif", 13, "bold"), pady=6)  # text add
        self.apptHeader.pack(fill=X)  # pack is a must

        # entersec
        self.enterSecLbl = Label(appotCt, text="Please enter Section: ", font=("Sans Serif", '11'))
        self.enterSecLbl.pack()
        self.enterSecLbl.place(x=15, y=50)

        # entersecNone
        self.noneLbl = Label(appotCt, text="(None to remove)", font=("Sans Serif", '8'))
        self.noneLbl.pack()
        self.noneLbl.place(x=157, y=52.5)

        # section entry
        self.enterSec = Entry(appotCt)
        self.enterSec.pack()
        self.enterSec.place(x=15, y=80, width=145, height=20)

        # confirm button
        self.settingsBtnIcon = PhotoImage(file="button_confirmTeacher.png")
        self.settingsBtn = Button(appotCt, image=self.settingsBtnIcon, borderwidth=0, command=self.cTeacher)
        self.settingsBtn.pack()
        self.settingsBtn.place(x=170, y=78)

        appotCt.mainloop()

    def delAct(self):
        cnfrm = messagebox.askquestion('Delete Account', 'Are you sure that you want to delete your account?',
                                       icon='warning', parent=settings1)
        if cnfrm == 'yes':
            ###SQL COMMAND HERE
            # del from teachers
            mySql_insert_query = 'DELETE FROM teachers  WHERE T_Name = "{}" and T_ID = "{}"'.format(
                self.tLogName,self.tID)
            cursor = connection.cursor()
            cursor.execute(mySql_insert_query)
            connection.commit()

            #del from subjects
            sql = 'DELETE FROM teachersubject WHERE Teacher_Name = "{}" and Teacher_ID = "{}"'.format(
                self.tLogName, self.tID)
            cursor = connection.cursor()
            cursor.execute(sql)
            connection.commit()
            cursor.close()
            messagebox.showinfo("Account Deleted", "Your account has been deleted successfully", parent=settings1)
            settings1.destroy()
    def dFace(self):
        #checking if data already exists
        mycursor = connection.cursor()
        sql = 'SELECT * from digiFaceTeacher where t_ID = "{}" '.format(self.tID)
        mycursor.execute(sql)
        dExists= mycursor.fetchall()
        if dExists:
            messagebox.showerror("Error","DigiFace has already been setup",parent = settings1)
        else:
            d1= digiFaceTeacher1(self.sal,self.tLogName,self.tID)
            d1

    def gui_1(self):
        #header
        self.settingsHeader = Label(settings1, text="Settings", bg=teacherColour, fg='white',
                                    font=("Sans serif", 18, "bold"), pady=7)  # text add
        self.settingsHeader.pack(fill=X)  # pack is a must

        # change pwd button
        self.changePwdBtnIcon = PhotoImage(file="button_changePasswordTeacher.png")
        self.changePwdBtn = Button(settings1, image=self.changePwdBtnIcon, borderwidth=0, command=self.changePassword)
        self.changePwdBtn.pack()
        self.changePwdBtn.place(x=40, y=70)

        # appoint as class teacher
        self.cTeacherBtnIcon = PhotoImage(file="button_appointClassTeacher.png")
        self.cTeacherBtn = Button(settings1, image=self.cTeacherBtnIcon, borderwidth=0, command=self.apptCt)
        self.cTeacherBtn.pack()
        self.cTeacherBtn.place(x=40, y=120)


        # delete account
        self.delAcntBtnIcon = PhotoImage(file="button_deleteAccountTeacher.png")
        self.delAcntBtn = Button(settings1, image=self.delAcntBtnIcon, borderwidth=0, command=self.delAct)
        self.delAcntBtn.pack()
        self.delAcntBtn.place(x=40, y=170)

        # digiFace account
        self.dFaceBtnIcon = PhotoImage(file="button_setUpDigifaceTeacher.png")
        self.dFaceBtn = Button(settings1, image=self.dFaceBtnIcon, borderwidth=0, command=self.dFace)
        self.dFaceBtn.pack()
        self.dFaceBtn.place(x=40, y=220)

if __name__ == '__main__':
    s1 = settingsTeacher("","","")
    s1
