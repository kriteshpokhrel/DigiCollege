from tkinter import *
from tkinter import messagebox
from db_connect import *
from teacherHome import *

global teacherColour
teacherColour = "#069ce5"


class vClass:
    def __init__(self, tLogName, sec1,tID):
        self.tLogName = tLogName
        self.sec1 = sec1
        self.tID = tID
        global viewClass
        viewClass = Toplevel()
        viewClass.geometry("900x480")
        viewClass.wm_minsize(width='900', height='480')
        viewClass.resizable(width=FALSE, height=False)
        viewClass.title("Classroom")
        self.gui_1()
        viewClass.mainloop()

    def listStudents(self):
        # btm frame
        btmFrame = Frame(viewClass)
        btmFrame.pack(fill=X)
        btmFrame.place(y=50)
        conn = connection.cursor()
        sql = 'SELECT S_Name, S_ID, Dept, Section, dob, C_no, Address, email FROM students WHERE Section = "{}"'.format(
            self.sec1)
        res = conn.execute(sql)
        ww = conn.fetchall()

        details = ["S_Name", "S_ID", "Dept", "Section", "DOB", "C_No", "Address", "Email"]
        i = 0
        width1 = ["20", "15", "10", "8", "20", "15", "25", "50"]
        # creating headings
        for j in range(len(details)):
            e = Entry(btmFrame, width=width1[j], bg=teacherColour)
            e.grid(row=i, column=j)
            e.insert(END, details[j])
        i += 1
        # inserting datasframe1,pc
        for student in ww:
            for j in range(len(student)):
                e = Entry(btmFrame, width=width1[j], bg='white')
                e.grid(row=i, column=j)
                e.insert(END, student[j])
            i += 1

    def gui_1(self):
        # top Frame
        topFrame = Frame(viewClass)
        topFrame.pack(side=TOP, fill=X)
        # header
        textDis = " Class Teacher:" + self.tLogName + "   Section: " + self.sec1
        self.tHeader = Label(topFrame, text=textDis, bg=teacherColour, fg='white',
                             font=("Sans serif", 16, "bold"), pady=6)  # text add
        self.tHeader.pack(fill=X)  # pack is a must
        self.listStudents()


if __name__ == '__main__':
    v1 = vClass("asd", "asd")
    v1
