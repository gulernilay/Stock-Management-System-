import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget,QHBoxLayout, QVBoxLayout, QLabel, QLineEdit, QPushButton, QFormLayout, QMessageBox,QComboBox,QTableWidget,QTableWidgetItem
from PyQt5.QtGui import QPixmap, QPalette, QBrush
from PyQt5.QtCore import Qt

from MainPage2 import MainApp
from Product import Bag, Belt, Suitcase, Wallet
from Stock import Stock

class LoginScreen(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Gökhan Çanta Stok Yönetim Sistemi")
        self.setGeometry(100, 100, 800, 600)

        # Arka plan rengini turuncu yap
        self.setStyleSheet("background-color: white;")

        # Merkez widget ve layout
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)

        # Arka plan resmini ayarla
        self.set_background_image()

        # Başlık
        self.title_label = QLabel("GÖKHAN ÇANTA STOK KONTROL YÖNETİM SİSTEMİ")
        self.title_label.setStyleSheet("font-size: 24px; font-weight: bold; color: black;")
        self.title_label.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.title_label)

        # Boş bir widget ekleyerek başlık ile form arasında boşluk bırak
        self.spacer = QWidget()
        self.spacer.setFixedHeight(50)  # Boşluğun yüksekliğini ayarlayın
        self.layout.addWidget(self.spacer)

        # Form widget'ını oluştur
        self.form_widget = QWidget()
        self.form_layout = QFormLayout()

        # Resim ekle
        self.image_label = QLabel()
        pixmap = QPixmap("C:\\Users\\nilay\\Desktop\\canta.jpeg")
        pixmap = pixmap.scaled(350, 350, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.image_label.setPixmap(pixmap)
        self.image_label.setAlignment(Qt.AlignCenter)
        self.form_layout.addRow(self.image_label)

        self.username_entry = QLineEdit()
        self.password_entry = QLineEdit()
        self.password_entry.setEchoMode(QLineEdit.Password)

        self.form_layout.addRow(QLabel("KULLANICI ADI:"), self.username_entry)
        self.form_layout.addRow(QLabel("ŞİFRE:"), self.password_entry)

        self.login_button = QPushButton("GİRİŞ")
        self.login_button.clicked.connect(self.login)
        self.form_layout.addWidget(self.login_button)

        self.form_widget.setLayout(self.form_layout)

        # Form widget'ını ortalamak için bir h-box layout kullanın
        self.form_container_layout = QHBoxLayout()
        self.form_container_layout.addWidget(self.form_widget)
        self.form_container_layout.setAlignment(Qt.AlignCenter)

        # Form container'ı ana layout'a ekleyin
        self.layout.addLayout(self.form_container_layout)

    def set_background_image(self):
        self.central_widget.setStyleSheet("background-image: url(C:\\Users\\nilay\\Desktop\\canta.jpeg); background-repeat: no-repeat; background-position: center;")

    def login(self):
        username = self.username_entry.text()
        password = self.password_entry.text()

        # Basit bir kullanıcı adı ve şifre kontrolü
        if username == "nilay" and password == "biomedicalcomputer":
            self.open_main_app()
        else:
            QMessageBox.warning(self, "Giriş Hatası", "Kullanıcı adı veya şifre yanlış!")

    def open_main_app(self):
        self.main_app = MainApp()  # Ana uygulama sınıfınızı çağırın
        self.main_app.show()
        self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    login_screen = LoginScreen()
    login_screen.show()
    sys.exit(app.exec_())




"""
birden fazla kullanıcı eklemek
database bağlantısı 
ürün ekle - stock görme ve filtreleme - ürün silme 
"""