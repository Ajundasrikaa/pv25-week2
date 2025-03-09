from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QLineEdit, QRadioButton, QComboBox, QGroupBox, QFormLayout
import sys

class RegistrationForm(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        self.setStyleSheet("""
            QLineEdit {
                border: 2px solid #ccc;
                border-radius: 5px;
                padding: 5px;
                font-size: 14px;
            }
            QLineEdit:focus {
                border: 2px solid #0078D7;
                background-color: #f0f8ff;
            }
            QPushButton {
                background-color: #0078D7;
                color: white;
                border-radius: 5px;
                padding: 8px;
                font-size: 14px;
            }
            QPushButton:hover {
                background-color: #005bb5;
            }
        """)

        main_layout = QVBoxLayout()
        
        identity_group = QGroupBox("Identitas (vertical box layout)")
        identity_layout = QVBoxLayout()
        identity_layout.addWidget(QLabel("Nama : Ajundasrika Anugrahanti TS"))
        identity_layout.addWidget(QLabel("Nim : F1D022108"))
        identity_layout.addWidget(QLabel("Kelas : D"))
        identity_group.setLayout(identity_layout)
        main_layout.addWidget(identity_group)
        
        nav_group = QGroupBox("Navigation (horizontal box layout)")
        nav_layout = QHBoxLayout()
        nav_layout.addWidget(QPushButton("Home"))
        nav_layout.addWidget(QPushButton("About"))
        nav_layout.addWidget(QPushButton("Contact"))
        nav_group.setLayout(nav_layout)
        main_layout.addWidget(nav_group)
        
        form_group = QGroupBox("User Registration (form layout)")
        form_layout = QFormLayout()
        form_layout.setHorizontalSpacing(20)
        
        form_layout.addRow(QLabel("Full Name:"), QLineEdit())
        form_layout.addRow(QLabel("Email:"), QLineEdit())
        form_layout.addRow(QLabel("Phone:"), QLineEdit())
        
        gender_layout = QHBoxLayout()
        gender_layout.addWidget(QRadioButton("Male"))
        gender_layout.addWidget(QRadioButton("Female"))
        form_layout.addRow(QLabel("Gender:"), gender_layout)
        
        country_box = QComboBox()
        country_box.addItems(["Select", "USA", "UK", "India", "Indonesia"])
        form_layout.addRow(QLabel("Country:"), country_box)
        
        form_group.setLayout(form_layout)
        main_layout.addWidget(form_group)
        
        action_group = QGroupBox("Actions (horizontal box layout)")
        action_layout = QHBoxLayout()
        action_layout.addWidget(QPushButton("Submit"))
        action_layout.addWidget(QPushButton("Cancel"))
        action_group.setLayout(action_layout)
        main_layout.addWidget(action_group)
        
        self.setLayout(main_layout)
        self.setWindowTitle("Week 2 : Layout - User Registration Form")
        self.resize(400, 300)
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = RegistrationForm()
    form.show()
    sys.exit(app.exec_())
