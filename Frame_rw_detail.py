# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Frame_rw_detail.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Frame_rw_detail(object):
    def setupUi(self, Frame_rw_detail):
        Frame_rw_detail.setObjectName("Frame_rw_detail")
        Frame_rw_detail.resize(269, 229)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Frame_rw_detail.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(Frame_rw_detail)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 10, 51, 21))
        self.label.setObjectName("label")
        self.tv_flag = QtWidgets.QLabel(self.centralwidget)
        self.tv_flag.setGeometry(QtCore.QRect(80, 10, 31, 21))
        self.tv_flag.setObjectName("tv_flag")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 30, 251, 191))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.cb_spyDeal = QtWidgets.QComboBox(self.groupBox)
        self.cb_spyDeal.setGeometry(QtCore.QRect(90, 70, 81, 22))
        self.cb_spyDeal.setObjectName("cb_spyDeal")
        self.cb_spyDeal.addItem("")
        self.cb_spyDeal.addItem("")
        self.cb_spyDeal.addItem("")
        self.cb_foe1Format = QtWidgets.QComboBox(self.groupBox)
        self.cb_foe1Format.setGeometry(QtCore.QRect(30, 10, 61, 21))
        self.cb_foe1Format.setObjectName("cb_foe1Format")
        self.cb_foe1Format.addItem("")
        self.cb_foe1Format.addItem("")
        self.cb_foe1Format.addItem("")
        self.cb_foe1Format.addItem("")
        self.cb_foe1Format.addItem("")
        self.cb_foe1Format.addItem("")
        self.cb_foe1Format.addItem("")
        self.cb_foe1Format.addItem("")
        self.cb_foe1Format.addItem("")
        self.cb_foe1Format.addItem("")
        self.cb_foe2Switch = QtWidgets.QCheckBox(self.groupBox)
        self.cb_foe2Switch.setGeometry(QtCore.QRect(10, 40, 21, 21))
        self.cb_foe2Switch.setText("")
        self.cb_foe2Switch.setObjectName("cb_foe2Switch")
        self.cb_foe2Compare = QtWidgets.QComboBox(self.groupBox)
        self.cb_foe2Compare.setGeometry(QtCore.QRect(90, 40, 41, 22))
        self.cb_foe2Compare.setObjectName("cb_foe2Compare")
        self.cb_foe2Compare.addItem("")
        self.cb_foe2Compare.addItem("")
        self.ed_foe2Num = QtWidgets.QLineEdit(self.groupBox)
        self.ed_foe2Num.setGeometry(QtCore.QRect(130, 40, 31, 21))
        self.ed_foe2Num.setObjectName("ed_foe2Num")
        self.ed_foe1Num = QtWidgets.QLineEdit(self.groupBox)
        self.ed_foe1Num.setGeometry(QtCore.QRect(130, 10, 31, 21))
        self.ed_foe1Num.setObjectName("ed_foe1Num")
        self.cb_spy = QtWidgets.QCheckBox(self.groupBox)
        self.cb_spy.setGeometry(QtCore.QRect(10, 70, 91, 21))
        self.cb_spy.setObjectName("cb_spy")
        self.cb_foe1Switch = QtWidgets.QCheckBox(self.groupBox)
        self.cb_foe1Switch.setGeometry(QtCore.QRect(10, 10, 21, 21))
        self.cb_foe1Switch.setText("")
        self.cb_foe1Switch.setObjectName("cb_foe1Switch")
        self.cb_foe2Format = QtWidgets.QComboBox(self.groupBox)
        self.cb_foe2Format.setGeometry(QtCore.QRect(30, 40, 61, 21))
        self.cb_foe2Format.setObjectName("cb_foe2Format")
        self.cb_foe2Format.addItem("")
        self.cb_foe2Format.addItem("")
        self.cb_foe2Format.addItem("")
        self.cb_foe2Format.addItem("")
        self.cb_foe2Format.addItem("")
        self.cb_foe2Format.addItem("")
        self.cb_foe2Format.addItem("")
        self.cb_foe2Format.addItem("")
        self.cb_foe2Format.addItem("")
        self.cb_foe2Format.addItem("")
        self.cb_foe2Deal = QtWidgets.QComboBox(self.groupBox)
        self.cb_foe2Deal.setGeometry(QtCore.QRect(160, 40, 87, 22))
        self.cb_foe2Deal.setObjectName("cb_foe2Deal")
        self.cb_foe2Deal.addItem("")
        self.cb_foe2Deal.addItem("")
        self.cb_foe2Deal.addItem("")
        self.cb_foe2Deal.addItem("")
        self.cb_foe2Deal.addItem("")
        self.cb_foe2Deal.addItem("")
        self.cb_foe1Compare = QtWidgets.QComboBox(self.groupBox)
        self.cb_foe1Compare.setGeometry(QtCore.QRect(90, 10, 41, 22))
        self.cb_foe1Compare.setObjectName("cb_foe1Compare")
        self.cb_foe1Compare.addItem("")
        self.cb_foe1Compare.addItem("")
        self.bt_save = QtWidgets.QPushButton(self.groupBox)
        self.bt_save.setGeometry(QtCore.QRect(80, 150, 93, 28))
        self.bt_save.setObjectName("bt_save")
        self.cb_nightFight = QtWidgets.QCheckBox(self.groupBox)
        self.cb_nightFight.setGeometry(QtCore.QRect(190, 70, 61, 19))
        self.cb_nightFight.setObjectName("cb_nightFight")
        self.cb_format = QtWidgets.QCheckBox(self.groupBox)
        self.cb_format.setGeometry(QtCore.QRect(10, 100, 51, 16))
        self.cb_format.setObjectName("cb_format")
        self.cb_formatS = QtWidgets.QComboBox(self.groupBox)
        self.cb_formatS.setGeometry(QtCore.QRect(90, 100, 101, 21))
        self.cb_formatS.setObjectName("cb_formatS")
        self.cb_formatS.addItem("")
        self.cb_formatS.addItem("")
        self.cb_formatS.addItem("")
        self.cb_formatS.addItem("")
        self.cb_formatS.addItem("")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(10, 130, 231, 16))
        self.label_2.setObjectName("label_2")
        self.cb_foe1Deal = QtWidgets.QComboBox(self.groupBox)
        self.cb_foe1Deal.setGeometry(QtCore.QRect(160, 10, 87, 22))
        self.cb_foe1Deal.setObjectName("cb_foe1Deal")
        self.cb_foe1Deal.addItem("")
        self.cb_foe1Deal.addItem("")
        self.cb_foe1Deal.addItem("")
        self.cb_foe1Deal.addItem("")
        self.cb_foe1Deal.addItem("")
        self.cb_foe1Deal.addItem("")
        self.cb_openDetail = QtWidgets.QCheckBox(self.centralwidget)
        self.cb_openDetail.setGeometry(QtCore.QRect(140, 10, 131, 21))
        self.cb_openDetail.setObjectName("cb_openDetail")
        Frame_rw_detail.setCentralWidget(self.centralwidget)

        self.retranslateUi(Frame_rw_detail)
        QtCore.QMetaObject.connectSlotsByName(Frame_rw_detail)

    def retranslateUi(self, Frame_rw_detail):
        _translate = QtCore.QCoreApplication.translate
        Frame_rw_detail.setWindowTitle(_translate("Frame_rw_detail", "任务设置_详细"))
        self.label.setText(_translate("Frame_rw_detail", "当前点："))
        self.tv_flag.setText(_translate("Frame_rw_detail", "A"))
        self.cb_spyDeal.setItemText(0, _translate("Frame_rw_detail", "SL"))
        self.cb_spyDeal.setItemText(1, _translate("Frame_rw_detail", "换轮型"))
        self.cb_spyDeal.setItemText(2, _translate("Frame_rw_detail", "换单横"))
        self.cb_foe1Format.setItemText(0, _translate("Frame_rw_detail", "驱逐"))
        self.cb_foe1Format.setItemText(1, _translate("Frame_rw_detail", "轻巡"))
        self.cb_foe1Format.setItemText(2, _translate("Frame_rw_detail", "重巡"))
        self.cb_foe1Format.setItemText(3, _translate("Frame_rw_detail", "战列"))
        self.cb_foe1Format.setItemText(4, _translate("Frame_rw_detail", "战巡"))
        self.cb_foe1Format.setItemText(5, _translate("Frame_rw_detail", "航母"))
        self.cb_foe1Format.setItemText(6, _translate("Frame_rw_detail", "轻母"))
        self.cb_foe1Format.setItemText(7, _translate("Frame_rw_detail", "潜艇"))
        self.cb_foe1Format.setItemText(8, _translate("Frame_rw_detail", "补给"))
        self.cb_foe1Format.setItemText(9, _translate("Frame_rw_detail", "雷巡"))
        self.cb_foe2Compare.setItemText(0, _translate("Frame_rw_detail", "≥"))
        self.cb_foe2Compare.setItemText(1, _translate("Frame_rw_detail", "＜"))
        self.ed_foe2Num.setText(_translate("Frame_rw_detail", "1"))
        self.ed_foe1Num.setText(_translate("Frame_rw_detail", "1"))
        self.cb_spy.setText(_translate("Frame_rw_detail", "索敌失败："))
        self.cb_foe2Format.setItemText(0, _translate("Frame_rw_detail", "驱逐"))
        self.cb_foe2Format.setItemText(1, _translate("Frame_rw_detail", "轻巡"))
        self.cb_foe2Format.setItemText(2, _translate("Frame_rw_detail", "重巡"))
        self.cb_foe2Format.setItemText(3, _translate("Frame_rw_detail", "战列"))
        self.cb_foe2Format.setItemText(4, _translate("Frame_rw_detail", "战巡"))
        self.cb_foe2Format.setItemText(5, _translate("Frame_rw_detail", "航母"))
        self.cb_foe2Format.setItemText(6, _translate("Frame_rw_detail", "轻母"))
        self.cb_foe2Format.setItemText(7, _translate("Frame_rw_detail", "潜艇"))
        self.cb_foe2Format.setItemText(8, _translate("Frame_rw_detail", "补给"))
        self.cb_foe2Format.setItemText(9, _translate("Frame_rw_detail", "雷巡"))
        self.cb_foe2Deal.setItemText(0, _translate("Frame_rw_detail", "SL"))
        self.cb_foe2Deal.setItemText(1, _translate("Frame_rw_detail", "单纵"))
        self.cb_foe2Deal.setItemText(2, _translate("Frame_rw_detail", "复纵"))
        self.cb_foe2Deal.setItemText(3, _translate("Frame_rw_detail", "轮型"))
        self.cb_foe2Deal.setItemText(4, _translate("Frame_rw_detail", "梯形"))
        self.cb_foe2Deal.setItemText(5, _translate("Frame_rw_detail", "单横"))
        self.cb_foe1Compare.setItemText(0, _translate("Frame_rw_detail", "≥"))
        self.cb_foe1Compare.setItemText(1, _translate("Frame_rw_detail", "＜"))
        self.bt_save.setText(_translate("Frame_rw_detail", "确认"))
        self.cb_nightFight.setText(_translate("Frame_rw_detail", "夜战"))
        self.cb_format.setText(_translate("Frame_rw_detail", "阵形:"))
        self.cb_formatS.setItemText(0, _translate("Frame_rw_detail", "单纵"))
        self.cb_formatS.setItemText(1, _translate("Frame_rw_detail", "复纵"))
        self.cb_formatS.setItemText(2, _translate("Frame_rw_detail", "轮型"))
        self.cb_formatS.setItemText(3, _translate("Frame_rw_detail", "梯形"))
        self.cb_formatS.setItemText(4, _translate("Frame_rw_detail", "单横"))
        self.label_2.setText(_translate("Frame_rw_detail", "注:索敌必定成功,索敌失败仅作为sl标志"))
        self.cb_foe1Deal.setItemText(0, _translate("Frame_rw_detail", "SL"))
        self.cb_foe1Deal.setItemText(1, _translate("Frame_rw_detail", "单纵"))
        self.cb_foe1Deal.setItemText(2, _translate("Frame_rw_detail", "复纵"))
        self.cb_foe1Deal.setItemText(3, _translate("Frame_rw_detail", "轮型"))
        self.cb_foe1Deal.setItemText(4, _translate("Frame_rw_detail", "梯形"))
        self.cb_foe1Deal.setItemText(5, _translate("Frame_rw_detail", "单横"))
        self.cb_openDetail.setText(_translate("Frame_rw_detail", "开启特殊设置"))

