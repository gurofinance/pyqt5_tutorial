from multiprocessing.sharedctypes import Value
import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg

class MainWindow(qtw.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Hello World What's up")

        #set Vertical layout
        self.setLayout(qtw.QVBoxLayout())
        
        #Create A label
        my_label = qtw.QLabel("Hello World")
        my_select = qtw.QLabel("Select a ")
        my_spin_text = qtw.QLabel("Spin Box Select is a") 
        #Change the font size of label
        my_label.setFont(qtg.QFont("Arial", 18))
        self.layout().addWidget(my_label)

        my_select.setFont(qtg.QFont("Arial", 18))
        self.layout().addWidget(my_select)

        my_spin_text.setFont(qtg.QFont("Arial", 18))
        self.layout().addWidget(my_spin_text)

        
        # self.layout().addWidget(my_select)


        my_entry = qtw.QLineEdit()
        my_entry.setObjectName("name_field")
        my_entry.setText("")
        self.layout().addWidget(my_entry)

        #Create Combo Box , editable'True 이면 선택 가능하고 편집이 가능
        my_combo = qtw.QComboBox(self , editable = True, insertPolicy = qtw.QComboBox.InsertAtBottom)

        #Add items to combo box
        item_list = ['Python', 'Java', 'C++', 'C#', 'JavaScript']
        my_combo.addItem('Python' , 'Super Supter Cool!')
        my_combo.addItem('Java' , 2)
        my_combo.addItem('Python' , qtw.QWidget)
        my_combo.addItems(['One', 'Two', 'Three'])
        my_combo.insertItem(2, 'Third things')
        self.layout().addWidget(my_combo)
        
        #정수 값을 저장하기 위한 변수  
        # my_spin=qtw.QSpinBox(self,
        #     value=10,
        #     maximum=100,
        #     minimum=0,
        #     singleStep=5,
        #     prefix='$',
        #     suffix='ORDER',
        # )

        #실수 값을 저장하기 위한 변수  
        my_spin=qtw.QDoubleSpinBox(self,
            value=10,
            maximum=100,
            minimum=0,
            singleStep=5.5,
            prefix='Your Order $',
            suffix='!!!!',
        )
        #put the spin box in the layout
        self.layout().addWidget(my_spin)

        #Create a button
        my_button = qtw.QPushButton("Click Me" ,clicked = lambda : press_it())
        my_button.setObjectName("my_button")
        self.layout().addWidget(my_button)

        self.show()

        def press_it():
            #Add name to label
            my_label.setText(f"Hello {my_entry.text()}!!")
            my_select.setText(f"You selected {my_combo.currentText()}")
            my_spin_text.setText(str(f'Your Select Number  is {(my_spin.value()) + 1}'))
            #clear the entry box
            my_entry.setText("")
app = qtw.QApplication([])

mw = MainWindow()

#Run The Application
app.exec_()