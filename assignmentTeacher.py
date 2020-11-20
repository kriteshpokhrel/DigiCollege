from tkinter import *
from Homepage import *
from tkcalendar import DateEntry
import datetime
global teacherColour
teacherColour = "#069ce5"

class asmt1:
    def __init__(self):
        global asst
        asst = Toplevel()
        asst.title('Assignment')
        asst.geometry("400x300")
        self.gui_1()
        asst.mainloop()

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
        self.subLbl = Label(asst, text="Subject: ", font=("Sans Serif", 11))
        self.subLbl.pack()
        self.subLbl.place(x=x1, y=y1)

        # name lbl
        self.nameLbl = Label(asst, text="Assignment Name: ", font=("Sans Serif", 11))
        self.nameLbl.pack()
        self.nameLbl.place(x=x1, y=y1+gap)

        # section lbl
        self.sectionLbl = Label(asst, text="Section" , font=("Sans Serif", 11))
        self.sectionLbl.pack()
        self.sectionLbl.place(x=x1, y=y1+2*gap)

        # assignment link lbl
        self.astLkLbl = Label(asst, text="Assignment Link: ", font=("Sans Serif", 11))
        self.astLkLbl.pack()
        self.astLkLbl.place(x=x1, y=y1 + 3 * gap)

        # due date lbl
        self.dueDateLbl = Label(asst, text="Due date:" , font=("Sans Serif", 11))
        self.dueDateLbl.pack()
        self.dueDateLbl.place(x=x1, y=y1+4*gap)

        # remarks lbl
        self.reamarksLbl = Label(asst, text="Remarks" , font=("Sans Serif", 11))
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
        self.cal1.config(date_pattern='yyyy/mm/dd')
        self.cal1.place(x=x2, y=y1 + 4 * gap)

        #remarks Entry
        self.rem1 = Entry(asst)
        self.rem1.pack()
        self.rem1.place(x=x2,y=y1+5*gap,width = width1)

        #submit button
        self.submitBtn = PhotoImage(file = "button_submitTeacherSmall.png")
        self.submitBtnLbl =Button(asst, image = self.submitBtn, borderwidth = 0)
        self.submitBtnLbl.pack()
        self.submitBtnLbl.place(x=x2,y=y1+6*gap)

v1= asmt1()
v1