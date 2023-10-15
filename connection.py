from PySide6 import QtWidgets, QtSql


class Data:
    def __init__(self):
        super(Data, self). __init__()

    def creat_connection(self):
        db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName('expense_db.db')
        
        if not db.open():
            QtWidgets.QMessageBox.critical(None, "Cannot open database",
                                           "Click Censel to exit.", QtWidgets.QMessageBox.Cansel)
            return False
        
        query = QtSql.QSqlQuery()
        query.exec("CREATE TABLE IF NOT EXISTS expenses (ID integer primary key," 
                   "title VARCHAR(255)", "adress VARCHAR(255)","director VARCHAR(100)",
                   "telefone VARCHAR(11)", "e-mail VARCHAR(30)")
                   