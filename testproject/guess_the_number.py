# environment settings
#......................................................................

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from datetime import datetime
# from selenium.webdriver.common.keys import Keys
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

url = "https://witty-hill-0acfceb03.azurestaticapps.net/guess_the_number.html"

try:
    driver.get(url)
    # elements
    input_field = driver.find_element_by_xpath('/html/body/div/div[2]/input')
    guess_button = driver.find_element_by_xpath("/html/body/div/div[2]/span/button")
    lower_field = driver.find_element_by_xpath("/html/body/div/p[3]")
    higher_field = driver.find_element_by_xpath("/html/body/div/p[4]")
    equal_field = driver.find_element_by_xpath("/html/body/div/p[5]")
    #num_gess = driver.find_element_by_xpath("/html/body/div/div[3]/p/span").text

   # variables
    guess_click = 0
    min = 0
    max = 100
    neg_num = -19
    high_num = 255
    err_message1 = "A szám < 0, az app összeomlott!"
    message1 =  "A szám < 0, az app nem omlott össze!"
    err_message2 = "A szám > 100, az app összeomlott!"
    message2 =  "A szám > 100, az app nem omlott össze!"
    err_message3 = "A számláló értéke eltér az app számláló értékétől !"
    message3 = "A számlálók értékei megegyeznek:\n"

    while (equal_field.get_attribute('class') == "alert alert-success ng-hide"):
        input_field.clear()
        number = int(((max - min) / 2) + min)
        d = int(max - number)
        for num in (neg_num, high_num, number):
            if num == neg_num:
                input_field.clear()
                input_field.send_keys(neg_num)
                guess_button.click()
                guess_click = guess_click + 1
                assert higher_field.get_attribute('class') == "alert alert-warning",err_message1
            elif num == high_num:
                input_field.clear()
                input_field.send_keys(high_num)
                guess_button.click()
                guess_click = guess_click + 1
                assert lower_field.get_attribute('class') == "alert alert-warning", err_message2
            else:
                input_field.clear()
                #number = int(((max - min) / 2) + min)
                #d = int(max - number)
                input_field.send_keys(number)
                guess_button.click()
                guess_click = guess_click + 1
                if int(max - number) > 1:
                    if lower_field.get_attribute('class') == "alert alert-warning":
                        max = number
                    if higher_field.get_attribute('class') == "alert alert-warning":
                        min = number
                else:
                    assert equal_field.get_attribute('class') == "alert alert-success"
                break
    num_gess = driver.find_element_by_xpath("/html/body/div/div[3]/p/span").text

    assert str(guess_click) == num_gess, err_message3

    print(message1+"\n")
    print(message2+"\n")
    print(message3)
    print(f"{guess_click} = {num_gess}")

finally:
    driver.close()
