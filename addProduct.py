import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QFormLayout, QMessageBox, QComboBox, QTableWidget, QTableWidgetItem
from PyQt5.QtCore import Qt
from Product import Bag, Belt, Suitcase, Wallet
from Stock import Stock

class StockManagerApp(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        # Stok yönetim sistemini oluşturuyoruz
        self.stock = Stock()

        # Ana pencere ayarları
        self.setWindowTitle("Stok Yönetimi")
        self.setGeometry(100, 100, 800, 600)

        # Merkez widget ve layout
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)

        # Ürün ekleme bölümü
        self.form_layout = QFormLayout()
        self.product_type = QComboBox()
        self.product_type.addItems(["Suitcase", "Wallet", "Belt", "Bag"])
        self.name_entry = QLineEdit()
        self.color_entry = QLineEdit()
        self.brand_entry = QLineEdit()
        self.stock_code_entry = QLineEdit()
        self.date_entry = QLineEdit()
        self.stock_amount_entry = QLineEdit()
        self.size_entry = QLineEdit()
        self.height_entry = QLineEdit()
        self.type_entry = QLineEdit()

        self.form_layout.addRow("Ürün Türü:", self.product_type)
        self.form_layout.addRow("Ürün Adı:", self.name_entry)
        self.form_layout.addRow("Renk:", self.color_entry)
        self.form_layout.addRow("Marka:", self.brand_entry)
        self.form_layout.addRow("Stok Kodu:", self.stock_code_entry)
        self.form_layout.addRow("Tarih:", self.date_entry)
        self.form_layout.addRow("Stok Miktarı:", self.stock_amount_entry)
        self.form_layout.addRow("Boyut (Sadece Suitcase için):", self.size_entry)
        self.form_layout.addRow("Yükseklik (Sadece Belt için):", self.height_entry)
        self.form_layout.addRow("Tür (Sadece Bag için):", self.type_entry)

        self.add_button = QPushButton("Ürün Ekle")
        self.add_button.clicked.connect(self.add_product)

        self.form_layout.addWidget(self.add_button)
        self.layout.addLayout(self.form_layout)

        # Ürün listeleme bölümü
        self.table = QTableWidget()
        self.table.setColumnCount(8)
        self.table.setHorizontalHeaderLabels(["Ürün Adı", "Renk", "Marka", "Stok Kodu", "Tarih", "Stok Miktarı", "Ekstra 1", "Ekstra 2"])
        self.layout.addWidget(self.table)

        self.update_button = QPushButton("Ürünleri Listele")
        self.update_button.clicked.connect(self.update_table)
        self.layout.addWidget(self.update_button)

    def add_product(self):
        product_type = self.product_type.currentText()
        name = self.name_entry.text()
        color = self.color_entry.text()
        brand = self.brand_entry.text()
        stock_code = self.stock_code_entry.text()
        date = self.date_entry.text()
        stock_amount = int(self.stock_amount_entry.text())
        size = self.size_entry.text() if product_type == "Suitcase" else None
        height = self.height_entry.text() if product_type == "Belt" else None
        type_ = self.type_entry.text() if product_type == "Bag" else None

        if product_type == "Suitcase":
            product = Suitcase(name, color, brand, stock_code, date, stock_amount, size)
        elif product_type == "Wallet":
            product = Wallet(name, color, brand, stock_code, date, stock_amount)
        elif product_type == "Belt":
            product = Belt(name, color, brand, stock_code, date, stock_amount, height)
        elif product_type == "Bag":
            product = Bag(name, color, brand, stock_code, date, stock_amount, type_)
        else:
            QMessageBox.warning(self, "Hata", "Geçersiz ürün türü!")
            return

        self.stock.add(product)
        QMessageBox.information(self, "Başarı", f"Ürün eklendi: {product}")

    def update_table(self):
        self.table.setRowCount(0)
        for product in self.stock.products.values():
            row_position = self.table.rowCount()
            self.table.insertRow(row_position)
            self.table.setItem(row_position, 0, QTableWidgetItem(product.name))
            self.table.setItem(row_position, 1, QTableWidgetItem(product.color))
            self.table.setItem(row_position, 2, QTableWidgetItem(product.brand))
            self.table.setItem(row_position, 3, QTableWidgetItem(product.stock_code))
            self.table.setItem(row_position, 4, QTableWidgetItem(product.date))
            self.table.setItem(row_position, 5, QTableWidgetItem(str(product.stock_amount)))
            if isinstance(product, Suitcase):
                self.table.setItem(row_position, 6, QTableWidgetItem(product.size))
                self.table.setItem(row_position, 7, QTableWidgetItem(''))
            elif isinstance(product, Wallet):
                self.table.setItem(row_position, 6, QTableWidgetItem(''))
                self.table.setItem(row_position, 7, QTableWidgetItem(''))
            elif isinstance(product, Belt):
                self.table.setItem(row_position, 6, QTableWidgetItem(str(product.height)))
                self.table.setItem(row_position, 7, QTableWidgetItem(''))
            elif isinstance(product, Bag):
                self.table.setItem(row_position, 6, QTableWidgetItem(''))
                self.table.setItem(row_position, 7, QTableWidgetItem(product.type))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = StockManagerApp()
    window.show()
    sys.exit(app.exec_())
