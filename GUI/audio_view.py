from PyQt4 import QtGui, QtCore
from PyQt4.QtGui import QFont
from naoqi import ALProxy

import Controller as con
from robot import Util as ul

IP = ul.RobotIP
PORT = ul.RobotPORT

class Audio_View(QtGui.QWidget):
    def __init__(self,parent=None):
        super(Audio_View, self).__init__(parent)
        self.initUI()
        self.tabWidget1 = QtGui.QTabWidget()
        self.tabWidget2 = QtGui.QTabWidget()
        self.textEdit = QtGui.QTextEdit()
        self.volSlider = QtGui.QSlider()
        self.musicList = QtGui.QComboBox()

    def initUI(self):
        self.resize(1000, 600)
        self.setWindowTitle('Audio')
        self.setWindowIcon(QtGui.QIcon('C:/Users/zeyu/Desktop/NaoGUI/image/Icon.png'))
        audioBG_image = QtGui.QPixmap()
        audioBG_image.load('C:/Users/zeyu/Desktop/NaoGUI/image/subBG.png')
        audioBG = QtGui.QPalette()
        audioBG.setBrush(self.backgroundRole(), QtGui.QBrush(audioBG_image))
        self.setPalette(audioBG)
        self.setAutoFillBackground(True)

        volume_label = QtGui.QLabel(self)
        volume_label.setPixmap(QtGui.QPixmap('C:/Users/zeyu/Desktop/NaoGUI/image/volume.png'))
        volume_label.move(70, 50)

        Audio_View.volSlider = QtGui.QSlider(self)
        Audio_View.volSlider.setGeometry(QtCore.QRect(130, 50, 210, 30))
        Audio_View.volSlider.setOrientation(QtCore.Qt.Horizontal)
        Audio_View.volSlider.setRange(0, 100)

        Talk_button = QtGui.QPushButton("Text to Speech", self)
        Talk_button.resize(180, 80)
        Talk_button.move(140, 150)
        Talk_button.setFont(QFont("Consolas", 15))



        BM_button = QtGui.QPushButton("Back to Main", self)
        BM_button.resize(180, 80)
        BM_button.move(140, 320)
        BM_button.setFont(QFont("Consolas", 15))


        self.connect(Talk_button, QtCore.SIGNAL('clicked()'),
                     self.set_Talk_view)


        self.connect(BM_button, QtCore.SIGNAL('clicked()'),
                     self.BM_ButtonClicked)


    def set_Talk_view(self):
        self.tabWidget2.close()

        self.tabWidget1 = QtGui.QTabWidget(self)
        self.tabWidget1.setGeometry(QtCore.QRect(420, 100, 480, 400))
        self.tabWidget1.setFont(QFont("Consolas", 16))

        input_label = QtGui.QLabel("Input", self.tabWidget1)
        input_label.move(20, 60)
        self.textEdit = QtGui.QTextEdit(self.tabWidget1)
        self.textEdit.resize(300, 170)
        self.textEdit.move(100, 60)

        talk_button = QtGui.QPushButton("Talk", self.tabWidget1)
        talk_button.resize(150, 50)
        talk_button.move(180, 280)

        self.tabWidget1.show()

        self.connect(talk_button, QtCore.SIGNAL('clicked()'),
                     self.talk_ButtonClicked)

    def set_PM_view(self):
        self.tabWidget1.close()

        self.tabWidget2 = QtGui.QTabWidget(self)
        self.tabWidget2.setGeometry(QtCore.QRect(420, 100, 480, 400))
        self.tabWidget2.setFont(QFont("Consolas", 16))

        musiclist_label = QtGui.QLabel("Music List", self.tabWidget2)
        musiclist_label.move(10, 100)

        self.musicList = QtGui.QComboBox(self.tabWidget2)
        self.musicList.insertItem(1,  "Sugar - Maroon 5" )
        self.musicList.insertItem(2, "I know you are trouble - Taylor Swift")
        self.musicList.insertItem(3, "Hello - Adele")
        self.musicList.resize(300, 50)
        self.musicList.move(140, 90)

        play_button = QtGui.QPushButton("Play", self.tabWidget2)
        play_button.resize(70, 50)
        play_button.move(140, 250)

        pause_button = QtGui.QPushButton("Pause", self.tabWidget2)
        pause_button.resize(70, 50)
        pause_button.move(240, 250)

        stop_button = QtGui.QPushButton("Stop", self.tabWidget2)
        stop_button.resize(70, 50)
        stop_button.move(340, 250)

        self.tabWidget2.show()
        self.connect(play_button, QtCore.SIGNAL('clicked()'),
                     self.play_music)
        self.connect(play_button, QtCore.SIGNAL('clicked()'),
                     self.pause_music)
        self.connect(play_button, QtCore.SIGNAL('clicked()'),
                     self.stop_music)


    def talk_ButtonClicked(self):
        print(self.textEdit.toPlainText())
        text = str(self.textEdit.toPlainText())
        print(Audio_View.volSlider.value())
        volume = float(Audio_View.volSlider.value())
        print(volume)
        con.talk_motion(text,volume)
        self.textEdit.clear()

    def play_music(self):
        print(self.textEdit.toPlainText())
        print(Audio_View.volSlider.value())
        self.textEdit.clear()

    def pause_music(self):
        print(self.textEdit.toPlainText())
        print(self.vSlider.value())
        self.textEdit.clear()

    def stop_music(self):
        print(self.textEdit.toPlainText())
        print(self.vSlider.value())
        self.textEdit.clear()

    def BM_ButtonClicked(self):
        self.tabWidget1.close()
        self.tabWidget2.close()
        self.close()