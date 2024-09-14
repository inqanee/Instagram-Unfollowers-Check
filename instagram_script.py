from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time
import os

def get_names_from_elements(elements):
    """Helper function to extract names from elements."""
    names = []
    for element in elements:
        name = element.text
        if name and name not in names:
            names.append(name)
    return names

def wait_for_input(prompt):
    """Helper function to wait for user input."""
    input(prompt)
    return

print("Initializing WebDriver...")
# Initialize WebDriver
driver = webdriver.Chrome()  # or webdriver.Firefox() for Firefox
print("WebDriver initialized.")

print("Opening Instagram login page...")
# Open Instagram
driver.get("https://www.instagram.com/accounts/login/")

print("Waiting for login page to load...")
time.sleep(2)  # Wait for the page to load

print("Logging in...")
# Login
username = driver.find_element(By.NAME, 'username')
password = driver.find_element(By.NAME, 'password')
username.send_keys('your_username')  # Replace with your Instagram username
password.send_keys('your_password')  # Replace with your Instagram password
password.send_keys(Keys.RETURN)
time.sleep(5)  # Wait for login to complete
print("Logged in.")

print("Navigating to profile...")
# Navigate to your profile
driver.get("https://www.instagram.com/your_username/")  # Replace 'inqanee' with your actual Instagram username
time.sleep(2)

print("Opening Followers List...")
# Open Followers List
followers_link = driver.find_element(By.XPATH, '//a[contains(@href,"/followers/")]')
followers_link.click()
time.sleep(2)

print("Scraping Followers...")
# Scrape Followers
followers = []

print("Scroll through the followers list and press Enter when ready to start reading names.")
wait_for_input("Press Enter to start reading followers...")

while True:
    elements = driver.find_elements(By.XPATH, '//a[contains(@href, "/")]')
    followers += get_names_from_elements(elements)
    if input("Type 'stop' to end reading followers or press Enter to continue...").strip().lower() == 'stop':
        break

print(f"Finished scraping followers. Total followers scraped: {len(followers)}")

print("Saving Followers to CSV...")
# Save Followers to CSV
pd.DataFrame(followers, columns=['Follower']).to_csv('followers.csv', index=False)
print("Followers saved to followers.csv.")

print("Going back to profile page...")
# Go back to the profile page and open Following List
driver.get("https://www.instagram.com/your_username/")
time.sleep(2)

print("Opening Following List...")
following_link = driver.find_element(By.XPATH, '//a[contains(@href,"/following/")]')
following_link.click()
time.sleep(2)

print("Scraping Following...")
# Scrape Following
following = []

print("Scroll through the following list and press Enter when ready to start reading names.")
wait_for_input("Press Enter to start reading following...")

while True:
    elements = driver.find_elements(By.XPATH, '//a[contains(@href, "/")]')
    following += get_names_from_elements(elements)
    if input("Type 'stop' to end reading following or press Enter to continue...").strip().lower() == 'stop':
        break

print(f"Finished scraping following. Total following scraped: {len(following)}")

print("Saving Following to CSV...")
# Save Following to CSV
pd.DataFrame(following, columns=['Following']).to_csv('following.csv', index=False)
print("Following saved to following.csv.")

print("Comparing Lists...")
# Compare Lists
followers_set = set(followers)
following_set = set(following)
not_in_followers = following_set - followers_set

print("Saving the difference to CSV...")
# Save the difference to CSV
pd.DataFrame(list(not_in_followers), columns=['Not in Followers']).to_csv('not_in_followers.csv', index=False)
print("Differences saved to not_in_followers.csv.")

print("Closing WebDriver...")
# Close WebDriver
driver.quit()
print("WebDriver closed.")
