from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
from pathlib import  Path
import pprint


from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
# In order for ChromeDriverManager to work you must pip install it in your own environment.
driver = webdriver.Chrome(ChromeDriverManager().install())

url = "https://witty-hill-0acfceb03.azurestaticapps.net/mutant_teams.html"

try:
    driver.get(url)
    frost = driver.find_element_by_xpath('// *[ @ id = "emma-frost"] / h2')
    hellfire = driver.find_element_by_xpath('//*[@id="hellfire"]')
    original = driver.find_element_by_xpath('//*[@id="original"]')

    #print(frost)
    #print(frost.text)
    #print(len(frost))
    print("Frost attribute" +frost.get_attribute("innerHTML"))
    print("Frost displayed" + str(frost.is_displayed()))
    print("Hellfire inner HTML" + hellfire.get_attribute("innerHTML"))
    print("Original inner HTML" + original.get_attribute("innerHTML"))
    print(original.is_selected())
    print(hellfire.is_selected())
    time.sleep(2)
    ActionChains(driver).move_to_element(hellfire).click(hellfire).perform()
    hellfire.click()

    print(frost.get_attribute("innerHTML"))
    print(frost.is_displayed())
finally:
    pass