import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QSystemTrayIcon, QMenu, QLineEdit, QHBoxLayout
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt

class ClipboardApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Clipboard App')
        self.setGeometry(300, 300, 300, 100)

        layout = QVBoxLayout()

        # First value
        hbox1 = QHBoxLayout()
        self.value1 = QLineEdit(self)
        self.value1.setText("Value 1")
        hbox1.addWidget(self.value1)
        self.button1 = QPushButton('Copy', self)
        self.button1.clicked.connect(lambda: self.copyToClipboard(self.value1.text()))
        hbox1.addWidget(self.button1)
        layout.addLayout(hbox1)

        # Second value
        hbox2 = QHBoxLayout()
        self.value2 = QLineEdit(self)
        self.value2.setText("Value 2")
        hbox2.addWidget(self.value2)
        self.button2 = QPushButton('Copy', self)
        self.button2.clicked.connect(lambda: self.copyToClipboard(self.value2.text()))
        hbox2.addWidget(self.button2)
        layout.addLayout(hbox2)

        self.setLayout(layout)

        # Create system tray icon
        self.tray_icon = QSystemTrayIcon(self)
        self.tray_icon.setIcon(QIcon.fromTheme("edit-copy"))
        
        # Create tray menu
        tray_menu = QMenu()
        show_action = tray_menu.addAction("Show")
        show_action.triggered.connect(self.show)
        quit_action = tray_menu.addAction("Quit")
        quit_action.triggered.connect(app.quit)
        self.tray_icon.setContextMenu(tray_menu)
        
        self.tray_icon.show()

    def copyToClipboard(self, value):
        clipboard = QApplication.clipboard()
        clipboard.setText(value)

    def closeEvent(self, event):
        event.ignore()
        self.hide()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ClipboardApp()
    ex.show()
    sys.exit(app.exec_())