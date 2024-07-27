import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QLineEdit, QFormLayout, QMessageBox, QTableWidget, QTableWidgetItem, QDialog
from PyQt5.QtCore import Qt

from addProduct import StockManagerApp

class MainApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Gökhan Çanta Stok Yönetim Sistemi")
        self.setGeometry(100, 100, 800, 600)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.main_layout = QVBoxLayout()
        self.central_widget.setLayout(self.main_layout)

        self.title_label = QLabel("Gökhan Çanta Stok Yönetim Sistemi")
        self.title_label.setStyleSheet("font-size: 35px; font-weight: bold;")
        self.title_label.setAlignment(Qt.AlignCenter)
        self.main_layout.addWidget(self.title_label)

        self.button_layout = QHBoxLayout()

        # Butonları oluştur
        self.add_product_button = QPushButton("Ürün Ekleme")
        self.add_product_button.setFixedSize(150, 150)  # Kare buton boyutu
        self.add_product_button.setStyleSheet("background-color: lightblue; font-weight: bold; font-size: 17px;")
        self.add_product_button.clicked.connect(self.show_add_product_dialog)
        self.button_layout.addWidget(self.add_product_button)

        self.delete_product_button = QPushButton("Ürün Silme")
        self.delete_product_button.setFixedSize(150, 150)  # Kare buton boyutu
        self.delete_product_button.setStyleSheet("background-color: lightcoral; font-weight: bold; font-size: 17px;")
        self.delete_product_button.clicked.connect(self.show_delete_product_dialog)
        self.button_layout.addWidget(self.delete_product_button)

        self.view_stock_button = QPushButton("Stok Görünümü")
        self.view_stock_button.setFixedSize(150, 150)  # Kare buton boyutu
        self.view_stock_button.setStyleSheet("background-color: lightgreen; font-weight: bold; font-size: 17px;")
        self.view_stock_button.clicked.connect(self.show_view_stock_dialog)
        self.button_layout.addWidget(self.view_stock_button)

        # Butonları ortalamak için bir spacer ekleyin
        self.main_layout.addStretch(1)
        self.main_layout.addLayout(self.button_layout)
        self.main_layout.addStretch(1)

        self.stock = {}

    def show_add_product_dialog(self):
        self.stock_manager_app = StockManagerApp(self)
        self.stock_manager_app.show()

    def show_delete_product_dialog(self):
        dialog = DeleteProductDialog(self)
        dialog.exec_()

    def show_view_stock_dialog(self):
        dialog = ViewStockDialog(self)
        dialog.exec_()

class DeleteProductDialog(QDialog):
    def __init__(self, parent):
        super().__init__(parent)
        self.setWindowTitle("Ürün Silme")
        self.setGeometry(150, 150, 400, 200)

        self.layout = QFormLayout()
        self.setLayout(self.layout)

        self.name_entry = QLineEdit()
        self.layout.addRow("Ürün Adı:", self.name_entry)

        self.delete_button = QPushButton("Sil")
        self.delete_button.clicked.connect(self.delete_product)
        self.layout.addWidget(self.delete_button)

    def delete_product(self):
        name = self.name_entry.text()

        if name in self.parent().stock:
            del self.parent().stock[name]
            QMessageBox.information(self, "Başarılı", "Ürün silindi!")
            self.close()
        else:
            QMessageBox.warning(self, "Hata", "Ürün bulunamadı.")

class ViewStockDialog(QDialog):
    def __init__(self, parent):
        super().__init__(parent)
        self.setWindowTitle("Stok Görünümü")
        self.setGeometry(150, 150, 600, 400)

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.table = QTableWidget()
        self.table.setColumnCount(2)
        self.table.setHorizontalHeaderLabels(["Ürün Adı", "Stok Miktarı"])
        self.layout.addWidget(self.table)

        self.update_table()

    def update_table(self):
        self.table.setRowCount(0)
        for name, quantity in self.parent().stock.items():
            row_position = self.table.rowCount()
            self.table.insertRow(row_position)
            self.table.setItem(row_position, 0, QTableWidgetItem(name))
            self.table.setItem(row_position, 1, QTableWidgetItem(str(quantity)))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    sys.exit(app.exec_())
