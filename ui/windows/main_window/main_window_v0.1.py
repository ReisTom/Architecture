# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\tomre\PycharmProjects\Architecture\ui\Windows\main_window\main_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1176, 885)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_main = QtWidgets.QFrame(self.centralwidget)
        self.frame_main.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_main.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_main.setObjectName("frame_main")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_main)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_header = QtWidgets.QFrame(self.frame_main)
        self.frame_header.setMinimumSize(QtCore.QSize(0, 70))
        self.frame_header.setMaximumSize(QtCore.QSize(16777215, 70))
        self.frame_header.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_header.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_header.setLineWidth(0)
        self.frame_header.setObjectName("frame_header")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_header)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame_toogle = QtWidgets.QFrame(self.frame_header)
        self.frame_toogle.setMaximumSize(QtCore.QSize(70, 16777215))
        self.frame_toogle.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_toogle.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_toogle.setLineWidth(0)
        self.frame_toogle.setMidLineWidth(1)
        self.frame_toogle.setObjectName("frame_toogle")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_toogle)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.btn_tgl_menu = QtWidgets.QPushButton(self.frame_toogle)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_tgl_menu.sizePolicy().hasHeightForWidth())
        self.btn_tgl_menu.setSizePolicy(sizePolicy)
        self.btn_tgl_menu.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.btn_tgl_menu.setStyleSheet("QPushButton {\n"
"    background-image: url(:/24x24/icons/24x24/cil-menu.png);\n"
"    background-position: center;\n"
"    background-repeat: no-reperat;\n"
"    border: none;\n"
"    background-color: rgb(80, 74, 64);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(133, 127, 114);\n"
"}\n"
"QPushButton:pressed {    \n"
"    background-color: rgb(98, 93, 82);\n"
"}")
        self.btn_tgl_menu.setText("")
        self.btn_tgl_menu.setObjectName("btn_tgl_menu")
        self.horizontalLayout_3.addWidget(self.btn_tgl_menu)
        self.horizontalLayout_2.addWidget(self.frame_toogle)
        self.frame_header_content = QtWidgets.QFrame(self.frame_header)
        self.frame_header_content.setToolTipDuration(0)
        self.frame_header_content.setStyleSheet("background-color: rgb(184, 178, 167);")
        self.frame_header_content.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_header_content.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_header_content.setObjectName("frame_header_content")
        self.horizontalLayout_2.addWidget(self.frame_header_content)
        self.verticalLayout_2.addWidget(self.frame_header)
        self.frame_center = QtWidgets.QFrame(self.frame_main)
        self.frame_center.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_center.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_center.setObjectName("frame_center")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_center)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame_side_menu = QtWidgets.QFrame(self.frame_center)
        self.frame_side_menu.setMinimumSize(QtCore.QSize(70, 0))
        self.frame_side_menu.setMaximumSize(QtCore.QSize(70, 16777215))
        self.frame_side_menu.setAutoFillBackground(False)
        self.frame_side_menu.setStyleSheet("background-color: rgb(80, 74, 64);")
        self.frame_side_menu.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_side_menu.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_side_menu.setLineWidth(1)
        self.frame_side_menu.setObjectName("frame_side_menu")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_side_menu)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.frame = QtWidgets.QFrame(self.frame_side_menu)
        self.frame.setToolTipDuration(-1)
        self.frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_4.addWidget(self.frame)
        self.horizontalLayout.addWidget(self.frame_side_menu)
        self.frame_content = QtWidgets.QFrame(self.frame_center)
        self.frame_content.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_content.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_content.setObjectName("frame_content")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_content)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame_main_content = QtWidgets.QFrame(self.frame_content)
        self.frame_main_content.setStyleSheet("background-color: rgb(66, 61, 51);")
        self.frame_main_content.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_main_content.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_main_content.setObjectName("frame_main_content")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_main_content)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.stackedWidget = QtWidgets.QStackedWidget(self.frame_main_content)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page_color = QtWidgets.QWidget()
        self.page_color.setObjectName("page_color")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.page_color)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.color_palett = QtWidgets.QFrame(self.page_color)
        self.color_palett.setMaximumSize(QtCore.QSize(16777215, 60))
        self.color_palett.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.color_palett.setFrameShadow(QtWidgets.QFrame.Raised)
        self.color_palett.setObjectName("color_palett")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.color_palett)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.frame_4 = QtWidgets.QFrame(self.color_palett)
        self.frame_4.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0.523, x2:1, y2:0.5, stop:0 rgb(250, 249, 247), stop:1 rgb(39, 36, 29));")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout_5.addWidget(self.frame_4)
        self.verticalLayout_5.addWidget(self.color_palett)
        self.frame_3 = QtWidgets.QFrame(self.page_color)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_5.addWidget(self.frame_3)
        self.stackedWidget.addWidget(self.page_color)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.stackedWidget.addWidget(self.page_2)
        self.horizontalLayout_4.addWidget(self.stackedWidget)
        self.verticalLayout_3.addWidget(self.frame_main_content)
        self.horizontalLayout.addWidget(self.frame_content)
        self.verticalLayout_2.addWidget(self.frame_center)
        self.frame_center.raise_()
        self.frame_header.raise_()
        self.verticalLayout.addWidget(self.frame_main)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
