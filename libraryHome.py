from tkinter import *
from Homepage import *
from tkcalendar import DateEntry
import datetime
from db_connect import *
from tkinter import messagebox
from librarySettings import *
global libColor
libColour = '#188ce5'


class lHome:
    def __init__(self, sal, logName,tID):
        self.sal = sal
        self.logName = logName
        self.tID = tID
        global libHome
        libHome = Toplevel()
        libHome.title("Library Home")
        libHome.geometry("400x470")
        self.gui_1()
        libHome.mainloop()

    def issueFinal(self):
        sName = self.sName1.get()
        sId = self.sId1.get()
        bId = self.bId1.get()
        iDate = self.cal1.get()
        rDate = self.cal2.get()
        remarks = self.rem1.get()

        # check if student name and ID is matches
        if connection.is_connected():
            mycursor = connection.cursor(buffered=True)
            sql = 'SELECT * from students where S_name = "{}" and S_ID = "{}"'.format(sName,sId)
            mycursor.execute(sql)
            sRece = mycursor.fetchall()
            mycursor.close()
            if not sRece:
                messagebox.showinfo("Field Error", "Student not found in database, please enter proper data",
                                    parent=isBook)
            else:
                # check if 3 books already issued
                mycursor = connection.cursor(buffered=True)
                sql = 'SELECT BookName, BookID, Student_ID from booksissued where Student_ID = "{}" '.format(sId)
                mycursor.execute(sql)
                noOfIssued = mycursor.rowcount
                if noOfIssued > 3:
                    messagebox.showerror("Error", "You have already issued 3 books", parent=isBook)
                else:
                    mycursor = connection.cursor(buffered=True)
                    sql = 'SELECT BookName, BookID from books where BookID = "{}" '.format(bId)
                    mycursor.execute(sql)
                    bRece = mycursor.fetchall()
                    if not bRece:
                        messagebox.showinfo("Field Error", "Book not found in database.",
                                            parent=isBook)
                    else:
                        # write in to sql
                        a = bRece[0]
                        bName = a[0]
                        mySql_insert_query = 'INSERT INTO booksIssued VALUES ("{}","{}","{}","{}","{}","{}","{}")' \
                            .format(bName, bId, sName, sId, iDate, rDate, remarks)
                        cursor = connection.cursor()
                        cursor.execute(mySql_insert_query)
                        connection.commit()
                        messagebox.showinfo("Book Issued", "Book issue has been registered", parent=isBook)
                        isBook.destroy()
        else:
            messagebox.showerror("DBMS error", "Database has been disconnected.")

    def issueBook1(self):
        global isBook
        isBook = Toplevel()
        isBook.geometry("380x300")
        isBook.title("Issue Book")

        # header
        isBookHeader = Label(isBook, text="Issue Book", bg=libColour, fg='white',
                             font=("Sans serif", 18, "bold"), pady=8)  # text add
        isBookHeader.pack(fill=X)  # pack is a must

        x1, x2 = 20, 130
        y1, gapY = 70, 30
        width1 = 200

        # Name
        self.sNameLbl = Label(isBook, text="Student Name: ", font=("Sans Serif", 11))
        self.sNameLbl.pack()
        self.sNameLbl.place(x=x1, y=y1)

        # USN
        self.sIdLbl = Label(isBook, text="Student ID: ", font=("Sans Serif", 11))
        self.sIdLbl.pack()
        self.sIdLbl.place(x=x1, y=y1 + gapY)

        # Book ID
        self.bIdLbl = Label(isBook, text="Book ID: ", font=("Sans Serif", 11))
        self.bIdLbl.pack()
        self.bIdLbl.place(x=x1, y=y1 + 2 * gapY)

        # Issue Date LBl
        self.iIsDateLbl = Label(isBook, text="Issue Date: ", font=("Sans Serif", 11))
        self.iIsDateLbl.pack()
        self.iIsDateLbl.place(x=x1, y=y1 + 3 * gapY)

        # Return date LBL
        self.iReDateLbl = Label(isBook, text="Return Date: ", font=("Sans Serif", 11))
        self.iReDateLbl.pack()
        self.iReDateLbl.place(x=x1, y=y1 + 4 * gapY)

        # Remarks date LBL
        self.remarksLbl = Label(isBook, text="Remarks: ", font=("Sans Serif", 11))
        self.remarksLbl.pack()
        self.remarksLbl.place(x=x1, y=y1 + 5 * gapY)

        # Name text field
        self.sName1 = Entry(isBook)
        self.sName1.pack()
        self.sName1.place(x=x2, y=y1, width=width1)

        # sID text field
        self.sId1 = Entry(isBook)
        self.sId1.pack()
        self.sId1.place(x=x2, y=y1 + gapY, width=width1)

        # BID text field
        self.bId1 = Entry(isBook)
        self.bId1.pack()
        self.bId1.place(x=x2, y=y1 + 2 * gapY, width=width1)

        # Issue Date
        d = datetime.date.today()
        self.cal1 = DateEntry(isBook, width=12, year=d.year, month=d.month, day=d.day,
                              background=libColour, foreground='white', borderwidth=2)
        self.cal1.pack()
        self.cal1.config(date_pattern='yyyy/mm/dd')
        self.cal1.place(x=x2, y=y1 + 3 * gapY)

        # return Date
        d = datetime.date.today()
        self.cal2 = DateEntry(isBook, width=12, year=d.year, month=d.month, day=d.day + 15,
                              background=libColour, foreground='white', borderwidth=2)
        self.cal2.pack()
        self.cal2.config(date_pattern='yyyy/mm/dd')
        self.cal2.place(x=x2, y=y1 + 4 * gapY)

        # ID text field
        self.rem1 = Entry(isBook)
        self.rem1.pack()
        self.rem1.place(x=x2, y=y1 + 5 * gapY, width=width1)

        # submit btn
        self.submitBtn = PhotoImage(file="button_submitLib.png")
        self.submitButton = Button(isBook, image=self.submitBtn, borderwidth=0, command=self.issueFinal)
        self.submitButton.pack()
        self.submitButton.place(x=x2, y=y1 + 5 * gapY + 30)

        isBook.mainloop()

    def retFinal(self):

        self.bID = self.bID1.get()
        self.sName = self.sNameRet1.get()
        self.sId = self.sIdRet1.get()

        # SQL CODE
        if connection.is_connected():
            mycursor = connection.cursor()
            sql = 'DELETE from booksissued where Student_name = "{}" and Student_ID = "{}" and BookID = "{}"'.format(
                self.sName,
                self.sId,
                self.bID)
            mycursor.execute(sql)
            connection.commit()
            delRowCount = mycursor.rowcount
            if delRowCount == 0:
                messagebox.showerror("Entry Error", "Book Issue not found in database, please enter proper data",
                                     parent=retBook)
            else:
                messagebox.showinfo("Completed", "Book has been returned.",parent=retBook)
                retBook.destroy()

    def returnBook1(self):
        global retBook
        retBook = Toplevel()
        retBook.title("Return Book")
        retBook.geometry('350x210')

        # header
        retBookHeader = Label(retBook, text="Return Book", bg=libColour, fg='white',
                              font=("Sans serif", 16, "bold"), pady=7)  # text add
        retBookHeader.pack(fill=X)  # pack is a must

        x1, x2 = 20, 130
        y1, gapY = 70, 30
        width1 = 200

        # Book ID
        self.bIdLbl = Label(retBook, text="Book ID: ", font=("Sans Serif", 11))
        self.bIdLbl.pack()
        self.bIdLbl.place(x=x1, y=y1)

        # USN
        self.sNameLbl = Label(retBook, text="Student Name: ", font=("Sans Serif", 11))
        self.sNameLbl.pack()
        self.sNameLbl.place(x=x1, y=y1 + gapY)

        # USN
        self.sIdLbl = Label(retBook, text="Student ID: ", font=("Sans Serif", 11))
        self.sIdLbl.pack()
        self.sIdLbl.place(x=x1, y=y1 + 2 * gapY)

        # B_ID text field
        self.bID1 = Entry(retBook)
        self.bID1.pack()
        self.bID1.place(x=x2, y=y1, width=width1)

        # Name text field
        self.sNameRet1 = Entry(retBook)
        self.sNameRet1.pack()
        self.sNameRet1.place(x=x2, y=y1 + gapY, width=width1)

        # USN text field
        self.sIdRet1 = Entry(retBook)
        self.sIdRet1.pack()
        self.sIdRet1.place(x=x2, y=y1 + 2 * gapY, width=width1)

        # submit button
        self.retSubmit = PhotoImage(file='button_submitLib.png')
        self.retSubmitBtn = Button(retBook, image=self.retSubmit, borderwidth=0, command=self.retFinal)
        self.retSubmitBtn.pack()
        self.retSubmitBtn.place(x=x2, y=y1 + 2 * gapY + 25)

        retBook.mainloop()

    def delBook(self):
        self.delBookID = self.id1.get()
        #sql code
        sql = 'DELETE FROM books WHERE BookID = "{}" '.format(
            self.delBookID)
        cursor = connection.cursor()
        cursor.execute(sql)
        connection.commit()
        cursor.close()
        delRowCount = cursor.rowcount
        if delRowCount == 0:
            messagebox.showerror("Error", "Book not found in database.",
                                 parent=listBDB)
        else:
            messagebox.showinfo("Book Deleted", "Book has been deleted from database", parent=listBDB)
    def viewAllIsdBk(self):
        # sql
        global listIsBook
        listIsBook = Toplevel()
        listIsBook.geometry('1100x500')
        listIsBook.title("Books Issued")
        listIsBook.resizable(width=FALSE, height=FALSE)

        # frame1
        frame1 = Frame(listIsBook)
        frame1.pack(side=TOP, fill=X)
        # DB header
        dbHeader = Label(frame1, text="Books Issued", bg=libColour, fg='white',
                         font=("Sans serif", 20, "bold"), pady=10)  # text add
        dbHeader.pack(fill=X)  # pack is a must

        # frame1
        frame2 = Frame(listIsBook)
        frame2.pack(fill=X)
        frame2.place(y=100)

        # DB SQL
        conn = connection.cursor()
        sql = 'SELECT * FROM booksIssued '
        res = conn.execute(sql)
        ww = conn.fetchall()
        i = 1
        totalBooksIssued = len(ww)
        details = ["BookName", "BookID", "Student_Name", "Student_ID", "Issue_date", "Return_Date", "Remarks"]
        # display total books
        if totalBooksIssued == 0:
            listIsBook.destroy()
            messagebox.showerror("Error", "No books have been issued", parent=libHome)
        else:
            totBooksLbl = Label(listIsBook, text='Total Books Issued: ' + str(totalBooksIssued), font=('bold', 15))
            totBooksLbl.pack()
            totBooksLbl.place(x=10, y=65)
            i = 0
            width1 = ["50", "15", "30", "15", "15", "15", "50"]
            # creating headings
            for j in range(len(details)):
                e = Entry(frame2, width=width1[j], bg=libColour)
                e.grid(row=i, column=j)
                e.insert(END, details[j])
            i += 1
            # inserting datas
            j = 0
            for books in ww:
                for j in range(len(books)):
                    e = Entry(frame2, width=width1[j], bg='white')
                    e.grid(row=i, column=j)
                    e.insert(END, books[j])
                i += 1
            listIsBook.mainloop()



    def listDB(self):
        global listBDB
        listBDB = Toplevel()
        listBDB.geometry('650x400')
        listBDB.title("Books")
        # frame1
        frame1 = Frame(listBDB)
        frame1.pack(side=TOP, fill=X)

        # DB header
        dbHeader = Label(frame1, text="Books Database", bg=libColour, fg='white',
                         font=("Sans serif", 20, "bold"), pady=12)  # text add
        dbHeader.pack(fill=X)  # pack is a must

        # frame1
        frame2 = Frame(listBDB)
        frame2.pack(fill=X)
        frame2.place(y=150)

        # DB SQL
        conn = connection.cursor()
        sql = 'SELECT * FROM books'
        res = conn.execute(sql)
        ww = conn.fetchall()
        i = 1
        totalBooks = len(ww)
        details = ["BookName", "BookID", "Author", "Edition"]

        # display total books
        totBooksLbl = Label(listBDB, text='Total Books: ' + str(totalBooks), font=('bold', 15))
        totBooksLbl.pack()
        totBooksLbl.place(x=10, y=65)
        i = 0
        width1 = ["50", "15", "30", "10"]
        # creating headings
        for j in range(len(details)):
            e = Entry(frame2, width=width1[j], bg=libColour)
            e.grid(row=i, column=j)
            e.insert(END, details[j])
        i += 1
        # inserting datas
        for books in ww:
            for j in range(len(books)):
                e = Entry(frame2, width=width1[j], bg='white')
                e.grid(row=i, column=j)
                e.insert(END, books[j])
            i += 1

        # bookID Lbl
        self.nameLbl = Label(listBDB, text="Book ID: ", font=("Sans Serif", 12,'bold'))
        self.nameLbl.pack()
        self.nameLbl.place(x=10,y=110)

        # Book ID entry field
        self.id1 = Entry(listBDB)
        self.id1.pack()
        self.id1.place (x=100,y=110,width=150)

        #del Book button
        self.delBookIcn =PhotoImage(file = "button_deleteBookLibrary.png")
        self.delBookIcnBtn =Button(listBDB, image = self.delBookIcn,borderwidth = 0,command = self.delBook)
        self.delBookIcnBtn.pack()
        self.delBookIcnBtn.place(x=270,y=107)

        #view all issued button
        self.viewAlIssuedIcn =PhotoImage(file = "button_allBookIssued.png")
        self.viewAlIssuedIcnBtn =Button(listBDB, image = self.viewAlIssuedIcn,borderwidth = 0,command = self.viewAllIsdBk)
        self.viewAlIssuedIcnBtn.pack()
        self.viewAlIssuedIcnBtn.place(x=470,y=107)

        listBDB.mainloop()

    def addFinal(self):
        adBookID = self.adBookId1.get()
        bName = self.bName1.get()
        bAuthor = self.bAuthor1.get()
        bEdition = self.bEdition1.get()

        if adBookID and bName and bAuthor and bEdition:
            if connection.is_connected():
                mycursor = connection.cursor()
                sql = 'SELECT * from books where BookID = "{}" '.format(adBookID)
                mycursor.execute(sql)
                bRece = mycursor.fetchall()
                if bRece:
                    messagebox.showinfo("Error", "Book already registered in database.",
                                        parent=adBook)
                else:
                    mycursor = connection.cursor()
                    sql = 'INSERT INTO books VALUES ("{}","{}","{}","{}")' \
                        .format(adBookID, bName, bAuthor, bEdition)
                    mycursor.execute(sql)
                    connection.commit()
                    messagebox.showinfo("Book Registered", 'Book has been added to the database.', parent=adBook)
                    adBook.destroy()
            else:
                print("DBMS not connected")

        else:
            messagebox.showerror("Error", "Please enter all data.", parent=adBook)

    def addBook1(self):
        global adBook
        adBook = Toplevel()
        adBook.title("Add Book")
        adBook.geometry("450x280")
        x1, x2 = 40, 130
        y1, gapY = 80, 35
        width1 = 250

        # Add book header
        adBookHeader = Label(adBook, text="Add Book", bg=libColour, fg='white',
                             font=("Sans serif", 20, "bold"), pady=8)  # text add
        adBookHeader.pack(fill=X)  # pack is a must
        # book ID text field
        self.adBookId1 = Entry(adBook)
        self.adBookId1.pack()
        self.adBookId1.place(x=x2, y=y1, width=width1)

        # Book Name text field
        self.bName1 = Entry(adBook)
        self.bName1.pack()
        self.bName1.place(x=x2, y=y1 + gapY, width=width1)

        # Author text field
        self.bAuthor1 = Entry(adBook)
        self.bAuthor1.pack()
        self.bAuthor1.place(x=x2, y=y1 + 2 * gapY, width=width1)

        # Edition text field
        self.bEdition1 = Entry(adBook)
        self.bEdition1.pack()
        self.bEdition1.place(x=x2, y=y1 + 3 * gapY, width=width1)

        # Book ID Lbl
        self.bIdLbl = Label(adBook, text="Book ID: ", font=("Sans Serif", 11))
        self.bIdLbl.pack()
        self.bIdLbl.place(x=x1, y=y1)

        # Book name Lbl
        self.bAdNameLbl = Label(adBook, text="Book Name: ", font=("Sans Serif", 11))
        self.bAdNameLbl.pack()
        self.bAdNameLbl.place(x=x1, y=y1 + gapY)

        # Book Author Lbl
        self.bAuthorLbl = Label(adBook, text="Author(s): ", font=("Sans Serif", 11))
        self.bAuthorLbl.pack()
        self.bAuthorLbl.place(x=x1, y=y1 + 2 * gapY)

        # Book Edition Lbl
        self.bEditionLbl = Label(adBook, text="Edition: ", font=("Sans Serif", 11))
        self.bEditionLbl.pack()
        self.bEditionLbl.place(x=x1, y=y1 + 3 * gapY)

        # submit btn
        self.adBookSubmit = PhotoImage(file='button_submitLib.png')
        self.adBookSubmitBtn = Button(adBook, image=self.adBookSubmit, borderwidth=0, command=self.addFinal)
        self.adBookSubmitBtn.pack()
        self.adBookSubmitBtn.place(x=x2, y=y1 + 3 * gapY + 30)

        adBook.mainloop()
    def settingsOpen(self):
        s1= settingsLibrary(self.sal,self.logName,self.tID)
        s1
    def gui_1(self):
        # header
        textDis = 'Welcome ' + self.sal + " " + self.logName
        self.tHeader = Label(libHome, text=textDis, bg=libColour, fg='white',
                             font=("Sans serif", 16, "bold"), pady=10)  # text add
        self.tHeader.pack(fill=X)  # pack is a must

        # issue Book image
        self.issueBook = PhotoImage(file='icon_bookIssue.png')
        self.issueBookLbl = Label(libHome, image=self.issueBook)
        self.issueBookLbl.pack()
        self.issueBookLbl.place(x=50, y=70)

        # return Book image
        self.returnBook = PhotoImage(file='icon_bookReturn.png')
        self.returnBookLbl = Label(libHome, image=self.returnBook)
        self.returnBookLbl.pack()
        self.returnBookLbl.place(x=230, y=70)

        # add Book image
        self.addBook = PhotoImage(file='icon_bookAdd.png')
        self.addBookLbl = Label(libHome, image=self.addBook)
        self.addBookLbl.pack()
        self.addBookLbl.place(x=50, y=265)

        # BookDb image
        self.bookDb = PhotoImage(file='icon_bookDb.png')
        self.bookDbLbl = Label(libHome, image=self.bookDb)
        self.bookDbLbl.pack()
        self.bookDbLbl.place(x=230, y=265)

        x1Btn, gapX = 42, 180
        y1Btn, gapY = 210, 190

        # issue book button
        self.issueBookBtn = PhotoImage(file='button_issueBook.png')
        self.issueBookBtnLbl = Button(libHome, image=self.issueBookBtn, borderwidth=0, command=self.issueBook1)
        self.issueBookBtnLbl.pack()
        self.issueBookBtnLbl.place(x=x1Btn, y=y1Btn)

        # return book button
        self.returnBookBtn = PhotoImage(file='button_returnBook.png')
        self.returnBookBtnLbl = Button(libHome, image=self.returnBookBtn, borderwidth=0, command=self.returnBook1)
        self.returnBookBtnLbl.pack()
        self.returnBookBtnLbl.place(x=x1Btn + gapX, y=y1Btn)

        # add book button
        self.addBookBtn = PhotoImage(file='button_addBook.png')
        self.addBookBtnLbl = Button(libHome, image=self.addBookBtn, borderwidth=0, command=self.addBook1)
        self.addBookBtnLbl.pack()
        self.addBookBtnLbl.place(x=x1Btn, y=y1Btn + gapY)

        # bookDB button
        self.bookDbBtn = PhotoImage(file='button_bookDatabase.png')
        self.bookDbBtnLbl = Button(libHome, image=self.bookDbBtn, borderwidth=0, command=self.listDB)
        self.bookDbBtnLbl.pack()
        self.bookDbBtnLbl.place(x=x1Btn + gapX, y=y1Btn + gapY)


        # settings button
        self.settingsBtnIcon = PhotoImage(file ="button_settingsTeacher.png")
        self.settingsBtn = Button(libHome, image = self.settingsBtnIcon, borderwidth = 0,command = self.settingsOpen)
        self.settingsBtn.pack()
        self.settingsBtn.place(x='350',y= '50')


if __name__ == '__main__':
    l2 = lHome("asd", "sd","")
