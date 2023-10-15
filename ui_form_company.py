# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_form_company.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLineEdit,
    QPlainTextEdit, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_staff_form(object):
    def setupUi(self, staff_form):
        if not staff_form.objectName():
            staff_form.setObjectName(u"staff_form")
        staff_form.resize(744, 609)
        staff_form.setStyleSheet(u"background-color: rgba(25, 25, 25, 255);\n"
"font-family: Roboto;")
        self.layoutWidget = QWidget(staff_form)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 20, 721, 571))
        self.verticalLayout_2 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.lb_company_info_f = QLabel(self.layoutWidget)
        self.lb_company_info_f.setObjectName(u"lb_company_info_f")
        self.lb_company_info_f.setStyleSheet(u"color:white;")

        self.horizontalLayout_6.addWidget(self.lb_company_info_f)

        self.btn_structure_f = QPushButton(self.layoutWidget)
        self.btn_structure_f.setObjectName(u"btn_structure_f")
        self.btn_structure_f.setStyleSheet(u"QPushButton {\n"
"color: white;\n"
"background-color: rgba(9, 9, 9, 100);\n"
"text-align:center;\n"
"width: 260px;\n"
"height: 50px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgba(255,85, 127, 100);\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgba(255, 255, 255, 70);\n"
"}\n"
"")

        self.horizontalLayout_6.addWidget(self.btn_structure_f)

        self.btn_profession_f = QPushButton(self.layoutWidget)
        self.btn_profession_f.setObjectName(u"btn_profession_f")
        self.btn_profession_f.setMinimumSize(QSize(0, 0))
        self.btn_profession_f.setStyleSheet(u"QPushButton {\n"
"color: white;\n"
"background-color: rgba(9, 9, 9, 100);\n"
"text-align: center;\n"
"width: 260px;\n"
"height: 50px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgba(255,85, 127, 100);\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgba(255, 255, 255, 70);\n"
"}\n"
"")

        self.horizontalLayout_6.addWidget(self.btn_profession_f)

        self.btn_employeis_f_2 = QPushButton(self.layoutWidget)
        self.btn_employeis_f_2.setObjectName(u"btn_employeis_f_2")
        self.btn_employeis_f_2.setStyleSheet(u"QPushButton {\n"
"color: white;\n"
"background-color: rgba(9, 9, 9, 100);\n"
"text-align:center;\n"
"width: 260px;\n"
"height: 50px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgba(255,85, 127, 100);\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgba(255, 255, 255, 70);\n"
"}\n"
"")

        self.horizontalLayout_6.addWidget(self.btn_employeis_f_2)


        self.verticalLayout_2.addLayout(self.horizontalLayout_6)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_title = QHBoxLayout()
        self.horizontalLayout_title.setSpacing(40)
        self.horizontalLayout_title.setObjectName(u"horizontalLayout_title")
        self.horizontalLayout_title.setContentsMargins(20, -1, -1, 20)
        self.lb_company_title_f = QLabel(self.layoutWidget)
        self.lb_company_title_f.setObjectName(u"lb_company_title_f")
        self.lb_company_title_f.setStyleSheet(u"color:white;")

        self.horizontalLayout_title.addWidget(self.lb_company_title_f)

        self.pl_company_title = QPlainTextEdit(self.layoutWidget)
        self.pl_company_title.setObjectName(u"pl_company_title")
        self.pl_company_title.setMinimumSize(QSize(0, 24))
        self.pl_company_title.setMaximumSize(QSize(16777215, 56))
        self.pl_company_title.setStyleSheet(u"color: white;")

        self.horizontalLayout_title.addWidget(self.pl_company_title)


        self.verticalLayout.addLayout(self.horizontalLayout_title)

        self.horizontalLayout_adress = QHBoxLayout()
        self.horizontalLayout_adress.setSpacing(20)
        self.horizontalLayout_adress.setObjectName(u"horizontalLayout_adress")
        self.horizontalLayout_adress.setContentsMargins(20, -1, -1, -1)
        self.lb_company_adress_f = QLabel(self.layoutWidget)
        self.lb_company_adress_f.setObjectName(u"lb_company_adress_f")
        self.lb_company_adress_f.setStyleSheet(u"color:white;")

        self.horizontalLayout_adress.addWidget(self.lb_company_adress_f)

        self.pl_company_adress_f = QPlainTextEdit(self.layoutWidget)
        self.pl_company_adress_f.setObjectName(u"pl_company_adress_f")
        self.pl_company_adress_f.setMaximumSize(QSize(16777215, 56))
        self.pl_company_adress_f.setStyleSheet(u"color: white;")

        self.horizontalLayout_adress.addWidget(self.pl_company_adress_f)


        self.verticalLayout.addLayout(self.horizontalLayout_adress)

        self.horizontalLayout_num = QHBoxLayout()
        self.horizontalLayout_num.setSpacing(15)
        self.horizontalLayout_num.setObjectName(u"horizontalLayout_num")
        self.horizontalLayout_num.setContentsMargins(20, 20, 550, 20)
        self.lb_company_num_f = QLabel(self.layoutWidget)
        self.lb_company_num_f.setObjectName(u"lb_company_num_f")
        self.lb_company_num_f.setStyleSheet(u"color:white;")

        self.horizontalLayout_num.addWidget(self.lb_company_num_f)

        self.ln_company_num_f = QLineEdit(self.layoutWidget)
        self.ln_company_num_f.setObjectName(u"ln_company_num_f")
        self.ln_company_num_f.setStyleSheet(u"color: white;")

        self.horizontalLayout_num.addWidget(self.ln_company_num_f)


        self.verticalLayout.addLayout(self.horizontalLayout_num)

        self.horizontalLayout_director = QHBoxLayout()
        self.horizontalLayout_director.setSpacing(14)
        self.horizontalLayout_director.setObjectName(u"horizontalLayout_director")
        self.horizontalLayout_director.setContentsMargins(20, 20, 150, 20)
        self.lab_company_director_f = QLabel(self.layoutWidget)
        self.lab_company_director_f.setObjectName(u"lab_company_director_f")
        self.lab_company_director_f.setStyleSheet(u"color:white;")

        self.horizontalLayout_director.addWidget(self.lab_company_director_f)

        self.ln_company_director_f = QLineEdit(self.layoutWidget)
        self.ln_company_director_f.setObjectName(u"ln_company_director_f")
        self.ln_company_director_f.setStyleSheet(u"color: white;")

        self.horizontalLayout_director.addWidget(self.ln_company_director_f)


        self.verticalLayout.addLayout(self.horizontalLayout_director)

        self.horizontalLayout_tel = QHBoxLayout()
        self.horizontalLayout_tel.setSpacing(18)
        self.horizontalLayout_tel.setObjectName(u"horizontalLayout_tel")
        self.horizontalLayout_tel.setContentsMargins(20, 20, 450, 20)
        self.lb_company_tel_f = QLabel(self.layoutWidget)
        self.lb_company_tel_f.setObjectName(u"lb_company_tel_f")
        self.lb_company_tel_f.setStyleSheet(u"color:white;")

        self.horizontalLayout_tel.addWidget(self.lb_company_tel_f)

        self.ln_company_tel_f = QLineEdit(self.layoutWidget)
        self.ln_company_tel_f.setObjectName(u"ln_company_tel_f")
        self.ln_company_tel_f.setStyleSheet(u"color: white;")

        self.horizontalLayout_tel.addWidget(self.ln_company_tel_f)


        self.verticalLayout.addLayout(self.horizontalLayout_tel)

        self.horizontalLayout_mail = QHBoxLayout()
        self.horizontalLayout_mail.setSpacing(14)
        self.horizontalLayout_mail.setObjectName(u"horizontalLayout_mail")
        self.horizontalLayout_mail.setContentsMargins(20, 20, 250, 20)
        self.lb_company_mail_f = QLabel(self.layoutWidget)
        self.lb_company_mail_f.setObjectName(u"lb_company_mail_f")
        self.lb_company_mail_f.setStyleSheet(u"color:white;")

        self.horizontalLayout_mail.addWidget(self.lb_company_mail_f)

        self.ln_company_mail_f = QLineEdit(self.layoutWidget)
        self.ln_company_mail_f.setObjectName(u"ln_company_mail_f")
        self.ln_company_mail_f.setStyleSheet(u"color: white;")

        self.horizontalLayout_mail.addWidget(self.ln_company_mail_f)


        self.verticalLayout.addLayout(self.horizontalLayout_mail)


        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.retranslateUi(staff_form)

        QMetaObject.connectSlotsByName(staff_form)
    # setupUi

    def retranslateUi(self, staff_form):
        staff_form.setWindowTitle(QCoreApplication.translate("staff_form", u"Form", None))
        self.lb_company_info_f.setText(QCoreApplication.translate("staff_form", u"\u0412\u0456\u0434\u043e\u043c\u043e\u0441\u0442\u0456 \u043f\u0440\u043e \u043f\u0456\u0434\u043f\u0440\u0438\u0454\u043c\u0441\u0442\u0432\u043e", None))
        self.btn_structure_f.setText(QCoreApplication.translate("staff_form", u"\u0421\u0442\u0440\u0443\u043a\u0442\u0443\u0440\u043d\u0456 \u043f\u0456\u0434\u0440\u043e\u0437\u0434\u0456\u043b\u0438", None))
        self.btn_profession_f.setText(QCoreApplication.translate("staff_form", u"\u041f\u0440\u043e\u0444\u0435\u0441\u0456\u0457 \u0442\u0430 \u043f\u043e\u0441\u0430\u0434\u0438", None))
        self.btn_employeis_f_2.setText(QCoreApplication.translate("staff_form", u"\u041f\u0440\u0430\u0446\u0456\u0432\u043d\u0438\u043a\u0438", None))
        self.lb_company_title_f.setText(QCoreApplication.translate("staff_form", u"\u041d\u0430\u0439\u043c\u0435\u043d\u0443\u0432\u0430\u043d\u043d\u044f", None))
        self.lb_company_adress_f.setText(QCoreApplication.translate("staff_form", u"\u0410\u0434\u0440\u0435\u0441\u0430", None))
        self.lb_company_num_f.setText(QCoreApplication.translate("staff_form", u"\u0404\u0414\u0420\u041f\u041e\u0423", None))
        self.lab_company_director_f.setText(QCoreApplication.translate("staff_form", u"\u041a\u0435\u0440\u0456\u0432\u043d\u0438\u043a", None))
        self.lb_company_tel_f.setText(QCoreApplication.translate("staff_form", u"\u0422\u0435\u043b\u0435\u0444\u043e\u043d", None))
        self.lb_company_mail_f.setText(QCoreApplication.translate("staff_form", u"\u0415\u043b\u0435\u043a\u0442\u0440\u043e\u043d\u043d\u0430 \u043f\u043e\u0448\u0442\u0430", None))
    # retranslateUi

