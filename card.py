# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_card.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QHeaderView, QLabel,
    QPushButton, QSizePolicy, QTableWidget, QTableWidgetItem,
    QWidget)

class Ui_Form_Employee(object):
    def setupUi(self, Form_Employee):
        if not Form_Employee.objectName():
            Form_Employee.setObjectName(u"Form_Employee")
        Form_Employee.resize(934, 684)
        Form_Employee.setMinimumSize(QSize(0, 50))
        Form_Employee.setStyleSheet(u"background-color: rgba(25, 25, 25, 255);\n"
"font-family: Roboto;\n"
"color:white;")
        self.btn_cart = QPushButton(Form_Employee)
        self.btn_cart.setObjectName(u"btn_cart")
        self.btn_cart.setGeometry(QRect(20, 540, 191, 41))
        self.btn_cart.setStyleSheet(u"QPushButton {\n"
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
        self.label = QLabel(Form_Employee)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 10, 201, 51))
        font = QFont()
        font.setFamilies([u"Roboto"])
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setStyleSheet(u"")
        self.tableWidget_employee = QTableWidget(Form_Employee)
        self.tableWidget_employee.setObjectName(u"tableWidget_employee")
        self.tableWidget_employee.setGeometry(QRect(30, 170, 871, 331))
        self.tableWidget_employee.setStyleSheet(u"QTableView {\n"
"color: white;\n"
"background-color: rgba(9,9, 9, 100);\n"
"}\n"
"QTableView:section {\n"
"background-color: rgba(127,152, 127, 100);\n"
"color: white;\n"
"height: 50px;\n"
"font-size: 14pt;\n"
"}\n"
"QTableView:item {\n"
"border-stile:none;\n"
"border_bottom:rgba(255, 255, 255, 70);\n"
"}\n"
"QTableView:item:selected {\n"
"border-stile:none;\n"
"border_bottom:rgba(255, 255, 255, 70);\n"
"background-color: rgba(127,152, 127, 50)\n"
"}")
        self.tableWidget_employee.setShowGrid(False)
        self.btn_test = QPushButton(Form_Employee)
        self.btn_test.setObjectName(u"btn_test")
        self.btn_test.setGeometry(QRect(240, 540, 191, 41))
        self.btn_test.setStyleSheet(u"QPushButton {\n"
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
        self.btn_add_cart = QPushButton(Form_Employee)
        self.btn_add_cart.setObjectName(u"btn_add_cart")
        self.btn_add_cart.setGeometry(QRect(20, 610, 191, 41))
        self.btn_add_cart.setStyleSheet(u"QPushButton {\n"
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
        self.btn_intruction = QPushButton(Form_Employee)
        self.btn_intruction.setObjectName(u"btn_intruction")
        self.btn_intruction.setGeometry(QRect(470, 540, 191, 41))
        self.btn_intruction.setStyleSheet(u"QPushButton {\n"
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
        self.btn_stag = QPushButton(Form_Employee)
        self.btn_stag.setObjectName(u"btn_stag")
        self.btn_stag.setGeometry(QRect(240, 610, 191, 41))
        self.btn_stag.setStyleSheet(u"QPushButton {\n"
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
        self.btn_med = QPushButton(Form_Employee)
        self.btn_med.setObjectName(u"btn_med")
        self.btn_med.setGeometry(QRect(470, 610, 191, 41))
        self.btn_med.setStyleSheet(u"QPushButton {\n"
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
        self.btn_print_sort = QPushButton(Form_Employee)
        self.btn_print_sort.setObjectName(u"btn_print_sort")
        self.btn_print_sort.setGeometry(QRect(700, 540, 191, 41))
        self.btn_print_sort.setStyleSheet(u"QPushButton {\n"
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
        self.btn_quit_cart = QPushButton(Form_Employee)
        self.btn_quit_cart.setObjectName(u"btn_quit_cart")
        self.btn_quit_cart.setGeometry(QRect(700, 610, 191, 41))
        self.btn_quit_cart.setStyleSheet(u"QPushButton {\n"
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
        self.layoutWidget = QWidget(Form_Employee)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(310, 40, 601, 71))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setSpacing(41)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(20, 20, 20, 0)
        self.btn_sort_department = QPushButton(self.layoutWidget)
        self.btn_sort_department.setObjectName(u"btn_sort_department")
        self.btn_sort_department.setStyleSheet(u"QPushButton {\n"
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
"\n"
"")

        self.horizontalLayout.addWidget(self.btn_sort_department)

        self.btn_sort_profession = QPushButton(self.layoutWidget)
        self.btn_sort_profession.setObjectName(u"btn_sort_profession")
        self.btn_sort_profession.setStyleSheet(u"QPushButton {\n"
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

        self.horizontalLayout.addWidget(self.btn_sort_profession)


        self.retranslateUi(Form_Employee)

        QMetaObject.connectSlotsByName(Form_Employee)
    # setupUi

    def retranslateUi(self, Form_Employee):
        Form_Employee.setWindowTitle(QCoreApplication.translate("Form_Employee", u"Form", None))
        self.btn_cart.setText(QCoreApplication.translate("Form_Employee", u"\u041e\u0441\u043e\u0431\u0438\u0441\u0442\u0430 \u043a\u0430\u0440\u0442\u043a\u0430", None))
        self.label.setText(QCoreApplication.translate("Form_Employee", u"\u041a\u0430\u0440\u0442\u043e\u0442\u0435\u043a\u0430 \u043f\u0435\u0440\u0441\u043e\u043d\u0430\u043b\u0443", None))
        self.btn_test.setText(QCoreApplication.translate("Form_Employee", u"\u041f\u0435\u0440\u0435\u0432\u0456\u0440\u043a\u0430 \u0437\u043d\u0430\u043d\u044c", None))
        self.btn_add_cart.setText(QCoreApplication.translate("Form_Employee", u"\u0414\u043e\u0434\u0430\u0442\u0438 \u043a\u0430\u0440\u0442\u043a\u0443", None))
        self.btn_intruction.setText(QCoreApplication.translate("Form_Employee", u"\u0406\u043d\u0441\u0442\u0440\u0443\u043a\u0442\u0430\u0436\u0456", None))
        self.btn_stag.setText(QCoreApplication.translate("Form_Employee", u"\u0421\u0442\u0430\u0436\u0443\u0432\u0430\u043d\u043d\u044f", None))
        self.btn_med.setText(QCoreApplication.translate("Form_Employee", u"\u041c\u0435\u0434\u0438\u0447\u043d\u0456 \u043e\u0433\u043b\u044f\u0434\u0438", None))
        self.btn_print_sort.setText(QCoreApplication.translate("Form_Employee", u"\u0414\u0440\u0443\u043a", None))
        self.btn_quit_cart.setText(QCoreApplication.translate("Form_Employee", u"\u0412\u0438\u0445\u0456\u0434", None))
        self.btn_sort_department.setText(QCoreApplication.translate("Form_Employee", u"\u0421\u043e\u0440\u0442\u0443\u0432\u0430\u043d\u043d\u044f \u0437\u0430 \u043f\u0456\u0434\u0440\u043e\u0437\u0434\u0456\u043b\u0430\u043c\u0438", None))
        self.btn_sort_profession.setText(QCoreApplication.translate("Form_Employee", u"\u0421\u043e\u0440\u0442\u0443\u0432\u0430\u043d\u043d\u044f \u0437\u0430 \u043f\u043e\u0441\u0430\u0434\u043e\u044e", None))
    # retranslateUi

