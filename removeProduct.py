import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel,QHBoxLayout, QLineEdit, QPushButton, QFormLayout, QMessageBox, QComboBox, QTableWidget, QTableWidgetItem
from PyQt5.QtCore import Qt
from Product import Bavul, Cuzdan, Kemer, Canta
from Stock import Stock

class RemoveProduct(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        # Stok yönetim sistemini oluşturuyoruz
        self.stock = Stock()

        # Ana pencere ayarları
        self.setWindowTitle("GÖKHAN ÇANTA STOK KONTROL YÖNETİM SİSTEMİ")
        self.setGeometry(100, 100, 800, 600)
        self.setStyleSheet("background-color:#E6E6FA;")

        # Merkez widget ve layout
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)

        # Create horizontal layout for the title and back button
        self.header_layout = QHBoxLayout()
        
        # Title label
        self.title_label = QLabel("Ürün Silme Ekranı")
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

        # Ürün ekleme bölümü
        self.form_layout = QFormLayout()

        # Ürün türü combobox ve etiketi
        self.product_type = QComboBox()
        self.product_type.addItems(["Bavul", "Cuzdan", "Kemer", "Canta"])
        self.product_type_label = QLabel("Ürün Türü:")
        self.product_type_label.setStyleSheet("font-weight: bold;")
        self.form_layout.addRow(self.product_type_label, self.product_type)

        # Diğer etiketler ve giriş alanları
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
        #self.date_entry = QLineEdit()
        #self.stock_amount_entry = QLineEdit()
        #self.size_entry = QLineEdit()
        #self.height_entry = QLineEdit()
        #self.type_entry = QLineEdit()

        self.name_label = QLabel("Ürün Adı:")
        self.color_label = QLabel("Renk:")
        self.brand_label = QLabel("Marka:")
        self.stock_code_label = QLabel("Stok Kodu:")
        #self.date_label = QLabel("Tarih:")
        #self.stock_amount_label = QLabel("Stok Miktarı:")
        #self.size_label = QLabel("Boyut (Sadece Bavul için):")
        #self.height_label = QLabel("Yükseklik (Sadece Kemer için):")
        #self.type_label = QLabel("Tür (Sadece Çanta için):")

        # Etiketleri kalın yapma
        labels = [self.name_label, self.color_label, self.brand_label, self.stock_code_label]
        for label in labels:
            label.setStyleSheet("font-weight: bold;")

        # Form layout'a etiketleri ve giriş alanlarını ekleme
        self.form_layout.addRow(self.name_label, self.name_entry)
        self.form_layout.addRow(self.color_label, self.color_entry)
        self.form_layout.addRow(self.brand_label, self.brand_entry)
        self.form_layout.addRow(self.stock_code_label, self.stock_code_entry)
        #self.form_layout.addRow(self.date_label, self.date_entry)
        #self.form_layout.addRow(self.stock_amount_label, self.stock_amount_entry)
        #self.form_layout.addRow(self.size_label, self.size_entry)
        #self.form_layout.addRow(self.height_label, self.height_entry)
        #self.form_layout.addRow(self.type_label, self.type_entry)

        self.layout.addLayout(self.form_layout)

        # Ürün listeleme bölümü
        self.table = QTableWidget()
        self.table.setColumnCount(10)
        self.table.setHorizontalHeaderLabels(["Ürün Adı", "Renk", "Marka", "Stok Kodu", "Stok Miktarı", "Boyut(Bavul)","Uzunluk(Kemer)","Tür(Çanta)","Azalan Miktar","İşlem Tarihi"])
        # Başlıkları kalın yapmak için stil ayarları
        header = self.table.horizontalHeader()
        header.setStyleSheet("font-weight: bold;")
        self.layout.addWidget(self.table)

        self.update_button = QPushButton("Ürün Bul")
        self.update_button.clicked.connect(self.update_table)
        self.update_button.setStyleSheet("font-weight: bold;")
        self.layout.addWidget(self.update_button)
        

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
                self.table.setItem(row_position, 7, QTableWidgetItem(product.type))

    def go_back(self):
        from MainPage2 import MainApp  # Import inside the function
        self.main_app = MainApp()  # Initialize the MainApp class
        self.main_app.show()
        self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = RemoveProduct()
    window.show()
    sys.exit(app.exec_())
