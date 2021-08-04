from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from pathlib import Path
import pprint

from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver

# In order for ChromeDriverManager to work you must pip install it in your own environment.
driver = webdriver.Chrome(ChromeDriverManager().install())

url = "https://witty-hill-0acfceb03.azurestaticapps.net/film_register.html"

try:
    driver.get(url)
    # film_list = driver.find_elements_by_tag_name('body > div.container > div.container-total > a')
    # film = driver.find_elements_by_link_text('container-movies')
    # / html / body / div[2] / div[3] / a[3] / div
    f = driver.find_elements_by_xpath('//div/div/a/div[@class="container-movies"]')
    vmi = string(//div/div/a/div/@class)
    print(f)
    print(type(f))
    print(len(f))
    #print(f[0].get_attribute(class))
finally:
    pass
