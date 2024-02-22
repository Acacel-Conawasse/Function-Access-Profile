from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set the path to the GeckoDriver executable
geckodriver_path = 'C:/Users/omalomo3/Downloads/geckodriver-v0.34.0-win32/geckodriver.exe'

# Specify the path to your Firefox binary if it's not in the default location
firefox_binary_path = 'C:/Program Files/Mozilla Firefox/firefox.exe'

# Create Firefox Options
firefox_options = Options()
firefox_options.binary_location = firefox_binary_path

# Create a Service object to pass to the Firefox driver
service = Service(executable_path=geckodriver_path)

# Initialize the WebDriver for Firefox with the Service object and Firefox Options
driver = webdriver.Firefox(service=service, options=firefox_options)

# Navigate to your webpage
driver.get('https://jhmi-uat.npr.mykronos.com/capp?tenantId=jhmi_nonprd_01#/setuptools?path=%2Fwfc%2Fapplications%2Fwsaaccessprofiles%2Ffaps.do&method=doPopulate&helpId=ApplicationSetup&pageId=300')

# Wait up to 10 seconds for the "ESS Posted" link to be clickable
wait = WebDriverWait(driver, 60)
ess_posted_link = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[text()='ESS Posted']")))

# Click on the "ESS Posted" link
ess_posted_link.click()

# Continue with your automation tasks...
