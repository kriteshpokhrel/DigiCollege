from tkinter import *
from db_connect import *
from tkinter import messagebox
from teacherHome import *
from Homepage import *

global studentColour
studentColour = "#f2820d"
0
class settingsStudent:
    def __init__(self, sLogName,sID):
        global settings1
        self.sLogName = sLogName
        self.sID = sID
        settings1 = Toplevel()
        settings1.title("Settings")
        settings1.geometry("310x170")
        settings1.resizable(width=FALSE, height= FALSE)
        self.gui_1()
        settings1.mainloop()

    def changePwd1(self):
        curPwd = self.cPwd1.get()
        newPwd1 = self.nPwd1.get()
        newPwd2 = self.nPwd2.get()
        if connection.is_connected():
            mycursor = connection.cursor()
            sql = 'SELECT * from students where S_name = "{}" and Password = "{}"'.format(self.sLogName, curPwd)
            mycursor.execute(sql)
            wName = mycursor.fetchall()
            if not wName:
                messagebox.showinfo("Password Error", "Please enter correct current Password", parent=chgPwd)

            else:
                # if success
                if newPwd1 == newPwd2:
                    if newPwd1 != curPwd:
                        ###SQL COMMAND HERE
                        mySql_insert_query = 'UPDATE students SET password = "{}" WHERE S_Name = "{}" and S_ID = "{}"'.format(
                            newPwd1, self.sLogName,self.sID)
                        cursor = connection.cursor()
                        cursor.execute(mySql_insert_query)
                        connection.commit()
                        messagebox.showinfo("Password Change Complete", "Password Changed successfully.", parent=chgPwd)
                        chgPwd.destroy()
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
        chPwdHeader = Label(chgPwd, text="Change Password", bg=studentColour, fg='white',
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


    def delAct(self):
        cnfrm = messagebox.askquestion('Delete Account', 'Are you sure that you want to delete your account?',
                                       icon='warning', parent=settings1)
        if cnfrm == 'yes':
            ###SQL COMMAND HERE
            # del from registration
            sql = 'DELETE FROM students WHERE S_Name = "{}" and S_ID = "{}"'.format(
                self.sLogName,self.sID)
            cursor = connection.cursor()
            cursor.execute(sql)
            connection.commit()
            cursor.close()

            #del from subjects
            sql = 'DELETE FROM studentsubject WHERE Student_Name = "{}" and Student_ID = "{}"'.format(
                self.sLogName,self.sID)
            cursor = connection.cursor()
            cursor.execute(sql)
            connection.commit()
            cursor.close()

            messagebox.showinfo("Account Deleted", "Your account has been deleted successfully", parent=settings1)
            settings1.destroy()

    def gui_1(self):
        self.settingsHeader = Label(settings1, text="Settings", bg=studentColour, fg='white',
                                    font=("Sans serif", 18, "bold"), pady=7)  # text add
        self.settingsHeader.pack(fill=X)  # pack is a must

        # change pwd button
        self.changePwdBtnIcon = PhotoImage(file="button_changePasswordStudent.png")
        self.changePwdBtn = Button(settings1, image=self.changePwdBtnIcon, borderwidth=0, command=self.changePassword)
        self.changePwdBtn.pack()
        self.changePwdBtn.place(x=40, y=70)

        # delete account
        self.delAcntBtnIcon = PhotoImage(file="button_deleteAccountStudent.png")
        self.delAcntBtn = Button(settings1, image=self.delAcntBtnIcon, borderwidth=0, command=self.delAct)
        self.delAcntBtn.pack()
        self.delAcntBtn.place(x=40, y=120)


if __name__ == '__main__':
    s1 = settingsStudent("","")
    s1
