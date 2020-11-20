from tkinter import *

studentColour = "#f2820d"

studentLogin = Tk()
studentLogin.title("Student Login")
studentLogin.geometry("420x250")

# student login header text
studentHeader = Label(studentLogin, text="Student Login", bg=studentColour, fg='white', font=("Sans serif", 18, "bold"),
                      pady=8)  # text add
studentHeader.pack(fill=X)  # pack is a must

# username
studentIdLbl = Label(studentLogin, text = "Username/ID", font = ("Sans Serif", 10))
studentIdLbl.pack()
studentIdLbl.place(x= 45, y= 80)

# password
studentPassLbl = Label(studentLogin, text = "Password", font = ("Sans Serif", 10))
studentPassLbl.pack()
studentPassLbl.place(x= 45, y= 120)


# user image
userImage= PhotoImage(file="icon_usernameStudent.png")
userImage_lbl = Label(image = userImage)
userImage_lbl.pack()
userImage_lbl.place(x= 18, y= 76)

# pass image
passImage= PhotoImage(file="icon_passwordStudent.png")
passImage_lbl = Label(image = passImage)
passImage_lbl.pack()
passImage_lbl.place(x= 18, y= 116)

# Username text field
user = Entry(studentLogin)

user.pack()
user.place(x= 140,y= 80,width = 170)

# Password text field
pass1 = Entry(studentLogin)
pass1.pack()
pass1.place(x= 140,y= 120,width = 170)
def ss():
    username = user.get()
    print(username)
    password = pass1.get()
    print(password)


def registerStudent():
    print("Student Registraion")
# student login button
studentLoginBtn = PhotoImage(file='button_loginStudent.png')
studentLoginButton = Button(studentLogin, image=studentLoginBtn, borderwidth=0, command=ss)
studentLoginButton.pack()
studentLoginButton.place(x=140, y=150)

# student register  button
studentRegisterBtn = PhotoImage(file='button_registerStudent.png')
studentRegisterButton = Button(studentLogin, image=studentRegisterBtn, borderwidth=0, command = registerStudent)
studentRegisterButton.pack()
studentRegisterButton.place(x=320, y=212)

studentLogin.mainloop()
