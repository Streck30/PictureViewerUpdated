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
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QAction, QLineEdit, QMessageBox
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
        self.tagLabels = []
        self.bigLabel = QLabel(self)
        self.bigLabel.resize(self.width * 3 / 4, self.height * 3 / 4)
        self.bigLabel.move(self.width / 8, self.height / 8)
        self.bigLabel.hide()
        #adding buttons and textbox
        self.textBox = QLineEdit(self)
        self.textBox.setStyleSheet("color: rgb(255, 255, 255);")
        self.textBox.move(self.width / 6, self.height * 7 / 8)
        self.textBox.resize(150,self.height / 16)
        self.textBox.hide()
        self.tagButton = QPushButton('Add Tag', self)
        self.tagButton.setStyleSheet("background-color: rgb(125,125,125);")
        self.tagButton.move(self.width / 6, self.height * 15 / 16)
        self.tagButton.clicked.connect(self.tagClick)
        self.tagButton.hide()
        self.saveTagButton = QPushButton('Save All Tags', self)
        self.saveTagButton.setStyleSheet("background-color: rgb(125, 125, 125);")
        self.saveTagButton.move(self.width / 6 + 75, self.height * 15 / 16)
        self.saveTagButton.clicked.connect(self.saveClick)
        self.saveTagButton.hide()
        self.setFocus()
        #item that holds the current string to be stored as tag
        self.currentString = []
        self.mode = 0
        #Sets up the warning message for too long strings
        self.warningMessage = QLabel(self)
        self.warningMessage.resize(self.width / 5, self.height / 16)
        self.warningMessage.setStyleSheet("background-color: red; font: bold 14px")
        self.warningMessage.setText("String too long")
        self.warningMessage.move(self.width / 2, self.height * 7 / 8)
        self.warningMessage.hide()
        #setting up the sounds to use
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
    #Adds the tag to the list triggered by clicking on the button only if the string is less than 11 characters, otherwise shows warning message
    def tagClick(self):
        tagValue = self.textBox.text()
        if(len(tagValue) < 11):
            self.currentString[self.index % len(self.pixList)] += (tagValue + "\n")
            self.tagLabels[self.index % len(self.pixList)].setText(self.currentString[self.index % len(self.pixList)])
            self.textBox.setText("")
            self.setFocus()
            self.warningMessage.hide()
        else:
            self.warningMessage.show()
    def saveClick(self):
        f = open('SavedTags.txt','w')
        f.truncate()
        for i in range(0, len(self.pixList), 1):
            f.write(self.tagLabels[i].text())
            f.write("#")
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
            self.tagLabels.append(QLabel(self))
            self.currentString.append("")
            self.tagLabels[i].resize(self.width / 8, self.height)
            self.tagLabels[i].move(self.width * 7 / 8, 0)
            self.tagLabels[i].setStyleSheet('border-color: grey; border-style: outset; border-width: 5px; font: bold 14px; color: white')
            self.tagLabels[i].setAlignment(Qt.AlignTop)
            self.tagLabels[i].hide()
            if(self.pixList[i].height() > self.height / 6 - 10):
                self.pixList[i] = self.pixList[i].scaledToHeight(self.height / 6 - 10)
            if(self.pixList[i].width() > self.width / 6 - 10):
                self.pixList[i] = self.pixList[i].scaledToWidth(self.width / 6 - 10)
            if(self.bigPixList[i].width() > self.width*3/4 ):
                self.bigPixList[i] = self.bigPixList[i].scaledToWidth(self.width*3/4)
            if(self.bigPixList[i].height() > self.height*3/4):
                self.bigPixList[i] = self.bigPixList[i].scaledToHeight(self.height*3/4)
            i = i + 1
        self.bigLabel.setAlignment(Qt.AlignCenter)
        self.bigLabel.setPixmap(self.bigPixList[0])
        #puts initial pixmaps into the designated qlabels
        for i in range(0, 5, 1):
            self.label[i].setPixmap(self.pixList[i])
            self.label[i].setAlignment(Qt.AlignCenter)
        self.show()
        self.loadTags()
    def loadTags(self):
        f = open('SavedTags.txt','r')
        tempString = f.read()
        j = 0
        for i in range(0, len(tempString), 1):
            if(tempString[i] != "#"):
                self.currentString[j]+=tempString[i]
            else:
                self.tagLabels[j].setText(self.currentString[j])
                j = j + 1

    #Moves the pointer to the picture one to the left.  If it breaks the bounds, it will move the frame
    def moveIndexLeft(self):
        j = 0
        if(self.mode == 1):
            self.tagLabels[self.index % len(self.pixList)].hide()
            self.tagLabels[(self.index - 1) % len(self.pixList)].show()
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
        self.textBox.setText("")
    #Moves the pointer one picture to the right.  If it breaks the bounds of QLabel it will move the frame
    def moveIndexRight(self):
        j = 0
        if(self.mode == 1):
            self.tagLabels[self.index % len(self.pixList)].hide()
            self.tagLabels[(self.index + 1) % len(self.pixList)].show()
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
        self.textBox.setText("")
    #Zooms in on the specific picture selected and puts it into a 700 x 500 frame    
    def zoomIn(self):
        self.mode = 1
        for i in range(0, 5, 1):
            self.label[i].hide()
        self.bigLabel.setAlignment(Qt.AlignCenter)
        self.bigLabel.show()
        self.tagButton.show()
        self.saveTagButton.show()
        self.textBox.show()
        self.tagLabels[self.index % len(self.pixList)].show()
    #Goes back to default view
    def zoomOut(self):
        self.mode = 0
        self.bigLabel.hide()
        for i in range(0, 5, 1):
            self.label[i].show()
        self.tagButton.hide()
        self.saveTagButton.hide()
        self.textBox.hide()
        self.tagLabels[self.index % len(self.pixList)].hide()
    #shifts the frame 5 pictures to the left
    def shiftLeft(self):
        if(self.mode == 1):
            self.tagLabels[self.index % len(self.pixList)].hide()
        self.label[self.index % 5].setStyleSheet('background-color:red')
        j = 0
        self.index = self.leftBreak - 1
        if(self.mode == 1):
            self.tagLabels[self.index % len(self.pixList)].show()
        self.leftBreak = self.leftBreak - 5
        self.rightBreak = self.rightBreak - 5
        for i in range(self.leftBreak, 1 + self.rightBreak, 1):
            self.label[j].setPixmap(self.pixList[i % len(self.pixList)])
            j = j + 1
        self.label[self.index % 5].setStyleSheet('background-color: blue')
        self.bigLabel.setPixmap(self.bigPixList[self.index % len(self.pixList)])
        self.textBox.setText("")
    #shifts the frame 5 pictures to the right
    def shiftRight(self):
        if(self.mode == 1):
            self.tagLabels[self.index % len(self.pixList)].hide()
        self.label[self.index % 5].setStyleSheet('background-color: red')
        j = 0
        self.index = self.rightBreak + 1
        if(self.mode == 1):
            self.tagLabels[self.index % len(self.pixList)].show()
        self.rightBreak = self.rightBreak + 5
        self.leftBreak = self.leftBreak + 5
        for i in range(self.leftBreak, 1 + self.rightBreak, 1):
            self.label[j].setPixmap(self.pixList[i % len(self.pixList)])
            j = j + 1
        self.label[self.index % 5].setStyleSheet('background-color: blue')
        self.bigLabel.setPixmap(self.bigPixList[self.index % len(self.pixList)])
        self.textBox.setText("")
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
        if(QMouseEvent.y() < self.height / 7 * 8 or QMouseEvent.y() > self.height / 15 * 16 and QMouseEvent.x() < self.width / 6 or QMouseEvent.x() > self.width / 3):
            self.setFocus()
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
