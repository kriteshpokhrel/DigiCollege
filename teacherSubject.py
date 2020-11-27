from tkinter import *
from Homepage import *
from tkinter import  messagebox
from db_connect import *

global teacherColour
teacherColour = "#069ce5"
class teacherSub:
    def __init__(self,logName,tID):
        self.logName = logName
        self.tID = tID

        global tSub1
        tSub1 = Toplevel()
        tSub1.geometry("730x300")
        tSub1.resizable(width=FALSE,height=FALSE)
        self.gui_1()
        tSub1.mainloop()

    def addSub(self):
        self.addSub = self.subAdd1.get()
        if not self.addSub:
            messagebox.showwarning("Field Empty", "Please enter Subject Code.",parent= tSub1)
        else:
            cursor = connection.cursor(buffered=TRUE)
            sql = 'SELECT * from subject where S_Code ="{}"'.format(self.addSub)
            cursor.execute(sql)
            subExist = cursor.fetchall()
            if not subExist:
                messagebox.showerror("Error","Enter valid Subject Code.",parent = tSub1)
            else:
                ###SQL COMMAND HERE
                sql = 'INSERT INTO teachersubject VALUES ("{}","{}","{}")' \
                    .format(self.logName,self.tID,self.addSub)
                cursor = connection.cursor(buffered=TRUE)
                cursor.execute(sql)
                cursor.close()
                messagebox.showinfo("Done", "Subject has been added successfully,",parent= tSub1)
                tSub1.destroy()
                t1= teacherSub(self.logName,self.tID)
                t1

    def delSub(self):
        self.delSub = self.subDel1.get()
        if not self.delSub:
            messagebox.showwarning("Field Empty", "Please enter Subject Code.",parent= tSub1)
        else:
            ###SQL COMMAND HERE
            sql = 'DELETE FROM teachersubject  where Teacher_Name = "{}" and Teacher_ID = "{}"  and Subject_Code ="{}"' \
                .format(self.logName,self.tID,self.delSub)
            cursor = connection.cursor(buffered=TRUE,dictionary=True)
            cursor.execute(sql)
            connection.commit()
            connection.commit()
            delRowCount = cursor.rowcount
            if delRowCount == 0:
                messagebox.showerror("Error", "You have not registered for this course.",
                                     parent=tSub1)
            else:
                messagebox.showinfo("Done", "Course deleted successfully",parent = tSub1)

            tSub1.destroy()
            s1= teacherSub(self.logName,self.tID)
            s1

    def gui_1(self):
        # header
        subHeader = Label(tSub1, text="Your Subjects", bg=teacherColour, fg='white',
                             font=("Sans serif", 15, "bold"), pady=7)  # text add
        subHeader.pack(fill=X)  # pack is a must



        width1 = 180
        x1Add, x2Add = 20, 130
        x1Del, x2Del = 350, 450
        y1 = 50
        gap = 30
        fsizeLbl = 11

        #subject Code Lbl for Add
        self.subAddLbl = Label(tSub1,text = "Subject Code: ",font=("Sans Serif", fsizeLbl))
        self.subAddLbl.pack()
        self.subAddLbl.place(x=x1Add,y=y1)

        #subject Code Lbl for del
        self.subDelLbl = Label(tSub1,text = "Subject Code: ",font=("Sans Serif", fsizeLbl))
        self.subDelLbl.pack()
        self.subDelLbl.place(x=x1Del,y=y1)

        #Subject Code entry for add
        self.subAdd1 = Entry(tSub1)
        self.subAdd1.pack()
        self.subAdd1.place(x=x2Add,y=y1,width=width1)

        #Subject Code entry for add
        self.subDel1 = Entry(tSub1)
        self.subDel1.pack()
        self.subDel1.place(x=x2Del,y=y1,width=width1)


        # add Subject button
        self.addSubBtnIcon = PhotoImage(file="button_addSubjectTeacher.png")
        self.addSubBtn = Button(tSub1, image=self.addSubBtnIcon, borderwidth=0,command = self.addSub)
        self.addSubBtn.pack()
        self.addSubBtn.place(x=x2Add, y=y1+gap)

        #delete subject button
        self.delSubBtnIcon = PhotoImage(file="button_deleteSubjectTeacher.png")
        self.delSubBtn = Button(tSub1, image=self.delSubBtnIcon, borderwidth=0,command = self.delSub)
        self.delSubBtn.pack()
        self.delSubBtn.place(x=x2Del, y=y1+gap)

        # btm frame
        btmFrame = Frame(tSub1)
        btmFrame.pack(fill=X)
        btmFrame.place(x=5,y=y1+3*gap)
        conn = connection.cursor(buffered=TRUE)
        sql = 'SELECT t.Teacher_Name, t.Teacher_ID,  t.Subject_Code, s.S_Name FROM teachersubject  t, subject s  WHERE t.Teacher_Name = "{}" and t.Teacher_ID = "{}" and s.S_Code = t.Subject_Code'.format(
            self.logName,self.tID)
        res = conn.execute(sql)
        tList = conn.fetchall()

        details = ["Teacher_Name", "Teacher_ID", "Subject_Code","Subject_Name"]
        i = 0
        width1 = ["35", "25","21","40"]
        # creating headings
        for j in range(len(details)):
            e = Entry(btmFrame, width=width1[j], bg=teacherColour)
            e.grid(row=i, column=j)
            e.insert(END, details[j])
        i += 1
        # inserting datasframe1,pc
        for subject in tList:
            for j in range(len(subject)):
                e = Entry(btmFrame, width=width1[j], bg='white')
                e.grid(row=i, column=j)
                e.insert(END, subject[j])
            i += 1

if __name__ == "__main__":
    s1= teacherSub("Chempa","1234")
    s1
