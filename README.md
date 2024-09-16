# Instagram Non-Followers Scraper

Hi there! This script provides a simple (and somewhat foolproof) way to generate a list of everyone who doesn’t follow you back on Instagram.

## Instructions

To run this script, follow these steps:

1. **Install the Required Software**
   - Please refer to the 'THINGS TO INSTALL' section above.

2. **Prepare the Script**
   - Paste the code from `instagram_script.py` into your preferred code editor (e.g., VSCode).

3. **Modify the Script**
   - Update the script by replacing all instances of `'your_username'` with your actual Instagram username.
   - Replace `'your_password'` with your actual Instagram password.

4. **Run the Script**
   - Type 'Chromedriver' into your terminal 
   - You should get a message saying something like 'ChromeDriver was started successfully on port....'
   - Execute the script. A WebDriver window will open and automatically log in to your Instagram account.

5. **Navigate to Your Profile**
   - After logging in, the script will redirect you to your Instagram profile page.

6. **Scrape Followers**
   - The script will open the list of followers. **INPUT REQUIRED:** Scroll to the bottom of your followers list, then press the 'Enter' key in the terminal where the script is running. Scroll back up when done.

7. **Stop the Followers Scraping**
   - Type `'stop'` in the terminal to end the followers scraping.

8. **Scrape Following**
   - The script will then open the list of accounts you are following. **INPUT REQUIRED:** Scroll to the bottom of your following list, then press the 'Enter' key in the terminal. Scroll back up when done.

9. **Stop the Following Scraping**
   - Type `'stop'` in the terminal to end the following scraping.

10. **Retrieve Results**
    - The list of non-followers, along with your followers and following lists, will be saved as CSV files in the same folder as `instagram_script.py`.

