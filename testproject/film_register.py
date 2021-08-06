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
#options.add_argument('--headless')
#options.add_argument('--disable-gpu')

# In order for ChromeDriverManager to work you must pip install it in your own environment.

# driver = webdriver.Chrome(ChromeDriverManager().install())
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

url = "https://witty-hill-0acfceb03.azurestaticapps.net/film_register.html"


# elements
#  reg_butt = driver.find_element_by_xpath("/html/body/div[2]/div[1]/button")

# variables

number_of_films = 24
a_number = number_of_films+1
film_title = "Black widow"
release_year = 2021
chronological_year_of_events = 2020
trailer_url = "https://www.youtube.com/watch?v=Fp9pNPdNwjI"
image_url = "https://m.media-amazon.com/images/I/914MHuDfMSL._AC_UY327_FMwebp_QL65_.jpg"
film_summary = "https://www.imdb.com/title/tt3480822/"
err_message1 = "A katalógusban lévő filmek száma nem 24"
message1 = "A katalógusban lévő filmek száma 24"

try:

    driver.get(url)

    film_list = WebDriverWait(driver, 5).until(lambda driver: len(driver.find_elements_by_tag_name('a')) == a_number)
    assert film_list, err_message1
    print(message1)

    driver.find_element_by_xpath("/html/body/div[2]/div[1]/button").click()

    #JavaScript = "driver.find_element_by_xpath('/html/body/div[2]/div[2]/fieldset/button[1]').click();"
    #driver.execute_script(JavaScript)

    cim1 = driver.find_element_by_id("nomeFilme")
    cim2 = driver.find_element_by_xpath('//*[@id="nomeFilme"]')
    driver.find_element_by_id("nomeFilme").send_keys("film_title")
    driver.find_element_by_xpath('//*[@id="nomeFilme"]').send_keys("film_title")
    print(cim1)
    print(cim2)
    driver.find_element_by_xpath('//*[@id=""nomeFilme"]').send_keys("film_title")
    driver.find_element_by_xpath('//*[@id="anoLancamentoFilme"]').send_keys("release_year")
    driver.find_element_by_xpath('//*[@id="anoCronologiaFilme"]').send_keys("chronological_year_of_events")
    driver.find_element_by_xpath('//*[@id="linkTrailerFilme"]').send_keys("trailer_url")
    driver.find_element_by_xpath('//*[@id="linkImagemFilme"]').send_keys("image_url")
    driver.find_element_by_xpath('//*[@id="linkImdbFilme"]').send_keys("film_summary")

    #driver.find_element_by_xpath('/html/body/div[2]/div[2]/fieldset/button[1]').click()


finally:
    pass
