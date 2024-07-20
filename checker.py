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
