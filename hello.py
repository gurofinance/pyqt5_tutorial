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
        

        #Change the font size of label
        my_label.setFont(qtg.QFont("Arial", 18))
        self.layout().addWidget(my_label)

        my_entry = qtw.QLineEdit()
        my_entry.setObjectName("name_field")
        my_entry.setText("")
        self.layout().addWidget(my_entry)

        #Create a button
        my_button = qtw.QPushButton("Click Me" ,clicked = lambda : press_it())
        my_button.setObjectName("my_button")
        self.layout().addWidget(my_button)

        self.show()

        def press_it():
            #Add name to label
            my_label.setText(f"Hello {my_entry.text()}!!")

            #clear the entry box
            my_entry.setText("")
app = qtw.QApplication([])

mw = MainWindow()

#Run The Application
app.exec_()