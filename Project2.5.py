#!/usr/bin/python3

"""
Fall 2017 CSc 690 

File: Browser Warmup
This example shows how to open a display window

Author: Andrew Streckfus
Last edited: 9/4/17
"""

import sys
import os
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt, QUrl
from PyQt5.QtMultimedia import QSoundEffect
class Window(QWidget):
 
    def __init__(self,width,height):
        super().__init__()
        self.height = height
        self.width = width
        self.index = 0
        self.leftBreak = 0
        self.rightBreak = 4
        self.bigPixList = []
        self.pixList = []
        self.label = []
        self.bigLabel = QLabel(self)
        self.bigLabel.resize(self.width - 100, self.height - 100)
        self.bigLabel.move(50,50)
        self.bigLabel.hide()
        self.mode = 0
        self.soundClick = QSoundEffect()
        self.soundClickWah = QSoundEffect()
        self.soundLoop = QSoundEffect()
        self.soundLoopWah = QSoundEffect()
        self.soundShift = QSoundEffect()
        self.soundShiftWah = QSoundEffect()
        self.soundClick.setSource(QUrl.fromLocalFile(os.path.join('sounds','PianoNote.wav')))
        self.soundClickWah.setSource(QUrl.fromLocalFile(os.path.join('sounds','PianoNoteWah.wav')))
        self.soundShift.setSource(QUrl.fromLocalFile(os.path.join('sounds','PianoMultiNote.wav')))
        self.soundShiftWah.setSource(QUrl.fromLocalFile(os.path.join('sounds','PianoMultiNoteWah.wav')))
        self.soundLoop.setSource(QUrl.fromLocalFile(os.path.join('sounds','loop08.wav')))
        self.soundLoopWah.setSource(QUrl.fromLocalFile(os.path.join('sounds','loop08Wah.wav')))
        self.soundLoop.setLoopCount(QSoundEffect.Infinite)
        self.soundLoopWah.setLoopCount(QSoundEffect.Infinite)
        self.soundLoop.play()
        self.soundLoopWah.play()
        self.soundLoopWah.setMuted(1)
        self.initUI()
 
    def initUI(self):
        # title of window
        self.setWindowTitle('PyQt5 Main Window')
        # place window on screen at x=0, y=0
        self.setGeometry(0, 0, self.width, self.height)
        self.setStyleSheet('background-color: black')
        #sets up QLabels for later input
        for i in range(0, 5, 1):
            self.label.append(QLabel(self))
            self.label[i].move(self.width / 12 + i * self.width / 6, self.height / 3)
            self.label[i].resize(self.width / 6, self.height / 6)
            self.label[i].setStyleSheet('background-color: red')
            if(i == 0):
                self.label[i].setStyleSheet('background-color: blue')
        #places pictures into pixmap array
        i = 0
        for file in os.listdir('data'):
            self.pixList.append(QPixmap(os.path.join('data', file)))
            self.bigPixList.append(QPixmap(os.path.join('data',file)))
            if(self.pixList[i].height() > self.height / 6 - 10):
                self.pixList[i] = self.pixList[i].scaledToHeight(self.height / 6 - 10)
            if(self.pixList[i].width() > self.width / 6 - 10):
                self.pixList[i] = self.pixList[i].scaledToWidth(self.width / 6 - 10)
            if(self.bigPixList[i].width() > self.width - 100):
                self.bigPixList[i] = self.bigPixList[i].scaledToWidth(self.width - 100)
            if(self.bigPixList[i].height() > self.height-100):
                self.bigPixList[i] = self.bigPixList[i].scaledToHeight(self.height - 100)
            i = i + 1
        self.bigLabel.setAlignment(Qt.AlignCenter)
        self.bigLabel.setPixmap(self.bigPixList[0])
        #puts initial pixmaps into the designated qlabels
        for i in range(0, 5, 1):
            self.label[i].setPixmap(self.pixList[i])
            self.label[i].setAlignment(Qt.AlignCenter)
        self.show()
    #Moves the pointer to the picture one to the left.  If it breaks the bounds, it will move the frame
    def moveIndexLeft(self):
        j = 0
        self.label[self.index % 5].setStyleSheet('background-color:red')
        self.index = self.index - 1
        if(self.index < self.leftBreak):
            self.leftBreak = self.leftBreak - 5
            self.rightBreak = self.rightBreak - 5
            for i in range(self.leftBreak, 1 + self.rightBreak, 1):
                self.label[j].setPixmap(self.pixList[i % len(self.pixList)])
                self.label[j].setAlignment(Qt.AlignCenter)
                j = j + 1
        self.label[self.index % 5].setStyleSheet('background-color: blue')
        self.bigLabel.setPixmap(self.bigPixList[self.index % len(self.pixList)])
    #Moves the pointer one picture to the right.  If it breaks the bounds of QLabel it will move the frame
    def moveIndexRight(self):
        j = 0
        self.label[self.index % 5].setStyleSheet('background-color: red')
        self.index = self.index + 1
        if(self.index > self.rightBreak):
            self.leftBreak = self.leftBreak + 5
            self.rightBreak = self.rightBreak + 5
            for i in range(self.leftBreak, 1 + self.rightBreak, 1):
                self.label[j].setPixmap(self.pixList[i % len(self.pixList)])
                self.label[j].setAlignment(Qt.AlignCenter)
                j = j + 1
        self.label[self.index % 5].setStyleSheet('background-color: blue')
        self.bigLabel.setPixmap(self.bigPixList[self.index % len(self.pixList)])
    #Zooms in on the specific picture selected and puts it into a 700 x 500 frame    
    def zoomIn(self):
        self.mode = 1
        for i in range(0, 5, 1):
            self.label[i].hide()
        self.bigLabel.setAlignment(Qt.AlignCenter)
        self.bigLabel.show()
    #Goes back to default view
    def zoomOut(self):
        self.mode = 0
        self.bigLabel.hide()
        for i in range(0, 5, 1):
            self.label[i].show()
    #shifts the frame 5 pictures to the left
    def shiftLeft(self):
        self.label[self.index % 5].setStyleSheet('background-color:red')
        j = 0
        self.index = self.leftBreak - 1
        self.leftBreak = self.leftBreak - 5
        self.rightBreak = self.rightBreak - 5
        for i in range(self.leftBreak, 1 + self.rightBreak, 1):
            self.label[j].setPixmap(self.pixList[i % len(self.pixList)])
            j = j + 1
        self.label[self.index % 5].setStyleSheet('background-color: blue')
        self.bigLabel.setPixmap(self.bigPixList[self.index % len(self.pixList)])
    #shifts the frame 5 pictures to the right
    def shiftRight(self):
        self.label[self.index % 5].setStyleSheet('background-color: red')
        j = 0
        self.index = self.rightBreak + 1
        self.rightBreak = self.rightBreak + 5
        self.leftBreak = self.leftBreak + 5
        for i in range(self.leftBreak, 1 + self.rightBreak, 1):
            self.label[j].setPixmap(self.pixList[i % len(self.pixList)])
            j = j + 1
        self.label[self.index % 5].setStyleSheet('background-color: blue')
        self.bigLabel.setPixmap(self.bigPixList[self.index % len(self.pixList)])
    #all of the key inputs and their responses in functions
    def keyPressEvent(self, event):
        if(event.key() == 16777234):
            self.moveIndexLeft()
            if(self.mode == 0):
                self.soundClick.play()
            else:
                self.soundClickWah.play()
        if(event.key() == 16777236):
            self.moveIndexRight()
            if(self.mode == 0):
                self.soundClick.play()
            else:
                self.soundClickWah.play()
        if(event.key() == 16777235):
            self.zoomIn()
            self.soundLoop.setMuted(1)
            self.soundLoopWah.setMuted(0)
        if(event.key() == 16777237):
            self.zoomOut()
            self.soundLoopWah.setMuted(1)
            self.soundLoop.setMuted(0)
        if(event.key() == 44):
            self.shiftLeft()
            if(self.mode == 0):
                self.soundShift.play()
            else:
                self.soundShiftWah.play()
        if(event.key() == 46):
            self.shiftRight()
            if(self.mode == 0):
                self.soundShift.play()
            else:
                self.soundShiftWah.play()
    def mousePressEvent(self, QMouseEvent):
        if(self.mode == 0):
            setPicTo = -1
            if(QMouseEvent.y() > self.height / 3 - 1 and QMouseEvent.y() < self.height / 2 + 1):
                if(QMouseEvent.x() > self.width / 12 and QMouseEvent.x() < self.width * 3 / 12 + 1):
                    setPicTo = 0
                if(QMouseEvent.x() > self.width * 3 / 12  and QMouseEvent.x() < self.width * 5 / 12 + 1):
                    setPicTo = 1
                if(QMouseEvent.x() > self.width * 5 / 12  and QMouseEvent.x() < self.width * 7 / 12 + 1):
                    setPicTo = 2
                if(QMouseEvent.x() > self.width * 7 / 12  and QMouseEvent.x() < self.width * 9 / 12 + 1):
                    setPicTo = 3
                if(QMouseEvent.x() > self.width * 9 / 12  and QMouseEvent.x() < self.width * 11 / 12 + 1):
                    setPicTo = 4
                if(setPicTo > -1):
                    self.label[self.index % 5].setStyleSheet('background-color:red')
                    self.mode = 1
                    self.index = self.leftBreak + setPicTo
                    self.label[self.index % 5].setStyleSheet('background-color:blue')
                    self.bigLabel.setPixmap(self.bigPixList[self.index % len(self.pixList)])
                    for i in range(0, 5, 1):
                        self.label[i].hide()
                    self.bigLabel.setAlignment(Qt.AlignCenter)
                    self.bigLabel.show()
if __name__ == '__main__':
    app = QApplication(sys.argv)
    if(len(sys.argv) == 1):
        h = 600
        w = 800
    elif(int(sys.argv[1]) < 600 or int(sys.argv[1]) > 1200):
        print("width and height out of bounds, using default values of 600 and 800")
        h = 600
        w = 800
    else:
        w = int(sys.argv[1])
        h = int(sys.argv[1]) * 3 / 4
    window = Window(w,h)
    sys.exit(app.exec_())