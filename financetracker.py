from os import supports_bytes_environ
import sqlite3
from datetime import datetime
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QInputDialog
import sys
from PyQt5.sip import setdestroyonexit

conn = sqlite3.connect("spent.db")
cur = conn.cursor()                  
sql = '''                           
create table if not exists expenses (
    amount number,
    category string,
    message string,
    date string
    )
'''
cur.execute(sql)                    
conn.commit()   

def window():

    buttonHeight = 170
    label1Text = "Track your your expenditures here:"


    def takeInput():
        value, ok = QInputDialog.getDouble(win, "Add amount:", "Amount")

        category, ok = QInputDialog.getText(win, "Add category:", "Category")

        message, ok = QInputDialog.getText(win, "Add message:", "Message")
  
        if value and category and message and ok:
            date = str(datetime.now())         
            data = (value, category, message, date) 
            sql = 'INSERT INTO expenses VALUES (?, ?, ?, ?)'
            cur.execute(sql,data)                    
            conn.commit()



    app = QApplication(sys.argv)
    win = QMainWindow()
    win.setGeometry(500,200,800,500)
    win.setWindowTitle("Finance Tracker")
 
    label1 = QLabel(win)
    label1.setText(label1Text)
    label1.adjustSize()
    label1.move(60,50)

    button1 = QPushButton(win)
    button1.setText("Add receipt")
    button1.clicked.connect(takeInput)
    button1.move(100, buttonHeight)
    

    win.show()
    sys.exit(app.exec_())
     
window()

