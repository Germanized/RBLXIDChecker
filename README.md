# RBLXID Onsale Checker

## Overview

The **RBLXID Onsale Checker** is a Python application designed to check the sale status of Roblox catalog items. It has two versions:
1. **Command Line Interface (CLI)** - A command-line tool that checks predefined and raw catalog IDs.
2. **Graphical User Interface (GUI)** - A PyQt5-based application that provides a user-friendly interface for checking catalog IDs.

This README explains the purpose of each version and provides an overview of the code used in both implementations. Please note that the code is designed for educational and personal use, and is not intended for any malicious activity.

---

## CLI Version

### Purpose

The CLI version of the **RBLXID Onsale Checker** allows users to check the sale status of catalog items by entering predefined catalog IDs or raw catalog IDs through the command line.

### Code Explanation

1. **Dependencies**: 
   - `requests`: For making HTTP requests to the Roblox API.
   - `webbrowser`: For opening item URLs in the web browser.

2. **Functionality**:
   - `check_predefined_catalog_ids()`: Checks a set of predefined catalog IDs for sale status.
   - `check_raw_catalog_ids(raw_ids)`: Checks catalog IDs entered by the user.

3. **Error Handling**:
   - Handles cases where the API request fails or the catalog ID is invalid.

4. **Web Scraping**:
   - Uses the `webbrowser` module to open URLs where items are on sale.

---

## GUI Version

### Purpose

The GUI version of the **RBLXID Onsale Checker** provides a graphical interface for checking catalog item sale status. It allows users to enter catalog IDs and view results in a user-friendly format.

### Code Explanation

1. **Dependencies**:
   - `PyQt5`: For creating the graphical user interface.
   - `selenium`: For web scraping to determine if an item is on sale.
   - `webdriver_manager`: For managing the ChromeDriver.

2. **Classes**:
   - `Worker`: A background thread class that performs the web scraping task. It uses Selenium to check the sale status of catalog items.
     - **Methods**:
       - `run()`: Executes the web scraping logic and emits signals with results.
   - `CatalogChecker`: The main GUI class that creates and manages the interface.
     - **Methods**:
       - `initUI()`: Initializes the user interface elements and layout.
       - `createMainTab()`: Creates the main tab with buttons for checking catalog IDs and displaying results.
       - `createCreditsTab()`: Creates the credits tab displaying the creator's name.
       - `check_predefined_catalog_ids()`: Starts the worker to check predefined catalog IDs.
       - `check_raw_catalog_ids()`: Starts the worker to check catalog IDs entered by the user.
       - `start_worker()`: Starts the background worker for checking catalog IDs.
       - `append_output()`: Appends results to the output text area.

3. **Error Handling**:
   - Uses Selenium’s exception handling to manage errors during web scraping.
   - Displays errors and status updates in the GUI.

4. **Selenium Web Scraping**:
   - Configures ChromeDriver with headless options to run in the background.
   - Uses updated Selenium methods to find elements and check if the item is on sale.

---

## Security Note

The code is developed with the intent of providing useful functionality for users who want to check the sale status of Roblox catalog items. It is crucial to use such tools responsibly and not for any unauthorized activities. The code provided does not include any functionalities that could compromise user security or privacy.

For any questions or concerns, please feel free to reach out.

---

## Requirements

- Python 3.x
- PyQt5
- requests
- selenium
- webdriver_manager

### Installation

To install the required packages, use the following command:

```bash
pip install PyQt5 requests selenium webdriver_manager
```
## Created by Marcelo

Feel free to modify and extend the functionality as needed. Happy coding!
