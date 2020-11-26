from tkinter import *
import mysql.connector
from teacherRegistration import *
from studentRegistration import *
from teacherHome import *
from db_connect import *
from tkcalendar import *
from studentHome import *
from libraryHome import *
homeColour = "#17768B"
global teacherColour
teacherColour = "#069ce5"
global studentColour
studentColour = "#f2820d"

# global variables

global SLogName
global th1

def start_gui_homepage():
    homePage = Tk()

    def teacherLogin1():

        teacherLogin = Toplevel()
        teacherLogin.title("Teacher Login")
        teacherLogin.geometry("420x250")
        teacherLogin.resizable(width=FALSE, height=False)
        # teacher login header text
        teacherHeader = Label(teacherLogin, text="Teacher/Staff Login", bg=teacherColour, fg='white',
                              font=("Sans serif", 18, "bold"),
                              pady=8)  # text add
        teacherHeader.pack(fill=X)  # pack is a must

        # username
        teacherIdLbl = Label(teacherLogin, text="Username/ID", font=("Sans Serif", 10))
        teacherIdLbl.pack()
        teacherIdLbl.place(x=45, y=80)

        # password
        teacherPassLbl = Label(teacherLogin, text="Password", font=("Sans Serif", 10))
        teacherPassLbl.pack()
        teacherPassLbl.place(x=45, y=120)

        # user image
        userImage = PhotoImage(file="icon_usernameTeacher.png")
        userImage_lbl = Label(teacherLogin, image=userImage)
        userImage_lbl.pack()
        userImage_lbl.place(x=18, y=76)

        # pass image
        passImage = PhotoImage(file="icon_passwordTeacher.png")
        passImage_lbl = Label(teacherLogin, image=passImage)
        passImage_lbl.pack()
        passImage_lbl.place(x=18, y=116)

        # Username text field
        user = Entry(teacherLogin)

        user.pack()
        user.place(x=140, y=80, width=170)

        # Password text field
        pass1 = Entry(teacherLogin, show="*", )
        pass1.pack()
        pass1.place(x=140, y=120, width=170)

        def tLogin():
            global tLogName
            tLogName = user.get()
            password = pass1.get()
            if connection.is_connected():
                mycursor = connection.cursor()
                sql = 'SELECT Sltn, t_name, t_id,dept from teachers where t_name = "{}" and Password = "{}"'.format(tLogName,
                                                                                                         password)
                mycursor.execute(sql)
                wName = mycursor.fetchall()
                if not wName:
                    messagebox.showinfo("Login Error", "Please enter a valid ID and Password!", parent=teacherLogin)
                else:
                    # if success
                    a = wName[0]
                    sal = a[0]
                    tLgName = a[1]
                    tID = a[2]
                    dept = a[3]
                    teacherLogin.destroy()
                    if not( dept == "Library"):
                        th1 = tHome(sal,tLgName,tID)
                        th1
                    else:
                        # library open
                        l1= lHome(sal,tLgName,tID)
                        l1
                mycursor.close()
            else:
                print("DBMS not connected")

        def registerTeacher():
            tReg1 = teacherReg()
            tReg1.gui_1()

        # teacher login button
        teacherLoginBtn = PhotoImage(file='button_loginTeacher.png')
        teacherLoginButton = Button(teacherLogin, image=teacherLoginBtn, borderwidth=0, command=tLogin)
        teacherLoginButton.pack()
        teacherLoginButton.place(x=140, y=150)

        # teacher register  button
        teacherRegisterBtn = PhotoImage(file='button_registerTeacher.png', master=teacherLogin)
        teacherRegisterButton = Button(teacherLogin, image=teacherRegisterBtn, borderwidth=0, command=registerTeacher)
        teacherRegisterButton.pack()
        teacherRegisterButton.place(x=320, y=212)

        teacherLogin.mainloop()

    def studentLogin1():

        studentLogin = Toplevel()
        studentLogin.title("Student Login")
        studentLogin.geometry("420x250")
        studentLogin.resizable(width=FALSE, height=False)
        # student login header text
        studentHeader = Label(studentLogin, text="Student Login", bg=studentColour, fg='white',
                              font=("Sans serif", 18, "bold"),
                              pady=8)  # text add
        studentHeader.pack(fill=X)  # pack is a must

        # username
        studentIdLbl = Label(studentLogin, text="Username/ID", font=("Sans Serif", 10))
        studentIdLbl.pack()
        studentIdLbl.place(x=45, y=80)

        # password
        studentPassLbl = Label(studentLogin, text="Password", font=("Sans Serif", 10))
        studentPassLbl.pack()
        studentPassLbl.place(x=45, y=120)

        # user image
        userImage = PhotoImage(file="icon_usernameStudent.png")
        userImage_lbl = Label(studentLogin, image=userImage)
        userImage_lbl.pack()
        userImage_lbl.place(x=18, y=76)

        # pass image
        passImage = PhotoImage(file="icon_passwordStudent.png")
        passImage_lbl = Label(studentLogin, image=passImage)
        passImage_lbl.pack()
        passImage_lbl.place(x=18, y=116)

        # Username text field
        user = Entry(studentLogin)
        user.pack()
        user.place(x=140, y=80, width=170)

        # Password text field
        pass1 = Entry(studentLogin, show="*")
        pass1.pack()
        pass1.place(x=140, y=120, width=170)

        def sLogin():

            sLogName = user.get()
            password = pass1.get()
            if connection.is_connected():
                mycursor = connection.cursor()
                sql = 'SELECT Sltn, S_name, Section,S_ID from students where S_name = "{}" and Password = "{}"'.format(sLogName,
                                                                                                         password)
                mycursor.execute(sql)
                wName = mycursor.fetchall()
                if not wName:                    messagebox.showinfo("Login Error", "Please enter a valid ID and Password!", parent=studentLogin)
                else:
                    # if success
                    ret = wName[0]
                    sec = ret[2]
                    sID = ret[3]
                    studentLogin.destroy()
                    st1 = sHome(sLogName,sec,sID)
                    st1.gui_1
                mycursor.close()
            else:
                print("DBMS not connected")
        def registerStudent():
            sReg1 = studentReg()
            sReg1.gui_1

        # student login button
        studentLoginBtn = PhotoImage(file='button_loginStudent.png')
        studentLoginButton = Button(studentLogin, image=studentLoginBtn, borderwidth=0, command=sLogin)
        studentLoginButton.pack()
        studentLoginButton.place(x=140, y=150)

        # student register  button
        studentRegisterBtn = PhotoImage(file='button_registerStudent.png')
        studentRegisterButton = Button(studentLogin, image=studentRegisterBtn, borderwidth=0, command=registerStudent)
        studentRegisterButton.pack()
        studentRegisterButton.place(x=320, y=212)

        studentLogin.mainloop()

    # homePage.configure(background = '#17768B') #set background for page
    homePage.title("DigiCollege")  # window title
    homePage.geometry("640x360")  # size
    homePage.resizable(width=FALSE, height=False)

    # Homepage header text
    homeHeader = Label(text="Welcome to DigiCollege", bg=homeColour, fg='white', font=("sdfs", 24, "bold"),
                       pady=15)  # text add
    homeHeader.pack(fill=X)  # pack is a must

    # teacher image
    teacherLogo = PhotoImage(file='icon_teacher.png')  # image add s1
    teacherLogo_lbl = Label(image=teacherLogo)  # image add s2
    teacherLogo_lbl.pack()  # pack is a must
    teacherLogo_lbl.place(x=110, y=110)

    # teacher login button
    teacherLoginBtn = PhotoImage(file='button_teacher_loginHP.png')
    teacherButton = Button(homePage, image=teacherLoginBtn, borderwidth=0, command=teacherLogin1)
    teacherButton.pack()
    teacherButton.place(x=85, y=280)

    # student image
    studentLogo = PhotoImage(file='icon_student.png')  # image add s1
    studentLogo_lbl = Label(image=studentLogo)  # image add s2
    studentLogo_lbl.pack()  # pack is a must
    studentLogo_lbl.place(x=380, y=110)

    # student login button
    studentLoginBtn = PhotoImage(file='button_student_loginHP.png')
    studentButton = Button(homePage, image=studentLoginBtn, borderwidth=0, command=studentLogin1)
    studentButton.pack()
    studentButton.place(x=375, y=278)

    '''
    #register button
    registerBtn = PhotoImage(file ='button_registerHomepage.png')
    registerButton = Button(homePage, image=registerBtn, borderwidth=0, command = register1)
    registerButton.pack()
    registerButton.place(x=550, y=335)
    '''
    homePage.mainloop()


if __name__ == '__main__':
    start_gui_homepage();
