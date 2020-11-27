import tkinter as tk
from tkinter import messagebox
import cv2
import os
from PIL import Image
import numpy as np
import mysql.connector
from db_connect import *
window = tk.Tk()
window.title("Face recognition system")
# window.config(background="lime")
l1 = tk.Label(window, text="Name", font=("Algerian", 20))
l1.grid(column=0, row=0)
t1 = tk.Entry(window, width=50, bd=5)
t1.grid(column=1, row=0)

l2 = tk.Label(window, text="Age", font=("Algerian", 20))
l2.grid(column=0, row=1)
t2 = tk.Entry(window, width=50, bd=5)
t2.grid(column=1, row=1)

l3 = tk.Label(window, text="Address", font=("Algerian", 20))
l3.grid(column=0, row=2)
t3 = tk.Entry(window, width=50, bd=5)
t3.grid(column=1, row=2)


def train_classifier():
    data_dir = "C:\\Users\\krite\\PycharmProjects\\DigiCollege\\data"
    path = [os.path.join(data_dir, f) for f in os.listdir(data_dir)]
    faces = []
    ids = []

    for image in path:
        img = Image.open(image).convert('L');
        imageNp = np.array(img, 'uint8')
        id = int(os.path.split(image)[1].split(".")[1])

        faces.append(imageNp)
        ids.append(id)
    ids = np.array(ids)

    # Train the classifier and save
    clf = cv2.face.LBPHFaceRecognizer_create()
    clf.train(faces, ids)
    clf.write("classifier.xml")
    messagebox.showinfo('Result', 'Training dataset completed!!!')


b1 = tk.Button(window, text="Training", font=("Algerian", 20), bg='orange', fg='red', command=train_classifier)
b1.grid(column=0, row=4)

def generate_dataset():

        mycursor = connection.cursor()
        mycursor.execute("SELECT * from my_table")
        myresult = mycursor.fetchall()
        id = 1
        for x in myresult:
            id += 1
        sql = "insert into my_table(id,Name,Age,Address) values(%s,%s,%s,%s)"
        val = (id, t1.get(), t2.get(), t3.get())
        mycursor.execute(sql, val)
        connection.commit()

        face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

        def face_cropped(img):
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = face_classifier.detectMultiScale(gray, 1.3, 5)
            # scaling factor=1.3
            # Minimum neighbor = 5

            if faces is ():
                return None
            for (x, y, w, h) in faces:
                cropped_face = img[y:y + h, x:x + w]
            return cropped_face

        cap = cv2.VideoCapture(0)
        img_id = 0

        while True:
            ret, frame = cap.read()
            if face_cropped(frame) is not None:
                img_id += 1
                face = cv2.resize(face_cropped(frame), (200, 200))
                face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
                file_name_path = "data/user." + str(id) + "." + str(img_id) + ".jpg"
                cv2.imwrite(file_name_path, face)
                cv2.putText(face, str(img_id), (50, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)
                # (50,50) is the origin point from where text is to be written
                # font scale=1
                # thickness=2

                cv2.imshow("Cropped face", face)
                if cv2.waitKey(1) == 13 or int(img_id) == 200:
                    break
        cap.release()
        cv2.destroyAllWindows()
        messagebox.showinfo('Result', 'Generating dataset completed!!!')


b3 = tk.Button(window, text="Generate dataset", font=("Algerian", 20), bg='pink', fg='black', command=generate_dataset)
b3.grid(column=2, row=4)

window.geometry("800x200")
window.mainloop()