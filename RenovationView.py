import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QLineEdit,
    QPushButton, QFormLayout, QMessageBox, QComboBox, QTableWidget, QTableWidgetItem, QHBoxLayout, QScrollArea
)
from PyQt5.QtCore import Qt
from Product import Bavul, Cuzdan, Kemer, Canta
from Stock import Stock

class RenovationView(QMainWindow):
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
        self.title_label = QLabel("Tamirat İzleme Formu")
        self.title_label.setStyleSheet("font-size: 22px; font-weight: bold;")
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

        # Create and set the form layout
        self.form_layout = QFormLayout()

        # Username Entry
        self.username_entry = QLineEdit()
        username_label = QLabel("Müşteri Adı Soyadı:")
        username_label.setStyleSheet("font-weight: bold;")
        self.form_layout.addRow(username_label, self.username_entry)
        
        # Tamirat Entry
        self.tamırat_entry = QLineEdit()
        tamırat_label = QLabel("Tamirat No:")
        tamırat_label.setStyleSheet("font-weight: bold;")
        self.form_layout.addRow(tamırat_label, self.tamırat_entry)
        

        # Product entry form
        self.layout.addLayout(self.form_layout)

        # Update Table Button
        self.update_button = QPushButton("Ürün Listele")
        self.update_button.clicked.connect(self.update_table)
        self.update_button.setStyleSheet("font-weight: bold;")
        self.layout.addWidget(self.update_button)

        # Create a scroll area for the table widget
        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)  # Make sure the widget inside the scroll area is resizable
        self.scroll_area.setStyleSheet("background-color: #E6E6FA;")  # Set background color for the scroll area
        
        # Product listing section
        self.table = QTableWidget()
        self.table.setColumnCount(9)
        self.table.setHorizontalHeaderLabels(["Müşteri Adı Soyadı", "Renk", "Marka", "Stok Kodu", "Tarih", "Stok Miktarı", "Boyut", "Uzunluk", "Tür"])
        self.table.horizontalHeader().setStyleSheet("font-weight: bold;")
        
        # Set minimum height for the table
        self.table.setMinimumHeight(400)  # Adjust as needed

        # Create a widget to hold the table
        self.table_widget = QWidget()
        self.table_layout = QVBoxLayout()
        self.table_widget.setLayout(self.table_layout)
        self.table_layout.addWidget(self.table)

        # Set the widget with the table into the scroll area
        self.scroll_area.setWidget(self.table_widget)

        # Add scroll area to the main layout
        self.layout.addWidget(self.scroll_area)


    def on_product_type_changed(self, index):
        product_type = self.product_type.currentText()
        self.type_entry.setVisible(product_type == "Canta")
        self.size_entry.setVisible(product_type == "Bavul")
        self.height_entry.setVisible(product_type == "Kemer")

    def add_product(self):
        username = self.username_entry.text()
        tamırat = self.tamırat_entry.text()
        product_type = self.product_type.currentText()
        color = self.color_entry.currentText()
        brand = self.brand_entry.currentText()
        stock_code = self.stock_code_entry.text()
        date = self.date_entry.text()
        size = self.size_entry.currentText() if product_type == "Bavul" else None
        height = self.height_entry.text() if product_type == "Kemer" else None
        type_ = self.type_entry.currentText() if product_type == "Canta" else None

        if product_type == "Bavul":
            product = Bavul(username, tamırat, color, brand, stock_code, date, size)
        elif product_type == "Cuzdan":
            product = Cuzdan(username, tamırat, color, brand, stock_code, date)
        elif product_type == "Kemer":
            product = Kemer(username, tamırat, color, brand, stock_code, date, height)
        elif product_type == "Canta":
            product = Canta(username, tamırat, color, brand, stock_code, date, type_)
        else:
            QMessageBox.warning(self, "Hata", "Geçersiz ürün türü!")
            return

        self.stock.add(product)
        QMessageBox.information(self, "Başarı", f"Ürün eklendi: {product}")

    def update_table(self):
        self.table.setRowCount(0)
        username = self.username_entry.text()
        tamırat = self.tamırat_entry.text()

        for product in self.stock.products.values():
            if (username and product.username != username) or (tamırat and product.tamırat != tamırat):
                continue  # Skip products that don't match the filter

            row_position = self.table.rowCount()
            self.table.insertRow(row_position)
            self.table.setItem(row_position, 0, QTableWidgetItem(product.username))
            self.table.setItem(row_position, 1, QTableWidgetItem(product.tamırat))
            self.table.setItem(row_position, 2, QTableWidgetItem(product.color))
            self.table.setItem(row_position, 3, QTableWidgetItem(product.brand))
            self.table.setItem(row_position, 4, QTableWidgetItem(product.stock_code))
            self.table.setItem(row_position, 5, QTableWidgetItem(product.date))
            if isinstance(product, Bavul):
                self.table.setItem(row_position, 6, QTableWidgetItem(product.size))
                self.table.setItem(row_position, 7, QTableWidgetItem(''))
            elif isinstance(product, Cuzdan):
                self.table.setItem(row_position, 6, QTableWidgetItem(''))
                self.table.setItem(row_position, 7, QTableWidgetItem(''))
            elif isinstance(product, Kemer): 
                self.table.setItem(row_position, 6, QTableWidgetItem(str(product.height)))
                self.table.setItem(row_position, 7, QTableWidgetItem(''))
            elif isinstance(product, Canta):
                self.table.setItem(row_position, 6, QTableWidgetItem(''))
                self.table.setItem(row_position, 7, QTableWidgetItem(product.type_))
    
    def go_back(self):
        from MainPage2 import MainApp  # Import inside the function
        self.main_app = MainApp()  # Initialize the MainApp class
        self.main_app.show()
        self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Renovation()
    window.show()
    sys.exit(app.exec_())
