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
#options.add_argument('--headless')
#options.add_argument('--disable-gpu')

# In order for ChromeDriverManager to work you must pip install it in your own environment.

# driver = webdriver.Chrome(ChromeDriverManager().install())
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

url = "https://witty-hill-0acfceb03.azurestaticapps.net/charterbooker.html"

try:
    # test data

    number_of_guest = "1"
    date_and_time = datetime(2021, 9, 1, 12)
    part_of_day = "Morning"
    hours_for_charter = "3"
    name = "Nagy László"
    email_with_at = "aaa@bb"
    email_invalid = "aabb"
    valid_email = "nail@t-online.hu"
    message_text = "Try to do your best !"
    validation_text = "Your message was sent successfully. Thanks! We" + "'" + "ll be in touch as soon as we can, " \
                                                                               "which is usually like lightning (Unless we" + "'" + "re sailing or eating tacos!)."
    message1 = "Test passed: app accepted email with no domain in it !!!"
    #err_message1 =
    err_message3 = "Test passed: app refused email with no @ in it !!"
    message3 = "Test failed: app accepted the invalid email (no @ in the email) !!"

    email_err_text = "PLEASE ENTER A VALID EMAIL ADDRESS."

    # function "testing_app()" tests the app with different e-mail addresses using test data above


    def testing_app(e_mail):

        driver.get(url)

        # elements - first page

        guest_number = driver.find_element_by_xpath('// *[ @ id = "step1"] / ul / li[1] / select / option[2]')
        next_button1 = driver.find_element_by_xpath('//*[@id="step1"]/ul/li[2]/button')

        # elements - second page

        input_date = driver.find_element_by_xpath('//*[@id="step2"]/ul/li[1]/input')
        daypart = driver.find_element_by_xpath('//*[@id="step2"]/ul/li[2]/select/option[2]')
        charter = driver.find_element_by_xpath('//*[@id="step2"]/ul/li[3]/select/option[2]')
        next_button2 = driver.find_element_by_xpath('//*[@id="step2"]/ul/li[4]/button')

        # elements - third page

        full_name = driver.find_element_by_xpath('//*[@id="step3"]/ul/li[1]/input')
        email = driver.find_element_by_xpath('//*[@id="step3"]/ul/li[2]/input')
        message = driver.find_element_by_xpath('//*[@id="step3"]/ul/li[3]/textarea')
        send_button = driver.find_element_by_xpath('//*[@id="step3"]/ul/li[4]/button')
        # email_error = driver.find_element_by_xpath('//*[@id="step3"]/ul/li[2]/input').get_attribute("aria-invalid")

        # function's body

        guest_number.click()
        next_button1.click()

        input_date.send_keys(date_and_time.strftime("%Y/%m/%d %I:%M\t%p"))
        daypart.click()
        charter.click()
        next_button2.click()

        full_name.send_keys(name)
        email.send_keys(e_mail)
        message.send_keys(message_text)
        send_button.click()
        if e_mail == email_invalid:
            t = driver.find_element_by_id("bf_email-error").text
            assert email_err_text != t, err_message3
            print(message3)
        else:
            val_text = WebDriverWait(driver, 2).until(EC.visibility_of_element_located((By.XPATH,
                                                                                    '//form[@id="booking-form"]/h2')))
            v_text = val_text.text
        return v_text


    # app is runing with different e_mails

    for e_mail in (valid_email, email_with_at, email_invalid):
        # how the application works with good e-mail

        val_text = testing_app(valid_email)

        # TC01 - notification of well filled-in form

        assert val_text == validation_text, "A helyes kitöltésre adott válasz nem jelent meg," \
                                            " az app nem futott le!"
        print("TC01")
        print("A teszt sikeresen lefutott !\n")
        print("A helyes kitöltésre adott válasz:")
        print(val_text + "\n")

        # TC02 - invalid email - no domain name

        val_text = testing_app(email_with_at)
        assert val_text == validation_text, "A helyes kitöltésre adott válasz nem jelent meg," \
                                            " az app nem futott le!"
        print("TC02")
        print(message1 + "\n")

        # TC04 - invalid email - no obligatory element @

        print("TC03")
        testing_app(email_invalid)
        print(message3 + "\n")

finally:
    driver.close()
