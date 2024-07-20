import inquirer
import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

catalog_ids = [
    17901274960, 17900412562, 18101120017, 18101787305, 17900817639,
    18100795481, 18102096668, 17900973647, 18100314801, 18100566475,
    18100228850, 17900918599, 17901519302, 18100145664, 18100143127,
    18100348824, 18100716346, 18100522261, 18100359435, 18100760548,
    18100881047, 18100160879, 18100931556, 18100684824, 17900992310,
    18100802382, 18101292674, 17901469198, 17901476467, 18101102133,
    18101095928
]

def check_catalog_ids(catalog_ids):
    on_sale_ids = []

    chrome_options = Options()
    chrome_options.add_argument("--headless")  
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--disable-infobars")
    chrome_options.add_argument("--window-size=1920,1080")
    chrome_options.add_argument("--log-level=3")
    chrome_options.add_experimental_option('excludeSwitches', ['enable-logging', 'enable-automation'])
    chrome_options.add_experimental_option('useAutomationExtension', False)

    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)

    for catalog_id in catalog_ids:
        try:
            url = f"https://www.roblox.com/catalog/{catalog_id}"
            driver.get(url)
            time.sleep(2)  

            buy_button = driver.find_elements(By.CLASS_NAME, "shopping-cart-buy-button")
            buy_button_alt = driver.find_elements(By.CLASS_NAME, "PurchaseButton")

            if buy_button or buy_button_alt:
                print(f"Catalog ID {catalog_id} is on sale.")
                on_sale_ids.append(catalog_id)
            else:
                print(f"Catalog ID {catalog_id} is not on sale.")
        except Exception as e:
            print(f"Failed to retrieve data for Catalog ID {catalog_id}. Error: {str(e)}")

    driver.quit()
    return on_sale_ids

def main_menu():
    questions = [
        inquirer.List('action',
                      message="Welcome to Marcelos RBLXID checker choose somthing fag?",
                      choices=['Check Predefined Catalog IDs', 'Input Raw Catalog IDs', 'Exit'])
    ]
    answers = inquirer.prompt(questions)

    if answers['action'] == 'Check Predefined Catalog IDs':
        on_sale_ids = check_catalog_ids(catalog_ids)
    elif answers['action'] == 'Input Raw Catalog IDs':
        raw_ids = inquirer.text(message="Enter catalog IDs separated by spaces:")
        if raw_ids:
            try:
                raw_ids_list = [int(id.strip()) for id in raw_ids.split()]
                on_sale_ids = check_catalog_ids(raw_ids_list)
            except ValueError:
                print("Invalid catalog ID format. Please enter only numbers separated by spaces.")
                return
    elif answers['action'] == 'Exit':
        print("Goodbye!")
        exit()

    if on_sale_ids:
        print("The following catalog IDs are on sale:")
        for id in on_sale_ids:
            print(f"Catalog ID: {id}")
    else:
        print("None of the catalog IDs are on sale womp womp.")

    input("Press any key to continue...")

if __name__ == "__main__":
    os.system('')
    main_menu()
