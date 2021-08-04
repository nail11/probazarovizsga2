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

# from datetime import date
# import time
# from pathlib import Path
# import pprint


options = Options()
# options.add_argument('--headless')
# options.add_argument('--disable-gpu')

# In order for ChromeDriverManager to work you must pip install it in your own environment.

# driver = webdriver.Chrome(ChromeDriverManager().install())
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

url = "https://witty-hill-0acfceb03.azurestaticapps.net/periodic_table.html"

# elements

# variables

# functions
def split_element(e):
    n = e.replace("\n", " ")
    el = n.split(" ")
    return el

try:
    driver.get(url)


    boxes = driver.find_elements_by_tag_name("li")
    element_list = []
    #listed_elements = []

    for i in range(len(boxes)):
        e = boxes[i].text
        el = split_element(e)
        if boxes[i].text != "":
            element_list.append(el[1])
    with open("data1.txt", "w") as f:
        for j in range(len(element_list)):
            element_in_list = f"{j+1}., {element_list[j]}"
            f.write(element_in_list+"\n")

            #listed_elements.append(element_in_list)
    #with open("data.txt", "w") as f:

        #f.write

    #print(listed_elements)


finally:
    pass