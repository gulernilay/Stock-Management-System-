import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QLineEdit, QFormLayout, QMessageBox, QTableWidget, QTableWidgetItem, QDialog, QSpacerItem, QSizePolicy
)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from addProduct import StockManagerApp
from removeProduct import RemoveProduct
from showProduct import ShowProduct
from RenovationMain import RenovationMain

class MainApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Gökhan Çanta Stok Yönetim Sistemi")
        self.setGeometry(100, 100, 800, 600)
        self.setStyleSheet("font-weight: bold;background-color:#E6E6FA;")

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.main_layout = QVBoxLayout()
        self.central_widget.setLayout(self.main_layout)

        # Title label
        self.title_label = QLabel("Gökhan Çanta Stok Yönetim Sistemi")
        self.title_label.setStyleSheet("font-size: 32px; font-weight: bold;")
        self.title_label.setAlignment(Qt.AlignCenter)
        self.main_layout.addWidget(self.title_label)

        # Add spacer to increase the space between title and image
        self.main_layout.addSpacing(40)  # Adjust the value to your desired spacing

        # Add the image with a frame
        self.image_label = QLabel()
        pixmap = QPixmap("C:\\Users\\nilay\\Desktop\\canta.jpeg")
        pixmap = pixmap.scaled(300, 300, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.image_label.setPixmap(pixmap)
        self.image_label.setFixedSize(pixmap.size())  # Set the QLabel size to the size of the image
        self.image_label.setAlignment(Qt.AlignCenter)
        self.image_label.setStyleSheet("border: 2px solid black;")  # Add a black border
        self.main_layout.addWidget(self.image_label, alignment=Qt.AlignCenter)

        # Button layout
        self.button_layout = QHBoxLayout()

        self.main_layout.addSpacing(40)  # Adjust the value to your desired spacing

        # Create buttons
        self.add_product_button = QPushButton("Stok Ürün Ekleme")
        self.add_product_button.setFixedSize(200, 150)  # Square button size
        self.add_product_button.setStyleSheet("background-color: lightblue; font-weight: bold; font-size: 17px;border: 2px solid black;")
        self.add_product_button.clicked.connect(self.show_add_product_dialog)
        self.button_layout.addWidget(self.add_product_button)

        self.delete_product_button = QPushButton("Stok Ürün Silme")
        self.delete_product_button.setFixedSize(200, 150)  # Square button size
        self.delete_product_button.setStyleSheet("background-color: lightcoral; font-weight: bold; font-size: 17px;border: 2px solid black;")
        self.delete_product_button.clicked.connect(self.show_delete_product_dialog)
        self.button_layout.addWidget(self.delete_product_button)

        self.view_stock_button = QPushButton("Stok İzleme")
        self.view_stock_button.setFixedSize(200, 150)  # Square button size
        self.view_stock_button.setStyleSheet("background-color: lightgreen; font-weight: bold; font-size: 17px;border: 2px solid black;")
        self.view_stock_button.clicked.connect(self.show_view_stock_dialog)
        self.button_layout.addWidget(self.view_stock_button)

        self.check_renovation_button = QPushButton("Tadilat Yönetim")
        self.check_renovation_button.setFixedSize(200, 150)  # Square button size
        self.check_renovation_button.setStyleSheet("background-color: lightblue; font-weight: bold; font-size: 17px;border: 2px solid black;")
        self.check_renovation_button.clicked.connect(self.show_check_renovation_dialog)
        self.button_layout.addWidget(self.check_renovation_button)

        # Add stretchable space around buttons
        self.button_layout.addStretch(1)
        self.main_layout.addLayout(self.button_layout)
        self.main_layout.addStretch(1)

    def show_add_product_dialog(self):
        self.stock_manager_app = StockManagerApp(self)
        self.stock_manager_app.show()

    def show_delete_product_dialog(self):
        self.remove_product = RemoveProduct(self)
        self.remove_product.show()

    def show_view_stock_dialog(self):
        self.show_product = ShowProduct(self)
        self.show_product.show()

    def show_check_renovation_dialog(self):
        self.renovation_product = RenovationMain(self)
        self.renovation_product.show() 

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    sys.exit(app.exec_())
