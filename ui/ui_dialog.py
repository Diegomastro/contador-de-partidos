# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialog.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setWindowModality(QtCore.Qt.ApplicationModal)
        Dialog.resize(527, 374)
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout(Dialog)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_1 = QtWidgets.QLabel(Dialog)
        self.label_1.setObjectName("label_1")
        self.horizontalLayout.addWidget(self.label_1)
        spacerItem = QtWidgets.QSpacerItem(34, 17, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.lbl_totalplays = QtWidgets.QLabel(Dialog)
        self.lbl_totalplays.setObjectName("lbl_totalplays")
        self.horizontalLayout.addWidget(self.lbl_totalplays)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        spacerItem1 = QtWidgets.QSpacerItem(34, 17, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.lbl_totalwins = QtWidgets.QLabel(Dialog)
        self.lbl_totalwins.setObjectName("lbl_totalwins")
        self.horizontalLayout_2.addWidget(self.lbl_totalwins)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_3.addWidget(self.label_5)
        spacerItem2 = QtWidgets.QSpacerItem(33, 17, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.lbl_totallosses = QtWidgets.QLabel(Dialog)
        self.lbl_totallosses.setObjectName("lbl_totallosses")
        self.horizontalLayout_3.addWidget(self.lbl_totallosses)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_9 = QtWidgets.QLabel(Dialog)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_4.addWidget(self.label_9)
        spacerItem3 = QtWidgets.QSpacerItem(20, 17, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem3)
        self.lbl_mostplayedday = QtWidgets.QLabel(Dialog)
        self.lbl_mostplayedday.setObjectName("lbl_mostplayedday")
        self.horizontalLayout_4.addWidget(self.lbl_mostplayedday)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_17 = QtWidgets.QLabel(Dialog)
        self.label_17.setObjectName("label_17")
        self.horizontalLayout_5.addWidget(self.label_17)
        spacerItem4 = QtWidgets.QSpacerItem(22, 17, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem4)
        self.lbl_mostwinningday = QtWidgets.QLabel(Dialog)
        self.lbl_mostwinningday.setObjectName("lbl_mostwinningday")
        self.horizontalLayout_5.addWidget(self.lbl_mostwinningday)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_21 = QtWidgets.QLabel(Dialog)
        self.label_21.setObjectName("label_21")
        self.horizontalLayout_6.addWidget(self.label_21)
        spacerItem5 = QtWidgets.QSpacerItem(19, 17, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem5)
        self.lbl_mostlosingday = QtWidgets.QLabel(Dialog)
        self.lbl_mostlosingday.setObjectName("lbl_mostlosingday")
        self.horizontalLayout_6.addWidget(self.lbl_mostlosingday)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_13.addLayout(self.verticalLayout)
        spacerItem6 = QtWidgets.QSpacerItem(36, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_13.addItem(spacerItem6)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_7.addWidget(self.label_3)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem7)
        self.lbl_mostplaysinonesession = QtWidgets.QLabel(Dialog)
        self.lbl_mostplaysinonesession.setObjectName("lbl_mostplaysinonesession")
        self.horizontalLayout_7.addWidget(self.lbl_mostplaysinonesession)
        self.verticalLayout_2.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_8.addWidget(self.label_7)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem8)
        self.lbl_mostwinsinonesession = QtWidgets.QLabel(Dialog)
        self.lbl_mostwinsinonesession.setObjectName("lbl_mostwinsinonesession")
        self.horizontalLayout_8.addWidget(self.lbl_mostwinsinonesession)
        self.verticalLayout_2.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_15 = QtWidgets.QLabel(Dialog)
        self.label_15.setObjectName("label_15")
        self.horizontalLayout_9.addWidget(self.label_15)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem9)
        self.lbl_mostlossesinonesession = QtWidgets.QLabel(Dialog)
        self.lbl_mostlossesinonesession.setObjectName("lbl_mostlossesinonesession")
        self.horizontalLayout_9.addWidget(self.lbl_mostlossesinonesession)
        self.verticalLayout_2.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_11 = QtWidgets.QLabel(Dialog)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_10.addWidget(self.label_11)
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem10)
        self.lbl_avgplayspersession = QtWidgets.QLabel(Dialog)
        self.lbl_avgplayspersession.setObjectName("lbl_avgplayspersession")
        self.horizontalLayout_10.addWidget(self.lbl_avgplayspersession)
        self.verticalLayout_2.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.label_19 = QtWidgets.QLabel(Dialog)
        self.label_19.setObjectName("label_19")
        self.horizontalLayout_11.addWidget(self.label_19)
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem11)
        self.lbl_avgwinspersession = QtWidgets.QLabel(Dialog)
        self.lbl_avgwinspersession.setObjectName("lbl_avgwinspersession")
        self.horizontalLayout_11.addWidget(self.lbl_avgwinspersession)
        self.verticalLayout_2.addLayout(self.horizontalLayout_11)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.label_23 = QtWidgets.QLabel(Dialog)
        self.label_23.setObjectName("label_23")
        self.horizontalLayout_12.addWidget(self.label_23)
        spacerItem12 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem12)
        self.lbl_avglossespersession = QtWidgets.QLabel(Dialog)
        self.lbl_avglossespersession.setObjectName("lbl_avglossespersession")
        self.horizontalLayout_12.addWidget(self.lbl_avglossespersession)
        self.verticalLayout_2.addLayout(self.horizontalLayout_12)
        self.horizontalLayout_13.addLayout(self.verticalLayout_2)
        spacerItem13 = QtWidgets.QSpacerItem(31, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_13.addItem(spacerItem13)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_1.setText(_translate("Dialog", "Total Plays: "))
        self.lbl_totalplays.setText(_translate("Dialog", "TextLabel"))
        self.label_2.setText(_translate("Dialog", "Total Wins: "))
        self.lbl_totalwins.setText(_translate("Dialog", "TextLabel"))
        self.label_5.setText(_translate("Dialog", "Total Losses:"))
        self.lbl_totallosses.setText(_translate("Dialog", "TextLabel"))
        self.label_9.setText(_translate("Dialog", "Most played session:"))
        self.lbl_mostplayedday.setText(_translate("Dialog", "TextLabel"))
        self.label_17.setText(_translate("Dialog", "Most winning session:"))
        self.lbl_mostwinningday.setText(_translate("Dialog", "TextLabel"))
        self.label_21.setText(_translate("Dialog", "Most losing session:"))
        self.lbl_mostlosingday.setText(_translate("Dialog", "TextLabel"))
        self.label_3.setText(_translate("Dialog", "Most plays in one session:"))
        self.lbl_mostplaysinonesession.setText(_translate("Dialog", "TextLabel"))
        self.label_7.setText(_translate("Dialog", "Most Wins in one session:"))
        self.lbl_mostwinsinonesession.setText(_translate("Dialog", "TextLabel"))
        self.label_15.setText(_translate("Dialog", "Most Losses in one session:"))
        self.lbl_mostlossesinonesession.setText(_translate("Dialog", "TextLabel"))
        self.label_11.setText(_translate("Dialog", "Avg. Plays per session:"))
        self.lbl_avgplayspersession.setText(_translate("Dialog", "TextLabel"))
        self.label_19.setText(_translate("Dialog", "Avg Wins per session:"))
        self.lbl_avgwinspersession.setText(_translate("Dialog", "TextLabel"))
        self.label_23.setText(_translate("Dialog", "Avg. Losses per session:"))
        self.lbl_avglossespersession.setText(_translate("Dialog", "TextLabel"))

