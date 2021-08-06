# environment settings
# ......................................................................
import time

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
options.add_argument('--headless')
options.add_argument('--disable-gpu')

# In order for ChromeDriverManager to work you must pip install it in your own environment.

# driver = webdriver.Chrome(ChromeDriverManager().install())
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

url = "https://witty-hill-0acfceb03.azurestaticapps.net/film_register.html"

# variables

number_of_films = 24
a_list_num = number_of_films + 1
b_list_num = a_list_num + 1
err_message1 = "A katalógusban lévő filmek száma nem 24"
message1 = "A katalógusban lévő filmek száma 24"
err_message2 = "A katalógusban lévő filmek új száma nem 25"
message2 = "A katalógusban lévő filmek új száma 25"
entry_elements = ["nomeFilme", "anoLancamentoFilme", "anoCronologiaFilme", "linkTrailerFilme",
                  "linkImagemFilme", "linkImdbFilme"]
entry_items = ["Black widow", 2021, 2020, "https://www.youtube.com/watch?v=Fp9pNPdNwjI",
               "https://m.media-amazon.com/images/I/914MHuDfMSL._AC_UY327_FMwebp_QL65_.jpg",
               "https://www.imdb.com/title/tt3480822/"]

try:

    driver.get(url)


    # functions

    def entry_filler(list1, list2):
        driver.find_element_by_xpath("/html/body/div[2]/div[1]/button").click()
        time.sleep(2)
        for i, entry in enumerate(list1):
            e = entry
            driver.find_element_by_xpath(f"//*[@id='{entry}']").send_keys(list2[i])
            time.sleep(1)
        driver.find_element_by_xpath("/html/body/div[2]/div[2]/fieldset/button[1]").click()


    # TC 01 = length of film list in the register = 24

    film_list = WebDriverWait(driver, 5).until(lambda driver: len(driver.find_elements_by_tag_name('a')) == a_list_num)
    assert film_list, err_message1
    print("TC 01")
    print(message1)
    print()

    # TC 02   after adding a new element, the new length of list register = 25

    entry_filler(entry_elements, entry_items)

    # film_list = WebDriverWait(driver, 5).until(lambda driver: len(driver.find_elements_by_tag_name('a')) == b_list_num)

    assert len(driver.find_elements_by_tag_name('a')) == b_list_num, err_message2
    print("TC 02")
    print(message2)

finally:
    driver.close()
