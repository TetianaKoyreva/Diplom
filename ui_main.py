# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_main.ui'
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
from PySide6.QtWidgets import (QApplication, QMainWindow, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)
import res_rc
#import res_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(801, 694)
        MainWindow.setStyleSheet(u"background-color: rgba(25, 25, 25, 255);\n"
"font-family: Roboto;\n"
"color:white;")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.btn_staff = QPushButton(self.centralwidget)
        self.btn_staff.setObjectName(u"btn_staff")
        self.btn_staff.setMaximumSize(QSize(16777215, 48))
        self.btn_staff.setStyleSheet(u"QPushButton {\n"
"color: white;\n"
"background-color: rgba(9, 9, 9, 100);\n"
"text-align: left;\n"
"width: 260px;\n"
"height: 50px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: rgba(255,85, 127, 100);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: rgba(255, 255, 255, 70);\n"
"}\n"
"")
        icon = QIcon()
        icon.addFile(u":/icon/icons/recent_actors_white_24dp.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_staff.setIcon(icon)
        self.btn_staff.setIconSize(QSize(32, 32))

        self.verticalLayout.addWidget(self.btn_staff)

        self.btn_studydoc = QPushButton(self.centralwidget)
        self.btn_studydoc.setObjectName(u"btn_studydoc")
        self.btn_studydoc.setStyleSheet(u"QPushButton {\n"
"color: white;\n"
"background-color: rgba(9, 9, 9, 100);\n"
"text-align: left;\n"
"width: 260px;\n"
"height: 50px;\n"
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

        self.verticalLayout.addWidget(self.btn_studydoc)

        self.btn_group = QPushButton(self.centralwidget)
        self.btn_group.setObjectName(u"btn_group")
        self.btn_group.setStyleSheet(u"QPushButton {\n"
"color: white;\n"
"background-color: rgba(9, 9, 9, 100);\n"
"text-align: left;\n"
"width: 260px;\n"
"height: 50px;\n"
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

        self.btn_book = QPushButton(self.centralwidget)
        self.btn_book.setObjectName(u"btn_book")
        self.btn_book.setStyleSheet(u"QPushButton {\n"
"color: white;\n"
"background-color: rgba(9, 9, 9, 100);\n"
"text-align: left;\n"
"width: 260px;\n"
"height: 50px;\n"
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

        self.btn_test = QPushButton(self.centralwidget)
        self.btn_test.setObjectName(u"btn_test")
        self.btn_test.setStyleSheet(u"QPushButton {\n"
"color: white;\n"
"background-color: rgba(9, 9, 9, 100);\n"
"text-align: left;\n"
"width: 260px;\n"
"height: 50px;\n"
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

        self.btn_analis = QPushButton(self.centralwidget)
        self.btn_analis.setObjectName(u"btn_analis")
        self.btn_analis.setStyleSheet(u"QPushButton {\n"
"color: white;\n"
"background-color: rgba(9, 9, 9, 100);\n"
"text-align: left;\n"
"width: 260px;\n"
"height: 50px;\n"
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
        self.btn_analis.setIcon(icon5)
        self.btn_analis.setIconSize(QSize(32, 32))

        self.verticalLayout.addWidget(self.btn_analis)

        self.btn_settings = QPushButton(self.centralwidget)
        self.btn_settings.setObjectName(u"btn_settings")
        self.btn_settings.setStyleSheet(u"QPushButton {\n"
"color: white;\n"
"background-color: rgba(9, 9, 9, 100);\n"
"text-align: left;\n"
"width: 260px;\n"
"height: 50px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: rgba(255,85, 127, 100);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: rgba(255, 255, 255, 70);\n"
"}")
        icon6 = QIcon()
        icon6.addFile(u":/icon/icons/settings_white_24dp.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_settings.setIcon(icon6)
        self.btn_settings.setIconSize(QSize(32, 32))

        self.verticalLayout.addWidget(self.btn_settings)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Labor protection", None))
        self.btn_staff.setText(QCoreApplication.translate("MainWindow", u"\u041a\u0430\u0434\u0440\u043e\u0432\u0438\u0439 \u043e\u0431\u043b\u0456\u043a", None))
        self.btn_studydoc.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0432\u0447\u0430\u043b\u044c\u043d\u0430 \u0434\u043e\u043a\u0443\u043c\u0435\u043d\u0442\u0430\u0446\u0456\u044f", None))
        self.btn_group.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0432\u0447\u0430\u043b\u044c\u043d\u0456 \u0433\u0440\u0443\u043f\u0438", None))
        self.btn_book.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0432\u0447\u0430\u043b\u044c\u043d\u0456 \u043c\u0430\u0442\u0435\u0440\u0456\u0430\u043b\u0438", None))
        self.btn_test.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0435\u0440\u0435\u0432\u0456\u0440\u043a\u0430 \u0437\u043d\u0430\u043d\u044c", None))
        self.btn_analis.setText(QCoreApplication.translate("MainWindow", u"\u0410\u043d\u0430\u043b\u0456\u0442\u0438\u0447\u043d\u0456 \u0437\u0432\u0456\u0442\u0438", None))
        self.btn_settings.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u043b\u0430\u0448\u0442\u0443\u0432\u0430\u043d\u043d\u044f", None))
    # retranslateUi

