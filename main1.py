#import sys
import pymysql
from config import host, user, db_name

#from PySide6 import QtWidgets
#from PySide6.QtWidgets import QApplication, QMainWindow

#from ui_main import Ui_MainWindow

try:
    connection = pymysql.connect(
        host = "localhost",
        port = 8889,
        user= "root",
        password = "root",
        database = "diplom_test",
        cursorclass=pymysql.cursors.DictCursor
    )
    print("successfully connected...")
    print("#"*20)

    try:
        with connection.cursor() as cursor:
            create_table_query = "CREATE TABLE IF NOT EXISTS `employees1`(id int AUTO_INCREMENT,"\
            #"surname_employee varchar(25) NOT NULL,"\
            #"name_employee varchar(25) NOT NULL,"\
            #"paronymic_employee varchar(25) NOT NULL,"\
            #"bithday_employee date NOT NULL,"\
            #"start_work_day date, "\
            #"adress_employee varchar(155) NOT NULL,"\
            #"telefone_employee varchar(25) NOT NULL,"\
            #"id_department INTEGER NOT NULL,"
            #"FOREIGN KEY fk_id_department (id_department) REFERENCES departments(id_department),"\
           #"id_profession INTEGER NOT NULL,"
           # "FOREIGN KEY fk_id_profesions (id_proffesssion) REFERENCES profesions(id_profession),"\
            "PRIMARY KEY (id_employee));"
            cursor.execute(create_table_query)
            print("Table created succssesfully")
    finally:
        connection.close()
except Exception as ex:
    print('Connection refused...')
    print(ex)

#class LaborProtection(QMainWindow):
    #def __init__(self):
       #super(LaborProtection, self).__init__()
       #self.ui = Ui_MainWindow()
       #self.ui.setupUi(self)


#if __name__ == "__main__":
    #app = QApplication(sys.argv)
    #window = LaborProtection()
    #window.show()

    #sys.exit(app.exec())

        