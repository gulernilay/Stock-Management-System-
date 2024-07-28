import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QFormLayout, QLabel, QLineEdit, QPushButton, QWidget
from pymongo import MongoClient

class LoginWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # MongoDB bağlantısı ve koleksiyon seçimi
        self.client = MongoClient('mongodb://localhost:27017/')
        self.db = self.client['gokhancanta']  # MongoDB veritabanı adı
        self.collection = self.db['Kullanıcılar']  # MongoDB koleksiyon adı
        
        # UI bileşenleri
        self.form_widget = QWidget()
        self.setCentralWidget(self.form_widget)
        self.form_layout = QFormLayout()

        # Kullanıcı adı ve şifre giriş alanları
        self.username_entry = QLineEdit()
        self.password_entry = QLineEdit()
        self.password_entry.setEchoMode(QLineEdit.Password)

        # Etiketlerin stilini ayarla
        label_style = "font-weight: bold; color: black; font-size: 14px"
        self.form_layout.addRow(QLabel("Kullanıcı Adı:"), self.username_entry)
        self.form_layout.addRow(QLabel("Şifre:"), self.password_entry)
        self.form_layout.itemAt(0, QFormLayout.LabelRole).widget().setStyleSheet(label_style)
        self.form_layout.itemAt(1, QFormLayout.LabelRole).widget().setStyleSheet(label_style)

        # Giriş butonunu ekle ve stil ayarlarını yap
        self.login_button = QPushButton("GİRİŞ")
        self.login_button.setFixedWidth(100)  # Buton genişliğini ayarla
        self.login_button.setStyleSheet("font-weight: bold; color: black; border: 2px solid black;")
        self.login_button.clicked.connect(self.login)
        self.form_layout.addWidget(self.login_button)

        self.form_widget.setLayout(self.form_layout)

    def login(self):
        username = self.username_entry.text()
        password = self.password_entry.text()

        # Kullanıcı adı ve şifre sorgusu
        query = {"username": username, "password": password}
        user = self.collection.find_one(query)

        if user:
            print("Giriş başarılı")
            # Burada başarılı giriş sonrası yapılacak işlemler
        else:
            print("Kullanıcı adı veya şifre hatalı")

    def closeEvent(self, event):
        self.client.close()  # Uygulama kapanırken MongoDB bağlantısını kapat
        event.accept()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LoginWindow()
    window.show()
    sys.exit(app.exec_())
