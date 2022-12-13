# Import the necessary modules
from selenium import webdriver
from selenium.webdriver.common.by import By
import random
import time

# Keep open after execution
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
# chrome_options.add_experimental_option("detach", True)
chrome_options.headless = True

# Open Safari and navigate to the Google website
driver = webdriver.Chrome('drivers/chromedriver.exe', chrome_options=chrome_options)
driver.get('https://got.gtarcade.com')

# Locate the search box on the page and enter the search term
login_email = driver.find_element(By.NAME, 'integration_game_login_email')
login_password = driver.find_element(By.NAME, 'password')
button = driver.find_element(By.ID, 'integration_game_login_header')

# Login details
username = ""
password = ""

# Login
login_email.send_keys(username)
login_password.send_keys(password)
driver.execute_script("arguments[0].click();", button)

# Join battle
button2= driver.find_element('id', 'joinBtn')
driver.execute_script("arguments[0].click();", button2)

# Sleep for 1.5 to 2.0 min
rint = random.randint(90, 120)
print(f"Going to sleep for {rint} s")
time.sleep(rint)

# Print
print(f"Done for user: {username}")
