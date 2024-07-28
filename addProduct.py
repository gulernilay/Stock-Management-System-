import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QFormLayout, QMessageBox, QComboBox, QTableWidget, QTableWidgetItem
from PyQt5.QtCore import Qt
from Product import Bavul, Cuzdan, Kemer, Canta
from Stock import Stock

class StockManagerApp(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        # Initialize stock management system
        self.stock = Stock()

        # Main window settings
        self.setWindowTitle("Gökhan Çanta Stok Yönetim Sistemi")
        self.setGeometry(100, 100, 800, 600)
        self.setStyleSheet("font-weight: bold;background-color:#E6E6FA;")

        # Central widget and layout
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)

        # Product entry form
        self.form_layout = QFormLayout()
        self.product_type = QComboBox()
        self.product_type.addItems(["Bavul", "Cuzdan", "Kemer", "Canta"])
        self.product_type.currentIndexChanged.connect(self.on_product_type_changed)
        self.name_entry = QLineEdit()
        self.color_entry = QComboBox()
        self.color_entry.addItems([
            "Beyaz", "Gri", "Siyah", "Kırmızı", "Yeşil", "Mavi", "Sarı", "Mor", "Turuncu", "Pembe", "Kahverengi",
            "Bej", "Bordo", "Fuşya", "Krem", "Lacivert", "Altın", "Gümüş", "Şampanya", "Zeytin Yeşili", "Lavanta",
            "Menekşe", "Turkuaz", "İndigo", "Kömür", "Antrasit", "Safir", "Yakut", "Zümrüt", "Amber", "Deniz Mavisi",
            "Şeftali", "Somon", "Kabak", "Camgöbeği", "Ametist", "Koyu Yeşil", "Parlament Mavisi", "Gök Mavisi",
            "Bebek Mavisi", "Neon Yeşil", "Neon Turuncu", "Neon Pembe", "Neon Sarı", "Kül", "Kestane", "Mercan",
            "Kiremit", "Hardal", "Toprak", "Çikolata", "Gökyüzü Mavisi", "Erik", "Vişne", "Yosun Yeşili", "Mint Yeşili",
            "Pastel Pembe", "Pastel Mavi", "Pastel Yeşil", "Pastel Sarı", "Fıstık Yeşili", "Adaçayı", "Deniz Köpüğü",
            "Buz Mavisi", "Gökkuşağı"
        ])
        self.brand_entry = QComboBox()
        self.brand_entry.addItems([
            "Fossil", "Grande", "Louis Vuitton", "Gucci", "Prada", "Chanel", "Hermès", "Dior", "Burberry", "Versace",
            "Balenciaga", "Valentino", "Givenchy", "Dolce & Gabbana", "Fendi", "Bvlgari", "Salvatore Ferragamo",
            "Giorgio Armani", "Tory Burch", "Kate Spade", "Michael Kors", "Coach", "Ralph Lauren", "Tommy Hilfiger",
            "Calvin Klein", "Hugo Boss", "Lacoste", "Diesel", "Levi's", "Guess", "Mango", "Zara", "H&M", "Uniqlo",
            "Banana Republic", "Gap", "Old Navy", "Forever 21", "Express", "Abercrombie & Fitch", "American Eagle",
            "Urban Outfitters", "Free People", "Anthropologie", "Patagonia", "The North Face", "Columbia", "Lululemon",
            "Adidas", "Nike", "Puma", "Reebok", "New Balance", "Under Armour", "Skechers", "Converse", "Vans",
            "Timberland", "Dr. Martens", "UGG", "Clarks", "Birkenstock"
        ])
        self.stock_code_entry = QLineEdit()
        self.date_entry = QLineEdit()
        self.stock_amount_entry = QLineEdit()
        self.size_entry = QComboBox()
        self.size_entry.addItems([
            "Kabin Boy", "Küçük (20-25 cm)", "Orta (26-35 cm)", "Büyük (36-45 cm)", "Ekstra Büyük (46 cm ve üstü)"
        ])
        self.size_entry.setVisible(False)# Initially hidden 
        self.height_entry = QLineEdit()
        self.height_entry.setVisible(False)# Initially hidden 

        # Type entry for bags
        self.type_entry = QComboBox()
        self.type_entry.addItems([
            "Kadın Çantası", "Spor Çantası", "Bel Çantası", "Sırt Çantası", "El Çantası", "Omuz Çantası",
            "Postacı Çantası", "Portföy Çantası", "Clutch Çanta", "Tote Çanta", "Kese Çanta", "Makyaj Çantası",
            "İş Çantası", "Laptop Çantası", "Tablet Çantası", "Bebek Çantası", "Plaj Çantası", "Alışveriş Çantası",
            "Valiz", "Hafta Sonu Çantası", "Deri Çanta", "Kanvas Çanta", "Çapraz Askılı Çanta",
            "Mini Çanta", "Maxi Çanta", "Kapitone Çanta", "Dokuma Çanta"
        ])
        self.type_entry.setVisible(False)  # Initially hidden

        # Labels
        label_style = "font-weight: bold;"

        product_type_label = QLabel("Ürün Türü:")
        product_type_label.setStyleSheet(label_style)
        name_label = QLabel("Ürün Adı:")
        name_label.setStyleSheet(label_style)
        color_label = QLabel("Renk:")
        color_label.setStyleSheet(label_style)
        brand_label = QLabel("Marka:")
        brand_label.setStyleSheet(label_style)
        stock_code_label = QLabel("Stok Kodu:")
        stock_code_label.setStyleSheet(label_style)
        date_label = QLabel("Tarih:")
        date_label.setStyleSheet(label_style)
        stock_amount_label = QLabel("Stok Miktarı:")
        stock_amount_label.setStyleSheet(label_style)
        size_label = QLabel("Boyut (Sadece Bavul için):")
        size_label.setStyleSheet(label_style)
        height_label = QLabel("Uzunluk (Sadece Kemer için):")
        height_label.setStyleSheet(label_style)
        type_label = QLabel("Tür (Sadece Çanta için):")
        type_label.setStyleSheet(label_style)

        # Adding widgets to form layout
        self.form_layout.addRow(product_type_label, self.product_type)
        self.form_layout.addRow(name_label, self.name_entry)
        self.form_layout.addRow(color_label, self.color_entry)
        self.form_layout.addRow(brand_label, self.brand_entry)
        self.form_layout.addRow(stock_code_label, self.stock_code_entry)
        self.form_layout.addRow(date_label, self.date_entry)
        self.form_layout.addRow(stock_amount_label, self.stock_amount_entry)
        self.form_layout.addRow(size_label, self.size_entry)
        self.form_layout.addRow(height_label, self.height_entry)
        self.form_layout.addRow(type_label, self.type_entry)

        self.add_button = QPushButton("Ürün Ekle")
        self.add_button.clicked.connect(self.add_product)
        self.add_button.setStyleSheet(label_style)

        self.form_layout.addWidget(self.add_button)
        self.layout.addLayout(self.form_layout)

        # Product listing section
        self.table = QTableWidget()
        self.table.setColumnCount(9)
        self.table.setHorizontalHeaderLabels(["Ürün Adı", "Renk", "Marka", "Stok Kodu", "Tarih", "Stok Miktarı", "Boyut","Uzunluk","Tür"])
        # Başlıkları kalın yapmak için stil ayarları
        header = self.table.horizontalHeader()
        header.setStyleSheet("font-weight: bold;")
        self.layout.addWidget(self.table)

        self.update_button = QPushButton("Ürünleri Listele")
        self.update_button.clicked.connect(self.update_table)
        self.layout.addWidget(self.update_button)
        self.update_button.setStyleSheet(label_style)

    def on_product_type_changed(self, index):
        product_type = self.product_type.currentText()
        self.type_entry.setVisible(product_type == "Canta")
        self.size_entry.setVisible(product_type == "Bavul")
        self.height_entry.setVisible(product_type == "Kemer")
    def add_product(self):
        product_type = self.product_type.currentText()
        name = self.name_entry.text()
        color = self.color_entry.currentText()
        brand = self.brand_entry.currentText()
        stock_code = self.stock_code_entry.text()
        date = self.date_entry.text()
        try:
            stock_amount = int(self.stock_amount_entry.text())
        except ValueError:
            QMessageBox.warning(self, "Hata", "Stok Miktarı geçerli bir sayı olmalıdır!")
            return

        size = self.size_entry.currentText() if product_type == "Bavul" else None
        height = self.height_entry.text() if product_type == "Kemer" else None
        type_ = self.type_entry.currentText() if product_type == "Canta" else None

        if product_type == "Bavul":
            product = Bavul(name, color, brand, stock_code, date, stock_amount, size)
        elif product_type == "Cuzdan":
            product = Cuzdan(name, color, brand, stock_code, date, stock_amount)
        elif product_type == "Kemer":
            product = Kemer(name, color, brand, stock_code, date, stock_amount, height)
        elif product_type == "Canta":
            product = Canta(name, color, brand, stock_code, date, stock_amount, type_)
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

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = StockManagerApp()
    window.show()
    sys.exit(app.exec_())
