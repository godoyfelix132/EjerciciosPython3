from PySide2.QtWidgets import QApplication, QLabel, QPushButton, QVBoxLayout, QMainWindow

app = QApplication([])
window = QMainWindow()
layout = QVBoxLayout()
#label = QLabel('hola mundo')
#label.show()
button = QPushButton('Button')
layout.addWidget(button)
window.setLayout(layout)
window.show()
app.exec_()