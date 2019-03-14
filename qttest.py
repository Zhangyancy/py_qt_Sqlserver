#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QTableWidgetItem
from qt_test1 import  Ui_MainWindow
import pymssql
class Main(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super(Main, self).__init__()
        self.setupUi(self)
        self.table()

    def table(self):
        res=self.btnPress1_clicked()
        self.tableWidget.setColumnCount(8)

        self.tableWidget.setRowCount(2)

        #j = 0  # 第几行（从0开始）
        #i = 0  # 第几列（从0开始）
        Value1 =[ "序号","考生编号","姓名","专业代码","专业名称","初试总成绩","复试总成绩","总成绩","备注", ] # 内容

        self.tableWidget.setRowHeight(0, 10)  # 设置i行的高度

        for i in range(0,9):
            Value = Value1[i]  # 内容
            self.tableWidget.setItem(0, i, QTableWidgetItem(Value))  # 设置j行i列的内容为Value
            self.tableWidget.setColumnWidth(i, 100)  # 设置j列的宽度
            #self.tableWidget.setColumnWidth(2, 15)  # 设置j列的宽度
        self.tableWidget.verticalHeader().setVisible(False)  # 隐藏垂直表头

        self.tableWidget.horizontalHeader().setVisible(False)  # 隐藏水平表头
        self.pushButton.clicked.connect(self.btnPress1_clicked)



    def SQLserver(self,name):
        server = "192.168.0.100"  # 连接服务器地址
        user = "sa"  # 连接帐号
        password = "root"  # 连接密码

        conn = pymssql.connect(server, user, password, "mydata")  # 获取连接
        if conn:
            print("连接成功!")

        cursor = conn.cursor()  # 获取光标
        # 查询数据
        cursor.execute('SELECT * FROM MsSheet1 WHERE 姓名=%s', name)

        #遍历数据（存放到元组中） 方式2
        for row in cursor:

            res=row
            print(row)
        # 关闭连接
        conn.close()
        return res
    def btnPress1_clicked(self):

        #以文本的形式输出到多行文本框
        name=self.Input_name.toPlainText()
        #print(name)
        if name.strip() != '':
            #print("输入欧克!")

            res=self.SQLserver(name)
            print(res)
            for i in range(0, 9):
                Value = str(res[i])  # 内容转字符串
                self.tableWidget.setItem(1, i, QTableWidgetItem(Value))  # 设置j行i列的内容为Value

        else:
            res=[]



if __name__ == '__main__':
    app = QApplication(sys.argv)
    #MainWindow = QMainWindow()
    #ui = Ui_MainWindow()
    #ui.setupUi(MainWindow)
    main = Main()
    main.show()
    #MainWindow.show()
    sys.exit(app.exec_())
