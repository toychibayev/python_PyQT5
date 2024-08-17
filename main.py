from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QComboBox, QLineEdit, QRadioButton, QSpinBox, QCheckBox
from PyQt5.QtGui import QFont
from os import system

system("cls")

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Foydalanuvchi Ma'lumotlari")
        self.setGeometry(100, 50, 500, 500)
        self.setStyleSheet("background-color: #e0f7fa;")

        
        label_font = QFont("Arial", 14)
        input_font = QFont("Arial", 12)
        
        
        self.label = QLabel("Ism:", self)
        self.label.setFont(label_font)
        self.label.setStyleSheet("color: #00796b;")  # Matn rangi
        self.label.move(20, 20)

        self.nameInput = QLineEdit(self)
        self.nameInput.setFont(input_font)
        self.nameInput.setFixedSize(250, 30)
        self.nameInput.setPlaceholderText("Ismingizni kiriting...")
        self.nameInput.setStyleSheet("""
            border-radius: 5px;
            padding: 5px;
            border: 1px solid #004d40;
            background-color: #ffffff;
            color: #004d40;  
        """)
        self.nameInput.move(180, 20)

        
        self.label = QLabel("Familiya:", self)
        self.label.setFont(label_font)
        self.label.setStyleSheet("color: #00796b;")
        self.label.move(20, 70)

        self.FamiliyaInput = QLineEdit(self)
        self.FamiliyaInput.setFont(input_font)
        self.FamiliyaInput.setFixedSize(250, 30)
        self.FamiliyaInput.setPlaceholderText("Familiyangizni kiriting...")
        self.FamiliyaInput.setStyleSheet("""
            border-radius: 5px;
            padding: 5px;
            border: 1px solid #004d40;
            background-color: #ffffff;
            color: #004d40;
        """)
        self.FamiliyaInput.move(180, 70)

        
        self.label = QLabel("Jins:", self)
        self.label.setFont(label_font)
        self.label.setStyleSheet("color: #00796b;")
        self.label.move(20, 120)

        self.erkakRB = QRadioButton("Erkak", self)
        self.erkakRB.setFont(input_font)
        self.erkakRB.setStyleSheet("font-size: 14px; color: #004d40;")
        self.erkakRB.move(180, 120)

        self.ayolRB = QRadioButton("Ayol", self)
        self.ayolRB.setFont(input_font)
        self.ayolRB.setStyleSheet("font-size: 14px; color: #004d40;")
        self.ayolRB.move(250, 120)

        
        self.label = QLabel("Bo'y:", self)
        self.label.setFont(label_font)
        self.label.setStyleSheet("color: #00796b;")
        self.label.move(20, 170)

        self.boy1 = QCheckBox("150-160", self)
        self.boy1.setFont(input_font)
        self.boy1.setStyleSheet("font-size: 14px; color: #004d40;")
        self.boy1.move(180, 170)

        self.boy2 = QCheckBox("170-190", self)
        self.boy2.setFont(input_font)
        self.boy2.setStyleSheet("font-size: 14px; color: #004d40;")
        self.boy2.move(260, 170)

        self.boy3 = QCheckBox("200+", self)
        self.boy3.setFont(input_font)
        self.boy3.setStyleSheet("font-size: 14px; color: #004d40;")
        self.boy3.move(340, 170)

        
        self.label = QLabel("Yoshingiz:", self)
        self.label.setFont(label_font)
        self.label.setStyleSheet("color: #00796b;")
        self.label.move(20, 220)

        self.spin_box = QSpinBox(self)
        self.spin_box.setFont(input_font)
        self.spin_box.setMinimum(0)
        self.spin_box.setMaximum(100)
        self.spin_box.setSingleStep(1)
        self.spin_box.setFixedSize(100, 30)
        self.spin_box.setStyleSheet("""
            border-radius: 5px;
            padding: 5px;
            border: 1px solid #004d40;
            background-color: #ffffff;
            color: #004d40;
        """)
        self.spin_box.move(180, 220)

        
        self.label = QLabel("Millatingiz:", self)
        self.label.setFont(label_font)
        self.label.setStyleSheet("color: #00796b;")
        self.label.move(20, 270)

        self.comboBox = QComboBox(self)
        self.comboBox.setFont(input_font)
        self.comboBox.setFixedSize(150, 30)
        self.comboBox.setStyleSheet("""
            border-radius: 5px;
            padding: 5px;
            border: 1px solid #004d40;
            background-color: #ffffff;
            color: #004d40;
        """)
        self.comboBox.move(180, 270)

        self.comboBox.addItem("---")
        self.comboBox.addItem("Uzbekistan")
        self.comboBox.addItem("Russia")
        self.comboBox.addItem("USA")
        self.comboBox.addItem("Tadjikistan")
        self.comboBox.addItem("Spain")
        self.comboBox.currentIndexChanged.connect(self.updateRegions)

        
        self.label = QLabel("Viloyatlaringiz:", self)
        self.label.setFont(label_font)
        self.label.setStyleSheet("color: #00796b;")
        self.label.move(20, 320)

        self.regionComboBox = QComboBox(self)
        self.regionComboBox.setFont(input_font)
        self.regionComboBox.setFixedSize(150, 30)
        self.regionComboBox.setStyleSheet("""
            border-radius: 5px;
            padding: 5px;
            border: 1px solid #004d40;
            background-color: #ffffff;
            color: #004d40;
        """)
        self.regionComboBox.move(180, 320)

    def updateRegions(self, index):
        self.regionComboBox.clear()
        if index == 1:  
            self.regionComboBox.addItems(["Tashkent", "Navoiy", "Jizzax", "Samarqand", "Andijon", "Namangan", "Buxoro"])
        elif index == 2: 
            self.regionComboBox.addItems(["Moscow", "Saint Petersburg", "Kazan", "Novosibirsk"])
        elif index == 3: 
            self.regionComboBox.addItems(["New York", "California", "Texas", "Florida"])
        elif index == 4:  
            self.regionComboBox.addItems(["Dushanbe", "Khujand", "Kulob", "Qurghonteppa"])
        elif index == 5:  
            self.regionComboBox.addItems(["Madrid", "Barcelona", "Valencia", "Seville"])

app = QApplication([])
oyna = Window()
oyna.show()
app.exec()
