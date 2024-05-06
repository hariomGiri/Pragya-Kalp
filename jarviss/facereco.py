import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QApplication
from PyQt5 import QtGui
from face import Ui_Form
import cv2
import face_recognition
import numpy
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtCore import QTimer
import os

class facerecog(QWidget):
    def __init__(self):
        super(facerecog, self).__init__()
        print("Main File")
        self.faceui = Ui_Form()  # Instantiate the Ui_mainGuifile class
        self.faceui.setupUi(self)  # Now you can call the setupUi method
        self.faceui.exitbutton.clicked.connect(self.close)
def runProgram(self):
    self.videoPath = cv2.VideoCapture(0)
    self.encodeImages(videoPath)
def encodeImages(self, cameraName):
    print("encoding started")
    if len(cameraName) == 1:
        self.capture = cv2.VideoCapture(int(cameraName))
    else:
        self.capture = cv2.VideoCapture(cameraName)
    self.timer = QTimer(self)
    path = 'images'
    if not os.path.exists(path):
            os.mkdir(path)
            
    images = []
    self.classNames = []
    self.enecodelist = []
    photoList = os.listdir(path)
    for cl in photoList:
        currentImage = cv2.imread(f'{path}/{cl}')
        images.append(currentImage)
        self.classNames.append(os.path.splitext(cl)[0])
        for img in images:
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            box = face_recognition.face_locations(img)
            encodeCurFrame = face_recognition.face_encodings(img, box)[0]
            self.encodeList.append(encodeCurFrame)
            
        print("Images encoded successfully")
        self.timer.timeout.connect(self.updateFrames)
        self.timer.start(10)
def updateFrames(self):
    ret, self.image = self.capture.read()

def displayImage(selfm, image, enecodeList, classNames, window=1):
    image = cv2.resize(image, (601, 151))
    try:
        self.faceRecognition(image, enecodeList, classNames)
    except Exception as e:
        print(e)
    
def faceRecognition(self, image, encodeList,className ):
    
if __name__ == "__main__":
    app = QApplication
    (sys.argv)
    ui = facerecog()
    ui.show()
    sys.exit(app.exec_())