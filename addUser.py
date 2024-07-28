from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QFormLayout, QLabel, QLineEdit, QPushButton
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from pymongo import MongoClient

class UserAddScreen(QMainWindow):
    def __init__(self):
        super().__init__()

        # MongoDB bağlantısı ve koleksiyon seçimi
        self.client = MongoClient('mongodb://localhost:27017/')
        self.db = self.client['gokhancanta']
        self.collection = self.db['Kullanıcılar']
        

        self.setWindowTitle("Kullanıcı Ekle")
        self.setGeometry(100, 100, 800, 600)

        # Arka plan rengi ve layout
        self.setStyleSheet("background-color: #D8BFD8;")
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)

        # Form
        self.form_widget = QWidget()
        self.form_layout = QFormLayout()

        # Giriş alanları
        self.name_entry = QLineEdit()
        self.username_entry = QLineEdit()
        self.password_entry = QLineEdit()
        self.password_entry.setEchoMode(QLineEdit.Password)

        # Etiketleri kalın yapma
        label_style = "font-weight: bold; color: black; font-size: 14px"

        self.title_label = QLabel("Gökhan Çanta Kullanıcı Kayıt Formu")
        self.title_label.setStyleSheet("font-size: 24px; font-weight: bold; color: black;")
        self.title_label.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.title_label)

        # Form layout'ına elemanları ekleme
        self.form_layout.addRow(QLabel("Ad - Soyad:"), self.name_entry)
        self.form_layout.addRow(QLabel("Kullanıcı Adı:"), self.username_entry)
        self.form_layout.addRow(QLabel("Şifre:"), self.password_entry)

        # Etiketleri stilize etme
        self.form_layout.itemAt(0, QFormLayout.LabelRole).widget().setStyleSheet(label_style)
        self.form_layout.itemAt(1, QFormLayout.LabelRole).widget().setStyleSheet(label_style)
        self.form_layout.itemAt(2, QFormLayout.LabelRole).widget().setStyleSheet(label_style)

        # Butonu ekleme ve stil ayarlarını yapma
        self.add_button = QPushButton("Kaydet")
        self.add_button.setStyleSheet("font-weight: bold; color: black; border: 2px solid black;")
        self.add_button.clicked.connect(self.add_user)
        self.form_layout.addWidget(self.add_button)

        self.form_widget.setLayout(self.form_layout)
        self.layout.addWidget(self.form_widget)

    def add_user(self):
        username = self.username_entry.text()
        password = self.password_entry.text()
        if username and password:
            # MongoDB'ye kullanıcı ekleme kodu
            pass

    def closeEvent(self, event):
        self.client.close()
        event.accept()

if __name__ == "__main__":
    app = QApplication([])
    window = UserAddScreen()
    window.show()
    app.exec_()
