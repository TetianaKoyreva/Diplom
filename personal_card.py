# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_personal_card.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSplitter, QVBoxLayout, QWidget)

class Ui_PersonalCard(object):
    def setupUi(self, PersonalCard):
        if not PersonalCard.objectName():
            PersonalCard.setObjectName(u"PersonalCard")
        PersonalCard.resize(1479, 889)
        PersonalCard.setStyleSheet(u"background-color: rgba(25, 25, 25, 255);\n"
"font-family: Roboto;\n"
"color:white;")
        self.label = QLabel(PersonalCard)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(9, 9, 368, 33))
        self.label.setStyleSheet(u"color:white;\n"
"font-size: 20pt;\n"
";\n"
"")
        self.widget = QWidget(PersonalCard)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(10, 69, 656, 925))
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 40)
        self.splitter = QSplitter(self.widget)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Horizontal)
        self.lb_surname_employee = QLabel(self.splitter)
        self.lb_surname_employee.setObjectName(u"lb_surname_employee")
        self.lb_surname_employee.setStyleSheet(u"color:white;\n"
"font-size: 14pt;\n"
";\n"
"")
        self.splitter.addWidget(self.lb_surname_employee)
        self.ln_surname_employee = QLineEdit(self.splitter)
        self.ln_surname_employee.setObjectName(u"ln_surname_employee")
        self.ln_surname_employee.setMaximumSize(QSize(1800, 16777215))
        self.ln_surname_employee.setStyleSheet(u"color:white;\n"
"font-size: 14pt;\n"
"")
        self.splitter.addWidget(self.ln_surname_employee)

        self.verticalLayout.addWidget(self.splitter)

        self.splitter_2 = QSplitter(self.widget)
        self.splitter_2.setObjectName(u"splitter_2")
        self.splitter_2.setOrientation(Qt.Horizontal)
        self.lbname_employee = QLabel(self.splitter_2)
        self.lbname_employee.setObjectName(u"lbname_employee")
        self.lbname_employee.setMaximumSize(QSize(180, 16777215))
        self.lbname_employee.setStyleSheet(u"color:white;\n"
"font-size:14pt;\n"
";\n"
"")
        self.splitter_2.addWidget(self.lbname_employee)
        self.ln_name_employee = QLineEdit(self.splitter_2)
        self.ln_name_employee.setObjectName(u"ln_name_employee")
        self.ln_name_employee.setMinimumSize(QSize(20, 28))
        self.ln_name_employee.setMaximumSize(QSize(1800, 28))
        self.ln_name_employee.setStyleSheet(u"color:white;\n"
"font-size: 14pt;\n"
"")
        self.splitter_2.addWidget(self.ln_name_employee)

        self.verticalLayout.addWidget(self.splitter_2)

        self.splitter_3 = QSplitter(self.widget)
        self.splitter_3.setObjectName(u"splitter_3")
        self.splitter_3.setOrientation(Qt.Horizontal)
        self.lb_paronymic_employee = QLabel(self.splitter_3)
        self.lb_paronymic_employee.setObjectName(u"lb_paronymic_employee")
        self.lb_paronymic_employee.setStyleSheet(u"color:white;\n"
"font-size:14pt;\n"
"\n"
"")
        self.splitter_3.addWidget(self.lb_paronymic_employee)
        self.ln_paronymic_employee = QLineEdit(self.splitter_3)
        self.ln_paronymic_employee.setObjectName(u"ln_paronymic_employee")
        self.ln_paronymic_employee.setMaximumSize(QSize(1800, 16777215))
        self.ln_paronymic_employee.setStyleSheet(u"color:white;\n"
"font-size: 14pt;\n"
"")
        self.splitter_3.addWidget(self.ln_paronymic_employee)

        self.verticalLayout.addWidget(self.splitter_3)

        self.splitter_4 = QSplitter(self.widget)
        self.splitter_4.setObjectName(u"splitter_4")
        self.splitter_4.setOrientation(Qt.Horizontal)
        self.widget1 = QWidget(self.splitter_4)
        self.widget1.setObjectName(u"widget1")
        self.gridLayout = QGridLayout(self.widget1)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.lb_sex = QLabel(self.widget1)
        self.lb_sex.setObjectName(u"lb_sex")
        self.lb_sex.setStyleSheet(u"color:white;\n"
"font-size:14pt;\n"
";\n"
"")

        self.gridLayout.addWidget(self.lb_sex, 0, 0, 1, 1)

        self.cb_sex = QComboBox(self.widget1)
        self.cb_sex.addItem("")
        self.cb_sex.addItem("")
        self.cb_sex.setObjectName(u"cb_sex")
        self.cb_sex.setStyleSheet(u"color:white;\n"
"font-size: 12pt;")

        self.gridLayout.addWidget(self.cb_sex, 0, 1, 1, 1)

        self.lb_family = QLabel(self.widget1)
        self.lb_family.setObjectName(u"lb_family")
        self.lb_family.setStyleSheet(u"color:white;\n"
"font-size:14pt;\n"
";\n"
"")

        self.gridLayout.addWidget(self.lb_family, 0, 2, 1, 1)

        self.cb_family = QComboBox(self.widget1)
        self.cb_family.addItem("")
        self.cb_family.addItem("")
        self.cb_family.addItem("")
        self.cb_family.addItem("")
        self.cb_family.setObjectName(u"cb_family")
        self.cb_family.setStyleSheet(u"color:white;\n"
"font-size: 12pt;")

        self.gridLayout.addWidget(self.cb_family, 0, 3, 1, 1)

        self.splitter_4.addWidget(self.widget1)

        self.verticalLayout.addWidget(self.splitter_4)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, -1, -1, 40)
        self.lb_birthdate = QLabel(self.widget)
        self.lb_birthdate.setObjectName(u"lb_birthdate")
        self.lb_birthdate.setStyleSheet(u"color:white;\n"
"font-size:14pt;\n"
";\n"
"")

        self.horizontalLayout.addWidget(self.lb_birthdate)

        self.ln_birthdate = QLineEdit(self.widget)
        self.ln_birthdate.setObjectName(u"ln_birthdate")
        self.ln_birthdate.setStyleSheet(u"color:white;\n"
"font-size:14pt;\n"
"")

        self.horizontalLayout.addWidget(self.ln_birthdate)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_department = QHBoxLayout()
        self.horizontalLayout_department.setObjectName(u"horizontalLayout_department")
        self.horizontalLayout_department.setContentsMargins(-1, -1, -1, 40)
        self.lb_department = QLabel(self.widget)
        self.lb_department.setObjectName(u"lb_department")
        self.lb_department.setStyleSheet(u"color:white;\n"
"font-size:14pt;\n"
";\n"
"")

        self.horizontalLayout_department.addWidget(self.lb_department)

        self.cb_department = QComboBox(self.widget)
        self.cb_department.addItem("")
        self.cb_department.addItem("")
        self.cb_department.addItem("")
        self.cb_department.setObjectName(u"cb_department")
        self.cb_department.setStyleSheet(u"color:white;\n"
"font-size: 12pt;")

        self.horizontalLayout_department.addWidget(self.cb_department)


        self.verticalLayout.addLayout(self.horizontalLayout_department)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(-1, -1, -1, 40)
        self.llb_category = QLabel(self.widget)
        self.llb_category.setObjectName(u"llb_category")
        self.llb_category.setStyleSheet(u"color:white;\n"
"font-size:14pt;\n"
";\n"
"")

        self.horizontalLayout_3.addWidget(self.llb_category)

        self.cb_category = QComboBox(self.widget)
        self.cb_category.addItem("")
        self.cb_category.addItem("")
        self.cb_category.addItem("")
        self.cb_category.setObjectName(u"cb_category")
        self.cb_category.setStyleSheet(u"color:white;\n"
"font-size: 12pt;")

        self.horizontalLayout_3.addWidget(self.cb_category)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(-1, -1, -1, 40)
        self.lb_profesion = QLabel(self.widget)
        self.lb_profesion.setObjectName(u"lb_profesion")
        self.lb_profesion.setStyleSheet(u"color:white;\n"
"font-size:14pt;\n"
";\n"
"")

        self.horizontalLayout_4.addWidget(self.lb_profesion)

        self.ln_add_profession = QLineEdit(self.widget)
        self.ln_add_profession.setObjectName(u"ln_add_profession")
        self.ln_add_profession.setStyleSheet(u"color:white;\n"
"font-size:14pt;\n"
"")

        self.horizontalLayout_4.addWidget(self.ln_add_profession)

        self.btn_professions = QPushButton(self.widget)
        self.btn_professions.setObjectName(u"btn_professions")
        self.btn_professions.setStyleSheet(u"QPushButton {\n"
"color: white;\n"
"background-color: rgba(89,89, 89, 100);\n"
"border-radius: 4 px;\n"
"border-color: rgb(127, 152, 110);\n"
"text-align: center;\n"
"width: 260px;\n"
"height: 50px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgba(127,152, 127, 100);\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgba(255, 255, 255, 70);\n"
"}\n"
"")

        self.horizontalLayout_4.addWidget(self.btn_professions)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(-1, -1, -1, 40)
        self.lb_start_worked = QLabel(self.widget)
        self.lb_start_worked.setObjectName(u"lb_start_worked")
        self.lb_start_worked.setStyleSheet(u"color:white;\n"
"font-size:14pt;\n"
";\n"
"")

        self.horizontalLayout_5.addWidget(self.lb_start_worked)

        self.ln_start_worked = QLineEdit(self.widget)
        self.ln_start_worked.setObjectName(u"ln_start_worked")
        self.ln_start_worked.setStyleSheet(u"color:white;\n"
"font-size:14pt;\n"
"")

        self.horizontalLayout_5.addWidget(self.ln_start_worked)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.splitter_5 = QSplitter(self.widget)
        self.splitter_5.setObjectName(u"splitter_5")
        self.splitter_5.setOrientation(Qt.Horizontal)
        self.lb_sumi = QLabel(self.splitter_5)
        self.lb_sumi.setObjectName(u"lb_sumi")
        self.lb_sumi.setStyleSheet(u"color:white;\n"
"font-size:14pt;\n"
";\n"
"")
        self.splitter_5.addWidget(self.lb_sumi)
        self.ln_sumiprofession = QLineEdit(self.splitter_5)
        self.ln_sumiprofession.setObjectName(u"ln_sumiprofession")
        self.ln_sumiprofession.setStyleSheet(u"color:white;\n"
"font-size:14pt;\n"
"")
        self.splitter_5.addWidget(self.ln_sumiprofession)
        self.btn_profession2 = QPushButton(self.splitter_5)
        self.btn_profession2.setObjectName(u"btn_profession2")
        self.btn_profession2.setStyleSheet(u"QPushButton {\n"
"color: white;\n"
"background-color: rgba(89,89, 89, 100);\n"
"border-radius: 4 px;\n"
"border-color: rgb(127, 152, 110);\n"
"text-align: center;\n"
"width: 260px;\n"
"height: 50px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgba(127,152, 127, 100);\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgba(255, 255, 255, 70);\n"
"}\n"
"")
        self.splitter_5.addWidget(self.btn_profession2)

        self.verticalLayout.addWidget(self.splitter_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(-1, -1, -1, 50)
        self.lb_sumi_startworked = QLabel(self.widget)
        self.lb_sumi_startworked.setObjectName(u"lb_sumi_startworked")
        self.lb_sumi_startworked.setMinimumSize(QSize(60, 0))
        self.lb_sumi_startworked.setStyleSheet(u"color:white;\n"
"font-size:14pt;\n"
";\n"
"")

        self.horizontalLayout_6.addWidget(self.lb_sumi_startworked)

        self.ln_sumi_startworked = QLineEdit(self.widget)
        self.ln_sumi_startworked.setObjectName(u"ln_sumi_startworked")
        self.ln_sumi_startworked.setStyleSheet(u"color:white;\n"
"font-size:14pt;\n"
"")

        self.horizontalLayout_6.addWidget(self.ln_sumi_startworked)


        self.verticalLayout.addLayout(self.horizontalLayout_6)

        self.btn_new_card = QPushButton(self.widget)
        self.btn_new_card.setObjectName(u"btn_new_card")
        self.btn_new_card.setStyleSheet(u"QPushButton {\n"
"color: white;\n"
"background-color: rgba(89,89, 89, 100);\n"
"border-radius: 4 px;\n"
"border-color: rgb(127, 152, 110);\n"
"text-align: center;\n"
"width: 260px;\n"
"height: 50px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgba(127,152, 127, 100);\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgba(255, 255, 255, 70);\n"
"}\n"
"")

        self.verticalLayout.addWidget(self.btn_new_card)

        self.btn_edit_card = QPushButton(self.widget)
        self.btn_edit_card.setObjectName(u"btn_edit_card")
        self.btn_edit_card.setStyleSheet(u"QPushButton {\n"
"color: white;\n"
"background-color: rgba(89,89, 89, 100);\n"
"border-radius: 4 px;\n"
"border-color: rgb(127, 152, 110);\n"
"text-align: center;\n"
"width: 260px;\n"
"height: 50px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgba(127,152, 127, 100);\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgba(255, 255, 255, 70);\n"
"}\n"
"")

        self.verticalLayout.addWidget(self.btn_edit_card)

        self.btn_delete_card = QPushButton(self.widget)
        self.btn_delete_card.setObjectName(u"btn_delete_card")
        self.btn_delete_card.setStyleSheet(u"QPushButton {\n"
"color: white;\n"
"background-color: rgba(89,89, 89, 100);\n"
"border-radius: 4 px;\n"
"border-color: rgb(127, 152, 110);\n"
"text-align: center;\n"
"width: 260px;\n"
"height: 50px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgba(127,152, 127, 100);\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgba(255, 255, 255, 70);\n"
"}\n"
"")

        self.verticalLayout.addWidget(self.btn_delete_card)

        self.btn_edit_2 = QPushButton(self.widget)
        self.btn_edit_2.setObjectName(u"btn_edit_2")
        self.btn_edit_2.setStyleSheet(u"QPushButton {\n"
"color: white;\n"
"background-color: rgba(89,89, 89, 100);\n"
"border-radius: 4 px;\n"
"border-color: rgb(127, 152, 110);\n"
"text-align: center;\n"
"width: 260px;\n"
"height: 50px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgba(127,152, 127, 100);\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgba(255, 255, 255, 70);\n"
"}\n"
"")

        self.verticalLayout.addWidget(self.btn_edit_2)


        self.retranslateUi(PersonalCard)

        QMetaObject.connectSlotsByName(PersonalCard)
    # setupUi

    def retranslateUi(self, PersonalCard):
        PersonalCard.setWindowTitle(QCoreApplication.translate("PersonalCard", u"Form", None))
        self.label.setText(QCoreApplication.translate("PersonalCard", u"\u041e\u0441\u043e\u0431\u0438\u0441\u0442\u0430 \u043a\u0430\u0440\u0442\u043a\u0430 \u043f\u0440\u0430\u0446\u0456\u0432\u043d\u0438\u043a\u0430", None))
        self.lb_surname_employee.setText(QCoreApplication.translate("PersonalCard", u"\u041f\u0440\u0456\u0437\u0432\u0438\u0449\u0435", None))
        self.lbname_employee.setText(QCoreApplication.translate("PersonalCard", u"\u0406'\u043c\u044f", None))
        self.lb_paronymic_employee.setText(QCoreApplication.translate("PersonalCard", u"\u041f\u043e \u0431\u0430\u0442\u044c\u043a\u043e\u0432\u0456", None))
        self.lb_sex.setText(QCoreApplication.translate("PersonalCard", u"\u041f\u043e\u043b", None))
        self.cb_sex.setItemText(0, QCoreApplication.translate("PersonalCard", u"\u0427\u043e\u043b\u043e\u0432\u0456\u043a", None))
        self.cb_sex.setItemText(1, QCoreApplication.translate("PersonalCard", u"\u0416\u0456\u043d\u043a\u0430", None))

        self.lb_family.setText(QCoreApplication.translate("PersonalCard", u"\u0421\u0456\u043c\u0435\u0439\u043d\u0438\u0439 \u0441\u0442\u0430\u043d", None))
        self.cb_family.setItemText(0, QCoreApplication.translate("PersonalCard", u"\u041e\u0434\u0440\u0443\u0436\u0435\u043d\u0438\u0439", None))
        self.cb_family.setItemText(1, QCoreApplication.translate("PersonalCard", u"\u041d\u0435\u043e\u0434\u0440\u0443\u0436\u0435\u043d\u0438\u0439", None))
        self.cb_family.setItemText(2, QCoreApplication.translate("PersonalCard", u"\u0417\u0430\u043c\u0456\u0436\u043d\u044f", None))
        self.cb_family.setItemText(3, QCoreApplication.translate("PersonalCard", u"\u0435\u0437\u0430\u043c\u0456\u0436\u043d\u0433\u044f", None))

        self.lb_birthdate.setText(QCoreApplication.translate("PersonalCard", u"\u0414\u0430\u0442\u0430 \u043d\u0430\u0440\u043e\u0434\u0436\u0435\u043d\u043d\u044f", None))
        self.lb_department.setText(QCoreApplication.translate("PersonalCard", u"\u0421\u0442\u0440\u0443\u043a\u0442\u0443\u0440\u043d\u0438\u0439 \u043f\u0456\u0434\u0440\u043e\u0437\u0434\u0456\u043b", None))
        self.cb_department.setItemText(0, QCoreApplication.translate("PersonalCard", u"\u0410\u0434\u043c\u0456\u043d\u0456\u0441\u0442\u0440\u0430\u0446\u0456\u044f", None))
        self.cb_department.setItemText(1, QCoreApplication.translate("PersonalCard", u"\u0411\u0443\u0445\u0433\u0430\u043b\u0442\u0435\u0440\u0441\u044c\u043a\u0456\u0439 \u0432\u0456\u0434\u0434\u0456\u043b", None))
        self.cb_department.setItemText(2, QCoreApplication.translate("PersonalCard", u"\u0426\u0435\u0445 1", None))

        self.llb_category.setText(QCoreApplication.translate("PersonalCard", u"\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0456\u044f \u043f\u0435\u0440\u0441\u043e\u043d\u0430\u043b\u0443", None))
        self.cb_category.setItemText(0, QCoreApplication.translate("PersonalCard", u"\u041a\u0435\u0440\u0456\u0432\u043d\u0438\u043a", None))
        self.cb_category.setItemText(1, QCoreApplication.translate("PersonalCard", u"\u0424\u0430\u0445\u0456\u0432\u0435\u0446\u044c", None))
        self.cb_category.setItemText(2, QCoreApplication.translate("PersonalCard", u"\u0420\u043e\u0431\u0456\u0442\u043d\u0438\u043a", None))

        self.lb_profesion.setText(QCoreApplication.translate("PersonalCard", u"\u041f\u043e\u0441\u0430\u0434\u0430", None))
        self.btn_professions.setText(QCoreApplication.translate("PersonalCard", u"\u0414\u043e\u0432\u0456\u0434\u043d\u0438\u043a \u043f\u0440\u043e\u0444\u0435\u0441\u0456\u0439", None))
        self.lb_start_worked.setText(QCoreApplication.translate("PersonalCard", u"\u0414\u0430\u0442\u0430 \u043f\u0440\u0438\u0439\u043e\u043c\u0443 \u043d\u0430 \u0440\u043e\u0431\u043e\u0442\u0443", None))
        self.lb_sumi.setText(QCoreApplication.translate("PersonalCard", u"\u041f\u043e\u0441\u0430\u0434\u0430 \u0437\u0430 \u0441\u0443\u043c\u0456\u0449\u0435\u043d\u043d\u044f\u043c", None))
        self.btn_profession2.setText(QCoreApplication.translate("PersonalCard", u"\u0414\u043e\u0432\u0456\u0434\u043d\u0438\u043a \u043f\u0440\u043e\u0444\u0435\u0441\u0456\u0439", None))
        self.lb_sumi_startworked.setText(QCoreApplication.translate("PersonalCard", u"\u0414\u0430\u0442\u0430 \u043f\u043e\u0447\u0430\u0442\u043a\u0443 \u0440\u043e\u0431\u043e\u0442\u0438 \u0437\u0430 \u0441\u0443\u043c\u0456\u0449\u0435\u043d\u043d\u044f\u043c", None))
        self.btn_new_card.setText(QCoreApplication.translate("PersonalCard", u"\u0414\u043e\u0434\u0430\u0442\u0438 \u043d\u043e\u0432\u0443 \u043a\u0430\u0440\u0442\u043a\u0443", None))
        self.btn_edit_card.setText(QCoreApplication.translate("PersonalCard", u"\u0420\u0435\u0434\u0430\u0433\u0443\u0432\u0430\u0442\u0438 \u043a\u0430\u0440\u0442\u043a\u0443", None))
        self.btn_delete_card.setText(QCoreApplication.translate("PersonalCard", u"\u0412\u0438\u0434\u0430\u043b\u0438\u0442\u0438 \u043a\u0430\u0440\u0442\u043a\u0443", None))
        self.btn_edit_2.setText(QCoreApplication.translate("PersonalCard", u"\u0412\u0438\u0434\u0430\u043b\u0438\u0442\u0438 \u0432\u0456\u0434\u043e\u043c\u043e\u0441\u0442\u0456", None))
    # retranslateUi

