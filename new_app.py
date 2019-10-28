from PySide2 import QtWidgets, QtGui, QtCore
import new_random_gui
from populate_list import populate_lists
from roster_ops import add_name, remove_name, edit_name

class MyQtApp(new_random_gui.Ui_MainWindow, QtWidgets.QMainWindow):
    def __init__(self):
        super(MyQtApp,self).__init__()
        self.setupUi(self)
        self.current_period = '2nd'
        self.wanted_groups = 2
        self.widget_list = []
        self.num_of_groups.activated.connect(self.build_groups)
        self.select_period.activated.connect(self.update_period)
        self.populate_the_lists(self.current_period,self.wanted_groups,self.widget_list)
        self.select_period.activated.connect(self.update_lists)
        self.update_period()
        self.update_lists()
        self.randomize_button.pressed.connect(self.rand_groups_now)
        self.rand_groups_now()
        self.actionAdd_Student.triggered.connect(self.add_student)
        self.actionRemove_Student.triggered.connect(self.remove_student)
        self.actionEdit_Student.triggered.connect(self.edit_student)
        self.lists = ['list1', 'list2', 'list3', 'list4', 'list5', 'list6', 'list7', 'list8', 'list9', 'list10', 'list11', 
                      'list12', 'list13', 'list14', 'list15']
        self.labels = ['label1', 'label2', 'label3', 'label4', 'label5', 'label6', 'label7', 'label8', 'label9', 'label10',
                      'label11', 'label12', 'label13', 'label14', 'label15']
        self.colors = ['#f4cccc', '#c9daf8', '#fce5cd', '#d9ead3', '#fff2cc', '#d9d2e9', '#f0a8f3', '#abeef7', '#c8faa2', 
                       '#fcf875', '#ff8e8e', '#d2acff', '#ffd356', '#70ffc8', '#80b1ff']

    def clear_groups(self):
        while self.list_layout.count() > 0:
            item = self.list_layout.takeAt(self.list_layout.count()-1)
            widget = item.widget()
            widget.deleteLater()

    def build_groups(self):
        if self.num_of_groups.activated:
            self.clear_groups()
            self.wanted_groups = int(self.num_of_groups.currentText())
            print(self.wanted_groups)
            self.widget_list = []
            if 2 <= self.wanted_groups <= 9:
                for i in range(0,self.wanted_groups):
                    label_row = 2 * (i // 3)
                    list_row = label_row + 1
                    label_column = i % 3
                    list_column = label_column
                    self.list_layout.addWidget(QtWidgets.QLabel(f'Group {i+1}',objectName=f'{self.labels[i]}', font=self.font1, 
                                                                alignment=QtGui.Qt.AlignCenter), label_row, label_column)
                    abc = QtWidgets.QListWidget()
                    self.list_layout.addWidget(abc,list_row,list_column)
                    self.widget_list.append(abc)
                    font = QtGui.QFont()
                    font.setPointSize(20)
                    abc.setFont(font)
                    abc.setStyleSheet(f'background-color: {self.colors[i]}')
            if 10 <= self.wanted_groups <= 15:
                for i in range(0,self.wanted_groups):
                    label_row = 2 * (i // 5)
                    list_row = label_row + 1
                    label_column = i % 5
                    list_column = label_column
                    self.list_layout.addWidget(QtWidgets.QLabel(f'Group {i+1}',objectName=f'{self.labels[i]}', font=self.font1, 
                                                                alignment=QtGui.Qt.AlignCenter), label_row, label_column)
                    abc = QtWidgets.QListWidget()
                    self.list_layout.addWidget(abc,list_row,list_column)
                    self.widget_list.append(abc)
                    font = QtGui.QFont()
                    font.setPointSize(20)
                    abc.setFont(font)
                    abc.setStyleSheet(f'background-color: {self.colors[i]}')
        self.update_lists()

    def populate_the_lists(self,current_period,wanted_groups,widget_list,rand=False):
        populate_lists(self,current_period,wanted_groups,widget_list,rand)

    def update_period(self):
        if self.select_period.activated:
            self.current_period = self.select_period.currentText()
            print(self.current_period)

    def update_lists(self):
        self.populate_the_lists(self.current_period,self.wanted_groups,self.widget_list)

    def rand_groups_now(self):
        if self.randomize_button.pressed:
            self.populate_the_lists(self.current_period,self.wanted_groups,self.widget_list,rand=True)
            print(self.widget_list)

    def add_student(self):
        who, ok = QtWidgets.QInputDialog.getText(self, 'Add', 'Enter the student\'s name:')
        if ok and who:
            add_name(self.current_period,who)
            self.update_lists()

    def remove_student(self):
        who, ok = QtWidgets.QInputDialog.getText(self, 'Remove', 'Enter the student\'s name:')
        if ok and who:
            remove_name(self.current_period,who)
            self.update_lists()

    def edit_student(self):
        who, ok = QtWidgets.QInputDialog.getText(self, 'Edit', 'Enter the name you want to edit:')
        if ok and who:
            who2, ok2 = QtWidgets.QInputDialog.getText(self, 'Edit', 'Enter the correct name:')
            if ok2 and who2:
                edit_name(self.current_period,who,who2)
                self.update_lists()

if __name__ == '__main__':
    app = QtWidgets.QApplication()
    qt_app = MyQtApp()
    qt_app.build_groups()
    qt_app.populate_the_lists(qt_app.current_period,qt_app.wanted_groups,qt_app.widget_list,rand=False)
    qt_app.show()
    app.exec_()