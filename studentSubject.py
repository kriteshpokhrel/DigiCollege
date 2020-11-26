from tkinter import *
from Homepage import *
from tkinter import  messagebox
from db_connect import *

global studentColour
studentColour = "#f2820d"

class studentSub:
    def __init__(self,logName,sec,sID):
        self.logName = logName
        self.sec =sec
        self.sID = sID
        print(self.sID,self.logName,self.sec)

        global stuSub1
        stuSub1 = Toplevel()
        stuSub1.geometry("700x300")
        self.gui_1()
        stuSub1.mainloop()

    def addSub(self):
        self.addSub = self.subAdd1.get()
        if not self.addSub:
            messagebox.showwarning("Field Empty", "Please enter Subject Code.")
        else:

            ###SQL COMMAND HERE
            sql = 'INSERT INTO studentsubject VALUES ("{}","{}","{}","{}")' \
                .format(self.logName,self.sID,self.sec,self.addSub)
            cursor = connection.cursor()
            cursor.execute(sql)
            connection.commit()
            messagebox.showinfo("Done", "Subject has been added successfully,")
            stuSub1.destroy()
            s1= studentSub(self.logName,self.sec,self.sID)
            s1

    def delSub(self):
        self.delSub = self.subDel1.get()
        if not self.delSub:
            messagebox.showwarning("Field Empty", "Please enter Subject Code.")
        else:
            ###SQL COMMAND HERE
            sql = 'DELETE FROM studentsubject  where Student_Name = "{}" and Student_ID = "{}" and Section = "{}" and Subject_Code ="{}"' \
                .format(self.logName,self.sID,self.sec,self.delSub)
            cursor = connection.cursor()
            cursor.execute(sql)
            connection.commit()
            connection.commit()
            delRowCount = cursor.rowcount
            if delRowCount == 0:
                messagebox.showerror("Error", "You have not registered for this course.",
                                     parent=stuSub1)
            else:
                messagebox.showinfo("Done", "Course deleted successfully",parent = stuSub1)

            stuSub1.destroy()
            s1= studentSub(self.logName,self.sec,self.sID)
            s1

    def gui_1(self):
        # header
        subHeader = Label(stuSub1, text="Your Subjects", bg=studentColour, fg='white',
                             font=("Sans serif", 15, "bold"), pady=7)  # text add
        subHeader.pack(fill=X)  # pack is a must



        width1 = 170
        x1Add, x2Add = 20, 130
        x1Del, x2Del = 350, 470
        y1 = 50
        gap = 30
        fsizeLbl = 11

        #subject Code Lbl for Add
        self.subAddLbl = Label(stuSub1,text = "Subject Code: ",font=("Sans Serif", fsizeLbl))
        self.subAddLbl.pack()
        self.subAddLbl.place(x=x1Add,y=y1)

        #subject Code Lbl for del
        self.subDelLbl = Label(stuSub1,text = "Subject Code: ",font=("Sans Serif", fsizeLbl))
        self.subDelLbl.pack()
        self.subDelLbl.place(x=x1Del,y=y1)

        #Subject Code entry for add
        self.subAdd1 = Entry(stuSub1)
        self.subAdd1.pack()
        self.subAdd1.place(x=x2Add,y=y1,width=width1)

        #Subject Code entry for add
        self.subDel1 = Entry(stuSub1)
        self.subDel1.pack()
        self.subDel1.place(x=x2Del,y=y1,width=width1)


        # add Subject button
        self.addSubBtnIcon = PhotoImage(file="button_addSubject.png")
        self.addSubBtn = Button(stuSub1, image=self.addSubBtnIcon, borderwidth=0,command = self.addSub)
        self.addSubBtn.pack()
        self.addSubBtn.place(x=x2Add, y=y1+gap)

        #delete subject button
        self.delSubBtnIcon = PhotoImage(file="button_deleteSubject.png")
        self.delSubBtn = Button(stuSub1, image=self.delSubBtnIcon, borderwidth=0,command = self.delSub)
        self.delSubBtn.pack()
        self.delSubBtn.place(x=x2Del, y=y1+gap)

        # btm frame
        btmFrame = Frame(stuSub1)
        btmFrame.pack(fill=X)
        btmFrame.place(x=5,y=y1+3*gap)
        conn = connection.cursor()
        sql = 'SELECT s.Student_Name, s.Student_ID, s.Section, s.Subject_Code, s1.S_Name FROM studentsubject as s, subject as s1 WHERE s.Student_Name = "{}" and s.Student_ID = "{}" and s.Section ="{}" and s1.S_Code =s.Subject_Code '.format(
            self.logName,self.sID,self.sec)

        res = conn.execute(sql)
        sList = conn.fetchall()

        details = ["Student_Name", "Student_ID", "Section", "Subject_Code","Subject_Name"]
        i = 0
        width1 = ["35", "15", "8", "15","40"]
        # creating headings
        for j in range(len(details)):
            e = Entry(btmFrame, width=width1[j], bg=studentColour)
            e.grid(row=i, column=j)
            e.insert(END, details[j])
        i += 1
        # inserting datasframe1,pc
        for subject in sList:
            for j in range(len(subject)):
                e = Entry(btmFrame, width=width1[j], bg='white')
                e.grid(row=i, column=j)
                e.insert(END, subject[j])
            i += 1
if __name__ == "__main__":
    s1= studentSub("Kritesh Pokhrel","5C","123")
    s1