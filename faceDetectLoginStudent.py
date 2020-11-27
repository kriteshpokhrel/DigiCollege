from tkinter import *
from tkinter import messagebox
import cv2
import os
from PIL import Image
import numpy as np
import mysql.connector
from db_connect import *
from studentHome import *
import time
global uDetect
uDetect= 0
global detect
detect= 0
class dFaceStudent:
    def __init__(self):
        self.detect_face()
    def detect_face(self):

        def draw_boundary(img, classifier, scaleFactor, minNeighbors, color, text, clf):
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray_image, scaleFactor, minNeighbors)

            coords = []

            for (x, y, w, h) in features:
                cv2.rectangle(img, (x, y), (x + w, y + h), color, 2)
                id, pred = clf.predict(gray_image[y:y + h, x:x + w])
                confidence = int(100 * (1 - pred / 300))

                mycursor = connection.cursor()
                mycursor.execute("select sal, S_Name, S_ID ,Section from digiFaceStudent where id=" + str(id))
                all = mycursor.fetchone()
                global S_Name
                global S_ID
                global sal
                global sec
                sal = all[0]
                S_Name = all[1]
                S_ID = all[2]
                sec = all[3]
                if confidence > 74:
                    global detect
                    detect += 1
                    cv2.putText(img, S_Name, (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 1, cv2.LINE_AA)
                    # cant call sHome here
                else:
                    global uDetect
                    uDetect += 1
                    cv2.putText(img, "UNKNOWN", (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 1, cv2.LINE_AA)
                coords = [x, y, w, h]
            return coords

        def recognize(img, clf, faceCascade):
            coords = draw_boundary(img, faceCascade, 1.1, 10, (255, 255, 255), "Face", clf)
            return img


        faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_capture = cv2.VideoCapture(0)

        while True:

            ret, img = video_capture.read()
            img = recognize(img, clf, faceCascade)
            cv2.imshow("DigiFace Login", img)
            if cv2.waitKey(1) == 13:
                break
            if detect >10 and cv2.waitKey(1):
                s1= sHome(sal,S_Name,S_ID,sec)
                s1
                video_capture.release()
                cv2.destroyWindow("DigiFace Login")
                break
            if uDetect >10000000:
                messagebox.showerror("Error","Face not matched to any accounts")
                break
        video_capture.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    d1=dFaceStudent()
    d1

