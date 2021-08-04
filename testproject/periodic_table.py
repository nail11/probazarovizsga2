from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from pathlib import  Path
import pprint


from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
# In order for ChromeDriverManager to work you must pip install it in your own environment.
driver = webdriver.Chrome(ChromeDriverManager().install())

url = "https://witty-hill-0acfceb03.azurestaticapps.net/periodic_table.html"

try:
    driver.get(url)
finally:
    pass