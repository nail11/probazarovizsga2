# environment settings
# ......................................................................

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from datetime import datetime

from selenium.webdriver.common.keys import Keys

from datetime import date
# import time
# from pathlib import Path
# import pprint


options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')

# In order for ChromeDriverManager to work you must pip install it in your own environment.

# driver = webdriver.Chrome(ChromeDriverManager().install())
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

url = "https://witty-hill-0acfceb03.azurestaticapps.net/periodic_table.html"

# variables
element_list = []
test_list = []
counter = 0
err_message = "A periódusos rendszer táblázatból és a data.txt fájlból kinyert adatok nem egyeznek!"
message = "A periódusos rendszer táblázatból és a data.txt fájlból kinyert adatok egyeznek !" \
          " A kinyert adatok a data1.txt fájlba megtekinthetők."

# functions

def split_element(e):
    n = e.replace("\n", " ")
    el = n.split(" ")
    return el

try:
    driver.get(url)

    boxes = driver.find_elements_by_tag_name("li")

    for i in range(len(boxes)):
        e = boxes[i].text
        el = split_element(e)
        if boxes[i].text != "":
            element_list.append(el[1])
    with open("data.txt", "r") as test_data:
        for l in test_data.readlines():
            test_element = split_element(l)
            assert element_list[counter] == test_element[1], err_message
            counter = counter + 1
    print(message)
    with open("data1.txt", "w") as new_data:
        for j in range(len(element_list)):
            element_in_list = f"{j+1}., {element_list[j]}"
            new_data.write(element_in_list+"\n")
finally:
    driver.close()