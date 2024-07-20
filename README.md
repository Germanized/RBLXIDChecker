checks raw roblox item ids to see if they are onsale bassically
## Checker.py code with module checker
import subprocess
import sys
import os
import time

required_modules = [
    "requests",
    "webbrowser",
    "inquirer"
]

def check_and_install_modules(modules):
    for module in modules:
        try:
            __import__(module)
            print(f"Module {module} is already installed.")
        except ImportError:
            print(f"Module {module} not found. Installing...")
            subprocess.check_call([sys.executable, "-m", "pip", "install", module])
            print(f"Module {module} installed successfully.")

check_and_install_modules(required_modules)

import requests
import webbrowser
import inquirer
import ctypes

catalog_ids = [
    17901274960, 17900412562, 18101120017, 18101787305, 17900817639,
    18100795481, 18102096668, 17900973647, 18100314801, 18100566475,
    18100228850, 17900918599, 17901519302, 18100145664, 18100143127,
    18100348824, 18100716346, 18100522261, 18100359435, 18100760548,
    18100881047, 18100160879, 18100931556, 18100684824, 17900992310,
    18100802382, 18101292674, 17901469198, 17901476467, 18101102133,
    18101095928
]

def set_console_title(title):
    ctypes.windll.kernel32.SetConsoleTitleW(title)

def typewriter_title_animation(title, delay=0.1):
    for i in range(len(title) + 1):
        set_console_title(title[:i])
        time.sleep(delay)
    time.sleep(1)
    for i in range(len(title) + 1):
        set_console_title(title[:len(title)-i])
        time.sleep(delay)
    set_console_title("")  

def check_catalog_ids(catalog_ids):
    for catalog_id in catalog_ids:
        url = f"https://economy.roblox.com/v1/assets/{catalog_id}/resale-data"
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            if data.get('assetResalePrices'):
                print(f"Catalog ID {catalog_id} is on sale.")
                webbrowser.open(f"https://www.roblox.com/catalog/{catalog_id}")
            else:
                print(f"Catalog ID {catalog_id} is not on sale.")
        else:
            print(f"Failed to retrieve data for Catalog ID {catalog_id}. Status code: {response.status_code}")

def main_menu():
    questions = [
        inquirer.List('action',
                      message="What would you like to do?",
                      choices=['Check Predefined Catalog IDs', 'Input Raw Catalog IDs', 'Exit'])
    ]
    answers = inquirer.prompt(questions)

    if answers['action'] == 'Check Predefined Catalog IDs':
        check_catalog_ids(catalog_ids)
    elif answers['action'] == 'Input Raw Catalog IDs':
        raw_ids = inquirer.text(message="Enter catalog IDs separated by spaces:")
        if raw_ids:
            raw_ids_list = [int(id.strip()) for id in raw_ids.split()]
            check_catalog_ids(raw_ids_list)
    elif answers['action'] == 'Exit':
        print("Goodbye!")
        exit()

if __name__ == "__main__":
    os.system('')  
    typewriter_title_animation("RBLXID onsale checker by Marcelo", delay=0.1)
    main_menu()
## Checker.pyw gui version no module checker code
import sys
import requests
import webbrowser
from PyQt5 import QtCore, QtGui, QtWidgets

class Worker(QtCore.QThread):
    output_signal = QtCore.pyqtSignal(str)
    finished_signal = QtCore.pyqtSignal()

    def __init__(self, catalog_ids):
        super().__init__()
        self.catalog_ids = catalog_ids

    def run(self):
        for catalog_id in self.catalog_ids:
            url = f"https://economy.roblox.com/v1/assets/{catalog_id}/resale-data"
            try:
                response = requests.get(url)
                if response.status_code == 200:
                    data = response.json()
                    if data.get('assetResalePrices'):
                        message = f"Catalog ID {catalog_id} is on sale."
                        self.output_signal.emit(message)
                        webbrowser.open(f"https://www.roblox.com/catalog/{catalog_id}")
                    else:
                        message = f"Catalog ID {catalog_id} is not on sale."
                        self.output_signal.emit(message)
                else:
                    message = f"Failed to retrieve data for Catalog ID {catalog_id}. Status code: {response.status_code}"
                    self.output_signal.emit(message)
            except requests.RequestException as e:
                message = f"An error occurred: {e}"
                self.output_signal.emit(message)
        self.finished_signal.emit()

