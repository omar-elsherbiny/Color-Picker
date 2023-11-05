from PyQt5 import QtCore, QtGui, QtWidgets
import pyautogui as pygui
from math import radians, sin, cos


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 800)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.input_box = QtWidgets.QGroupBox(self.centralwidget)
        self.input_box.setGeometry(QtCore.QRect(25, 425, 750, 350))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.input_box.setFont(font)
        self.input_box.setTitle("")
        self.input_box.setStyleSheet(u"#input_box{\n""border: 1px solid black;}")
        self.input_box.setAlignment(QtCore.Qt.AlignCenter)
        self.input_box.setObjectName("input_box")
        self.label_frame = QtWidgets.QFrame(self.input_box)
        self.label_frame.setGeometry(QtCore.QRect(0, 0, 160, 350))
        self.label_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_frame.setStyleSheet(u"font: 25px MS Shell Dlg 2, sans-serif;")
        self.label_frame.setObjectName("label_frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.label_frame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.step_check = QtWidgets.QCheckBox(self.input_box)
        self.step_check.setObjectName(u"step_check")
        self.step_check.setGeometry(QtCore.QRect(12, 300, 100, 30))
        font3 = QtGui.QFont()
        font3.setPointSize(9)
        self.step_check.setFont(font3)
        self.format_check = QtWidgets.QCheckBox(self.input_box)
        self.format_check.setObjectName(u"format_check")
        self.format_check.setGeometry(QtCore.QRect(12, 320, 100, 30))
        self.format_check.setFont(font3)
        self.R_label = QtWidgets.QLabel(self.label_frame)
        self.R_label.setAlignment(QtCore.Qt.AlignCenter)
        self.R_label.setObjectName("R_label")
        self.verticalLayout.addWidget(self.R_label)
        self.G_label = QtWidgets.QLabel(self.label_frame)
        self.G_label.setAlignment(QtCore.Qt.AlignCenter)
        self.G_label.setObjectName("G_label")
        self.verticalLayout.addWidget(self.G_label)
        self.B_label = QtWidgets.QLabel(self.label_frame)
        self.B_label.setAlignment(QtCore.Qt.AlignCenter)
        self.B_label.setObjectName("B_label")
        self.verticalLayout.addWidget(self.B_label)
        self.R_slider = QtWidgets.QSlider(self.input_box)
        self.R_slider.setGeometry(QtCore.QRect(160, 12, 550, 104))
        self.R_slider.setMaximum(255)
        self.R_slider.setPageStep(30)
        self.R_slider.setOrientation(QtCore.Qt.Horizontal)
        self.R_slider.setObjectName("R_slider")
        self.G_slider = QtWidgets.QSlider(self.input_box)
        self.G_slider.setGeometry(QtCore.QRect(160, 123, 550, 104))
        self.G_slider.setMaximum(255)
        self.G_slider.setPageStep(30)
        self.G_slider.setOrientation(QtCore.Qt.Horizontal)
        self.G_slider.setObjectName("G_slider")
        self.B_slider = QtWidgets.QSlider(self.input_box)
        self.B_slider.setGeometry(QtCore.QRect(160, 234, 550, 104))
        self.B_slider.setMaximum(255)
        self.B_slider.setPageStep(30)
        self.B_slider.setOrientation(QtCore.Qt.Horizontal)
        self.B_slider.setObjectName("B_slider")
        self.wheel_col = QtWidgets.QLabel(self.centralwidget)
        self.wheel_col.setGeometry(QtCore.QRect(25, 25, 400, 400))
        self.wheel_col.setText("")
        self.wheel_col.setPixmap(QtGui.QPixmap("wheel.png"))
        self.wheel_col.setScaledContents(True)
        self.wheel_col.setObjectName("wheel_col")
        self.gradient_col1 = QtWidgets.QLabel(self.centralwidget)
        self.gradient_col1.setGeometry(QtCore.QRect(500, 25, 200, 187))
        self.gradient_col1.setStyleSheet("background-color: rgb(255, 255, 255);\n""border: 1px solid black;\n")
        self.gradient_col1.setText("")
        self.gradient_col1.setObjectName("gradient_col")
        self.gradient_col2 = QtWidgets.QLabel(self.centralwidget)
        self.gradient_col2.setGeometry(QtCore.QRect(500, 212, 200, 188))
        self.gradient_col2.setStyleSheet("background-color: rgb(255, 255, 255);\n""border: 1px solid black;\n")
        self.gradient_col2.setText("")
        self.gradient_col2.setObjectName("gradient_col")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.shortcut1 = QtWidgets.QShortcut(QtGui.QKeySequence("Ctrl+E"),MainWindow)
        self.shortcut1.activated.connect(self.copy_val)
        self.shortcut2 = QtWidgets.QShortcut(QtGui.QKeySequence("Ctrl+Q"),MainWindow)
        self.shortcut2.activated.connect(self.paste_val)
        self.clipboard = QtWidgets.QApplication.clipboard()
        self.pointer = QtWidgets.QLabel(self.centralwidget)
        self.pointer.setObjectName(u"pointer")
        self.pointer.setGeometry(QtCore.QRect(217, 217, 19, 19))
        font2 = QtGui.QFont()
        font2.setFamily(u"Arial")
        font2.setPointSize(14)
        font2.setBold(True)
        font2.setWeight(75)
        self.pointer.setFont(font2)

        self.upd_gradient(0,0,0)
        self.R_slider.valueChanged.connect(self.update_vals)
        self.G_slider.valueChanged.connect(self.update_vals)
        self.B_slider.valueChanged.connect(self.update_vals)
        self.step_check.stateChanged.connect(self.change_step)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Color PIcker by osh"))
        self.R_label.setText(_translate("MainWindow", "R: 0"))
        self.G_label.setText(_translate("MainWindow", "G: 0"))
        self.B_label.setText(_translate("MainWindow", "B: 0"))
        self.step_check.setText(_translate("MainWindow", "Small step"))
        self.format_check.setText(_translate("MainWindow", "HSV format"))
        self.pointer.setText(_translate("MainWindow", "O"))
    def change_step(self):
        if self.step_check.isChecked():
            self.R_slider.setPageStep(1)
            self.G_slider.setPageStep(1)
            self.B_slider.setPageStep(1)
        else:
            self.R_slider.setPageStep(30)
            self.G_slider.setPageStep(30)
            self.B_slider.setPageStep(30)
    def copy_val(self):
        r,g,b=self.R_slider.value(),self.G_slider.value(),self.B_slider.value()
        if self.format_check.isChecked():
            h,s,l=self.rgb_to_hsv(r,g,b)
            self.clipboard.setText(f'{(h,s,l)}')
        else:
            self.clipboard.setText(f'{(r,g,b)}')
        print(f"Copied value {self.clipboard.text()}")
    def paste_val(self):
        val=pygui.pixel(pygui.position()[0], pygui.position()[1])
        self.R_slider.setValue(val[0])
        self.G_slider.setValue(val[1])
        self.B_slider.setValue(val[2])
        self.update_vals()
    def rgb_to_hsv(self, R, G, B):
        r,g,b=R/255.0,G/255.0,B/255.0
        cmax,cmin=max(r,g,b),min(r,g,b)
        diff=cmax-cmin

        if cmax==cmin:
            h=0
        elif cmax==r:
            h=(60*((g-b)/diff)+360) % 360
        elif cmax==g:
            h=(60*((b-r)/diff)+120) % 360
        elif cmax==b:
            h=(60*((r-g)/diff)+240) % 360
        
        if cmax==0:
            s=0
        else:
            s=(diff/cmax)*100
        
        v=cmax*100

        return (round(h),round(s),round(v))  

    def update_vals(self):
        r=self.R_slider.value()
        g=self.G_slider.value()
        b=self.B_slider.value()
        self.upd_labels(r,g,b)
        self.upd_gradient(r,g,b)
        self.upd_wheel(self.rgb_to_hsv(r, g ,b))
    def upd_labels(self, r, g, b):
        self.R_label.setText(f"R: {r}")
        self.G_label.setText(f"G: {g}")
        self.B_label.setText(f"B: {b}")
    def upd_gradient(self, r, g, b):
        #self.gradient_col.setStyleSheet("border: 1px solid black;\n"f"background-color: rgb{(r, g, b)};\n")
        self.gradient_col1.setStyleSheet("border: 1px solid black;\n"f"border-bottom:5px solid rgb{(r, g, b)};\n"f"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(255,255,255,255), stop:1 rgba{(r, g, b, 255)});;\n")
        self.gradient_col2.setStyleSheet("border: 1px solid black;\n"f"border-top:5px solid rgb{(r, g, b)};\n"f"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba{(r, g, b, 255)}, stop:1 rgba(0, 0, 0, 255));;\n")
    def upd_wheel(self, hsv):
        h=radians(hsv[0])
        s=hsv[1]
        x=sin(h)*s*1.6
        y=cos(h)*s*1.6
        xpos, ypos=int(217+x),int(217-y)
        self.pointer.move(xpos,ypos)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
