import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QLineEdit,
    QPushButton, QFormLayout, QMessageBox, QComboBox, QTableWidget, QTableWidgetItem, QHBoxLayout, QScrollArea
)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from Product import Bavul, Cuzdan, Kemer, Canta
from RenovationAdd import RenovationAdd
from RenovationView import RenovationView
from Stock import Stock

class RenovationMain(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        # Initialize stock management system
        self.stock = Stock()

        # Main window settings
        self.setWindowTitle("Gökhan Çanta Stok Yönetim Sistemi")
        self.setGeometry(150, 150, 900, 700)
        self.setStyleSheet("font-weight: bold;background-color:#E6E6FA;")

        # Central widget and layout
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)

        # Create horizontal layout for the title and back button
        self.header_layout = QHBoxLayout()
        
        # Title label
        self.title_label = QLabel("Gökhan Çanta Tamirat Kayıt Formu")
        self.title_label.setStyleSheet("font-size: 32px; font-weight: bold; padding-top: 40px;padding-left: 80px;")  # Added padding-top
        self.title_label.setAlignment(Qt.AlignCenter)
        
        # Back Button
        self.back_button = QPushButton("Geri")
        self.back_button.clicked.connect(self.go_back)
        self.back_button.setStyleSheet("font-weight: bold;")
        self.back_button.setMinimumSize(80, 25)  # Minimum Width: 80 pixels, Minimum Height: 25 pixels
        self.back_button.setMaximumSize(120, 35)  # Maximum Width: 120 pixels, Maximum Height: 35 pixels

        # Add widgets to header layout
        self.header_layout.addWidget(self.title_label)
        self.header_layout.addWidget(self.back_button)

        # Add header layout to the main layout
        self.layout.addLayout(self.header_layout)

        self.layout.addSpacing(40)  # Adjust the value to your desired spacing

        # Add the image with a frame
        self.image_label = QLabel()
        pixmap = QPixmap("C:\\Users\\nilay\\Desktop\\canta.jpeg")
        pixmap = pixmap.scaled(300, 300, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.image_label.setPixmap(pixmap)
        self.image_label.setFixedSize(pixmap.size())  # Set the QLabel size to the size of the image
        self.image_label.setAlignment(Qt.AlignCenter)
        self.image_label.setStyleSheet("border: 2px solid black;")  # Add a black border
        self.layout.addWidget(self.image_label, alignment=Qt.AlignCenter)


        # Button layout
        self.button_layout = QHBoxLayout()

        # Create buttons
        self.tadilat_add_product_button = QPushButton("Tadilat Ürün Ekleme")
        self.tadilat_add_product_button.setFixedSize(200, 150)  # Square button size
        self.tadilat_add_product_button.setStyleSheet("background-color: lightblue; font-weight: bold; font-size: 17px;border: 2px solid black;")
        self.tadilat_add_product_button.clicked.connect(self.show_renovation_add_product_dialog)
        self.button_layout.addWidget(self.tadilat_add_product_button)

        self.tadilat_view_product_button = QPushButton("Tadilat Ürün İzleme")
        self.tadilat_view_product_button.setFixedSize(200, 150)  # Square button size
        self.tadilat_view_product_button.setStyleSheet("background-color: lightcoral; font-weight: bold; font-size: 17px;border: 2px solid black;")
        self.tadilat_view_product_button.clicked.connect(self.show_renovation_product_dialog)
        self.button_layout.addWidget(self.tadilat_view_product_button)

        # Add button layout to the main layout
        self.layout.addStretch(1)
        self.layout.addLayout(self.button_layout)
        self.layout.addStretch(1)

    def show_renovation_add_product_dialog(self):
        self.renovationadd = RenovationAdd(self)
        self.renovationadd.show()

    def show_renovation_product_dialog(self):
        self.renovationshow = RenovationView(self)
        self.renovationshow.show()

    def go_back(self):
        from MainPage2 import MainApp  # Import inside the function
        self.main_app = MainApp()  # Initialize the MainApp class
        self.main_app.show()
        self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = RenovationMain()
    window.show()
    sys.exit(app.exec_())