class CatalogChecker(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle("RBLXID Onsale Checker by Marcelo")
        self.setGeometry(100, 100, 600, 400)  

        self.setStyleSheet("""
            QWidget {
                background-color: #2e2e2e;
                color: #ffffff;
                font-family: Arial, sans-serif;
            }
            QPushButton {
                background-color: #555555;
                border-radius: 10px;
                padding: 10px;
            }
            QPushButton:hover {
                background-color: #777777;
            }
            QLineEdit {
                background-color: #444444;
                border-radius: 10px;
                padding: 10px;
            }
            QLabel {
                font-size: 14px;
            }
            QTextEdit {
                background-color: #333333;
                border-radius: 10px;
                padding: 10px;
                font-size: 12px;
                color: #ffffff;
                selection-background-color: #555555;
            }
            QTabWidget::pane {
                border: none;
                background-color: #2e2e2e;
            }
            QTabBar::tab {
                background-color: #444444;
                border: 1px solid #555555;
                border-radius: 10px;
                padding: 10px;
            }
            QTabBar::tab:selected {
                background-color: #555555;
                color: #ffffff;
            }
            QTabBar::tab:last {
                margin-right: 0;
            }
        """)

        layout = QtWidgets.QVBoxLayout()

        self.tabs = QtWidgets.QTabWidget()
        self.tabs.addTab(self.createMainTab(), "Main")
        self.tabs.addTab(self.createCreditsTab(), "Credits")
        layout.addWidget(self.tabs)

        self.setLayout(layout)

    def createMainTab(self):
        mainTab = QtWidgets.QWidget()
        mainLayout = QtWidgets.QVBoxLayout()

        self.titleLabel = QtWidgets.QLabel("RBLXID Onsale Checker")
        self.titleLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.titleLabel.setStyleSheet("font-size: 18px; font-weight: bold;")
        mainLayout.addWidget(self.titleLabel)

        self.checkPredefinedBtn = QtWidgets.QPushButton("Check Predefined Catalog IDs")
        self.checkPredefinedBtn.clicked.connect(self.check_predefined_catalog_ids)
        mainLayout.addWidget(self.checkPredefinedBtn)

        self.rawCatalogInput = QtWidgets.QLineEdit()
        self.rawCatalogInput.setPlaceholderText("Enter catalog IDs separated by spaces...")
        mainLayout.addWidget(self.rawCatalogInput)

        self.checkRawBtn = QtWidgets.QPushButton("Check Raw Catalog IDs")
        self.checkRawBtn.clicked.connect(self.check_raw_catalog_ids)
        mainLayout.addWidget(self.checkRawBtn)

        self.exitBtn = QtWidgets.QPushButton("Exit")
        self.exitBtn.clicked.connect(self.close)
        mainLayout.addWidget(self.exitBtn)

        self.outputTextEdit = QtWidgets.QTextEdit()
        self.outputTextEdit.setReadOnly(True)
        mainLayout.addWidget(self.outputTextEdit)

        mainTab.setLayout(mainLayout)
        return mainTab

    def createCreditsTab(self):
        creditsTab = QtWidgets.QWidget()
        creditsLayout = QtWidgets.QVBoxLayout()

        creditsLabel = QtWidgets.QLabel("Credits")
        creditsLabel.setAlignment(QtCore.Qt.AlignCenter)
        creditsLabel.setStyleSheet("font-size: 18px; font-weight: bold;")
        creditsLayout.addWidget(creditsLabel)

        creditsText = QtWidgets.QLabel("Created by Marcelo")
        creditsText.setAlignment(QtCore.Qt.AlignCenter)
        creditsLayout.addWidget(creditsText)

        creditsTab.setLayout(creditsLayout)
        return creditsTab

    def append_output(self, message):
        self.outputTextEdit.append(message)

    def check_predefined_catalog_ids(self):
        catalog_ids = [
            17901274960, 17900412562, 18101120017, 18101787305, 17900817639,
            18100795481, 18102096668, 17900973647, 18100314801, 18100566475,
            18100228850, 17900918599, 17901519302, 18100145664, 18100143127,
            18100348824, 18100716346, 18100522261, 18100359435, 18100760548,
            18100881047, 18100160879, 18100931556, 18100684824, 17900992310,
            18100802382, 18101292674, 17901469198, 17901476467, 18101102133,
            18101095928
        ]
        self.start_worker(catalog_ids)

    def check_raw_catalog_ids(self):
        raw_ids = self.rawCatalogInput.text()
        if raw_ids:
            try:
                raw_ids_list = [int(id.strip()) for id in raw_ids.split()]
                self.start_worker(raw_ids_list)
            except ValueError:
                self.append_output("Please enter valid catalog IDs.")

    def start_worker(self, catalog_ids):
        self.worker = Worker(catalog_ids)
        self.worker.output_signal.connect(self.append_output)
        self.worker.finished_signal.connect(self.on_worker_finished)
        self.worker.start()

    def on_worker_finished(self):
        self.append_output("Finished checking all catalog IDs.")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = CatalogChecker()
    window.show()
    sys.exit(app.exec_())
