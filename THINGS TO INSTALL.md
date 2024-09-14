This is a Selenium-based Python script, to run it on a Windows or macOS computer, you need to install and set up several components. 
Here’s a list of what you need and how to install them:

### 1. **Python**

Make sure Python is installed on your computer.

- **Windows:**
  1. Download Python from the [official Python website](https://www.python.org/downloads/).
  2. Run the installer and make sure to check the box "Add Python to PATH."

- **macOS:**
  1. You can install Python using Homebrew:
     ```bash
     brew install python
     ```

### 2. **Python Packages**

You need to install the required Python packages using `pip`.

Open a terminal (macOS) or Command Prompt (Windows) and run:

```bash
pip install selenium pandas
```

### 3. **Web Browser Driver**

This script uses the Chrome WebDriver. You need to install the corresponding WebDriver for your browser.

#### **For Google Chrome:**

- **Download ChromeDriver:**
  1. Go to https://googlechromelabs.github.io/chrome-for-testing/
  2. Download the version that matches your installed version of Google Chrome.
  3. **Extract the downloaded file.**

- **Install ChromeDriver:**
  - **Windows:**
    1. Place `chromedriver.exe` in a directory of your choice.
    2. Add the directory to your system's PATH environment variable or move `chromedriver.exe` to a directory already in PATH.

  - **macOS:**
    1. Move `chromedriver` to `/usr/local/bin`:
       ```bash
       sudo mv chromedriver /usr/local/bin/
       ```
    2. Make sure it's executable:
       ```bash
       sudo chmod +x /usr/local/bin/chromedriver
       ```

#### **For Firefox (optional):**

If you decide to use Firefox, install GeckoDriver instead:

- **Download GeckoDriver:**
  1. Go to the [GeckoDriver releases page](https://github.com/mozilla/geckodriver/releases).
  2. Download the version that matches your operating system.

- **Install GeckoDriver:**
  - **Windows:**
    1. Place `geckodriver.exe` in a directory of your choice.
    2. Add the directory to your system's PATH environment variable or move `geckodriver.exe` to a directory already in PATH.

  - **macOS:**
    1. Move `geckodriver` to `/usr/local/bin`:
       ```bash
       sudo mv geckodriver /usr/local/bin/
       ```
    2. Make sure it's executable:
       ```bash
       sudo chmod +x /usr/local/bin/geckodriver
       ```

### 4. **Verify Installation**

To verify that everything is set up correctly:

- **Check Python:**
  ```bash
  python --version
  ```
- **Check pip:**
  ```bash
  pip --version
  ```
- **Check WebDriver:**
  ```bash
  chromedriver --version
  ```

If you follow these steps and have Python, necessary packages, and WebDriver installed, you should be able to run this script successfully. If you encounter any issues, make sure to check for error messages and ensure that all paths and versions are correctly configured (or just ask ChatGPT lol).
