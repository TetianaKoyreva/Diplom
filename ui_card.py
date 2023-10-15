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
    QVBoxLayout, QWidget)
import res-rc_rc

class Ui_Form_Employee(object):
    def setupUi(self, Form_Employee):
        if not Form_Employee.objectName():
            Form_Employee.setObjectName(u"Form_Employee")
        Form_Employee.resize(1063, 680)
        Form_Employee.setMinimumSize(QSize(0, 50))
        Form_Employee.setStyleSheet(u"background-color: rgba(25, 25, 25, 255);\n"
"font-family: Roboto;\n"
"color:white;")
        self.label_employee = QLabel(Form_Employee)
        self.label_employee.setObjectName(u"label_employee")
        self.label_employee.setGeometry(QRect(150, 20, 204, 51))
        font = QFont()
        font.setFamilies([u"Roboto"])
        font.setPointSize(12)
        self.label_employee.setFont(font)
        self.label_employee.setStyleSheet(u"")
        self.tableWidget_employee = QTableWidget(Form_Employee)
        self.tableWidget_employee.setObjectName(u"tableWidget_employee")
        self.tableWidget_employee.setGeometry(QRect(150, 160, 871, 331))
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
        self.btn_testinformation = QPushButton(Form_Employee)
        self.btn_testinformation.setObjectName(u"btn_testinformation")
        self.btn_testinformation.setGeometry(QRect(320, 540, 241, 41))
        self.btn_testinformation.setFont(font)
        self.btn_testinformation.setStyleSheet(u"QPushButton {\n"
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
        self.btn_add_cart.setGeometry(QRect(110, 610, 191, 41))
        self.btn_add_cart.setFont(font)
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
        self.btn_intruction.setGeometry(QRect(580, 540, 191, 41))
        self.btn_intruction.setFont(font)
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
        self.btn_stag.setGeometry(QRect(790, 540, 191, 41))
        self.btn_stag.setFont(font)
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
        self.btn_print_sort = QPushButton(Form_Employee)
        self.btn_print_sort.setObjectName(u"btn_print_sort")
        self.btn_print_sort.setGeometry(QRect(580, 610, 191, 41))
        self.btn_print_sort.setFont(font)
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
        self.btn_quit_cart.setGeometry(QRect(790, 610, 191, 41))
        self.btn_quit_cart.setFont(font)
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
        self.layoutWidget.setGeometry(QRect(460, 40, 602, 71))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setSpacing(41)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(20, 20, 20, 0)
        self.btn_sort_department = QPushButton(self.layoutWidget)
        self.btn_sort_department.setObjectName(u"btn_sort_department")
        self.btn_sort_department.setFont(font)
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
        self.btn_sort_profession.setFont(font)
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

        self.widget = QWidget(Form_Employee)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(20, 20, 41, 341))
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.btn_staff = QPushButton(self.widget)
        self.btn_staff.setObjectName(u"btn_staff")
        self.btn_staff.setMinimumSize(QSize(32, 32))
        font1 = QFont()
        font1.setFamilies([u"Roboto"])
        font1.setKerning(True)
        self.btn_staff.setFont(font1)
        self.btn_staff.setStyleSheet(u"QPushButton {\n"
"color: white;\n"
"background-color: rgba(9, 9, 9, 100);\n"
"text-align: left;\n"
"width: 260px;\n"
"height: 50px;\n"
"text-align: center;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: rgba(255,85, 127, 100);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: rgba(255, 255, 255, 70);\n"
"}")
        icon = QIcon()
        icon.addFile(u":/icon/icons/recent_actors_white_24dp.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_staff.setIcon(icon)
        self.btn_staff.setIconSize(QSize(32, 32))
        self.btn_staff.setFlat(False)

        self.verticalLayout.addWidget(self.btn_staff)

        self.btn_studydoc = QPushButton(self.widget)
        self.btn_studydoc.setObjectName(u"btn_studydoc")
        self.btn_studydoc.setMinimumSize(QSize(32, 32))
        self.btn_studydoc.setStyleSheet(u"QPushButton {\n"
"color: white;\n"
"background-color: rgba(9, 9, 9, 100);\n"
"text-align: left;\n"
"width: 260px;\n"
"height: 50px;\n"
"text-align: center;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: rgba(255,85, 127, 100);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: rgba(255, 255, 255, 70);\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/icon/icons/text_snippet_white_24dp.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_studydoc.setIcon(icon1)
        self.btn_studydoc.setIconSize(QSize(32, 32))
        self.btn_studydoc.setFlat(False)

        self.verticalLayout.addWidget(self.btn_studydoc)

        self.btn_group = QPushButton(self.widget)
        self.btn_group.setObjectName(u"btn_group")
        self.btn_group.setMinimumSize(QSize(32, 32))
        self.btn_group.setStyleSheet(u"QPushButton {\n"
"color: white;\n"
"background-color: rgba(9, 9, 9, 100);\n"
"text-align: left;\n"
"width: 260px;\n"
"height: 50px;\n"
"text-align: center;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: rgba(255,85, 127, 100);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: rgba(255, 255, 255, 70);\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/icon/icons/groups_white_24dp.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_group.setIcon(icon2)
        self.btn_group.setIconSize(QSize(32, 32))

        self.verticalLayout.addWidget(self.btn_group)

        self.btn_book = QPushButton(self.widget)
        self.btn_book.setObjectName(u"btn_book")
        self.btn_book.setMinimumSize(QSize(32, 32))
        self.btn_book.setStyleSheet(u"QPushButton {\n"
"color: white;\n"
"background-color: rgba(9, 9, 9, 100);\n"
"text-align: left;\n"
"width: 260px;\n"
"height: 50px;\n"
"text-align: center;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: rgba(255,85, 127, 100);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: rgba(255, 255, 255, 70);\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u":/icon/icons/menu_book_white_24dp.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_book.setIcon(icon3)
        self.btn_book.setIconSize(QSize(32, 32))

        self.verticalLayout.addWidget(self.btn_book)

        self.btn_test = QPushButton(self.widget)
        self.btn_test.setObjectName(u"btn_test")
        self.btn_test.setMinimumSize(QSize(32, 32))
        self.btn_test.setStyleSheet(u"QPushButton {\n"
"color: white;\n"
"background-color: rgba(9, 9, 9, 100);\n"
"text-align: left;\n"
"width: 260px;\n"
"height: 50px;\n"
"text-align: center;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: rgba(255,85, 127, 100);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: rgba(255, 255, 255, 70);\n"
"}")
        icon4 = QIcon()
        icon4.addFile(u":/icon/icons/fact_check_white_24dp.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_test.setIcon(icon4)
        self.btn_test.setIconSize(QSize(32, 32))

        self.verticalLayout.addWidget(self.btn_test)

        self.btn_analys = QPushButton(self.widget)
        self.btn_analys.setObjectName(u"btn_analys")
        self.btn_analys.setMinimumSize(QSize(32, 32))
        self.btn_analys.setStyleSheet(u"QPushButton {\n"
"color: white;\n"
"background-color: rgba(9, 9, 9, 100);\n"
"text-align: left;\n"
"width: 260px;\n"
"height: 50px;\n"
"text-align: center;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: rgba(255,85, 127, 100);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: rgba(255, 255, 255, 70);\n"
"}")
        icon5 = QIcon()
        icon5.addFile(u":/icon/icons/analitics_white_24dp.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_analys.setIcon(icon5)
        self.btn_analys.setIconSize(QSize(32, 32))

        self.verticalLayout.addWidget(self.btn_analys)

        self.btn_cart = QPushButton(Form_Employee)
        self.btn_cart.setObjectName(u"btn_cart")
        self.btn_cart.setGeometry(QRect(110, 540, 191, 41))
        self.btn_cart.setFont(font)
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

        self.retranslateUi(Form_Employee)

        self.btn_staff.setDefault(True)


        QMetaObject.connectSlotsByName(Form_Employee)
    # setupUi

    def retranslateUi(self, Form_Employee):
        Form_Employee.setWindowTitle(QCoreApplication.translate("Form_Employee", u"Form", None))
        self.label_employee.setText(QCoreApplication.translate("Form_Employee", u"\u041a\u0430\u0440\u0442\u043e\u0442\u0435\u043a\u0430 \u043f\u0435\u0440\u0441\u043e\u043d\u0430\u043b\u0443", None))
        self.btn_testinformation.setText(QCoreApplication.translate("Form_Employee", u"\u0412\u0456\u0434\u043e\u043c\u043e\u0441\u0442\u0456 \u043f\u0440\u043e \u043f\u0435\u0440\u0435\u0432\u0456\u0440\u043a\u0443 \u0437\u043d\u0430\u043d\u044c", None))
        self.btn_add_cart.setText(QCoreApplication.translate("Form_Employee", u"\u0414\u043e\u0434\u0430\u0442\u0438 \u043a\u0430\u0440\u0442\u043a\u0443", None))
        self.btn_intruction.setText(QCoreApplication.translate("Form_Employee", u"\u0406\u043d\u0441\u0442\u0440\u0443\u043a\u0442\u0430\u0436\u0456", None))
        self.btn_stag.setText(QCoreApplication.translate("Form_Employee", u"\u0421\u0442\u0430\u0436\u0443\u0432\u0430\u043d\u043d\u044f", None))
        self.btn_print_sort.setText(QCoreApplication.translate("Form_Employee", u"\u0414\u0440\u0443\u043a", None))
        self.btn_quit_cart.setText(QCoreApplication.translate("Form_Employee", u"\u0412\u0438\u0445\u0456\u0434", None))
        self.btn_sort_department.setText(QCoreApplication.translate("Form_Employee", u"\u0421\u043e\u0440\u0442\u0443\u0432\u0430\u043d\u043d\u044f \u0437\u0430 \u043f\u0456\u0434\u0440\u043e\u0437\u0434\u0456\u043b\u0430\u043c\u0438", None))
        self.btn_sort_profession.setText(QCoreApplication.translate("Form_Employee", u"\u0421\u043e\u0440\u0442\u0443\u0432\u0430\u043d\u043d\u044f \u0437\u0430 \u043f\u043e\u0441\u0430\u0434\u043e\u044e", None))
        self.btn_staff.setText("")
        self.btn_studydoc.setText("")
        self.btn_group.setText("")
        self.btn_book.setText("")
        self.btn_test.setText("")
        self.btn_analys.setText("")
        self.btn_cart.setText(QCoreApplication.translate("Form_Employee", u"\u041e\u0441\u043e\u0431\u0438\u0441\u0442\u0430 \u043a\u0430\u0440\u0442\u043a\u0430", None))
    # retranslateUi

