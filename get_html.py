from selenium import webdriver
from bs4 import BeautifulSoup as bs
from selenium.webdriver.firefox.options import Options
from time import sleep
import os
from acc import acount_info
import json


def html_g():
    EMAIL, PASS = acount_info()
    if "@" not in EMAIL:
        message = "Please check your email in acc.py file and try again"
        body = message
        print(message)
    else:
        url = "https://www.audible.com/"
        URL = input("Please enter url for scraping audible.com:\n")
        # SAMPLE URL:
        #URL = "https://www.audible.com/pd/The-Adventures-of-Tom-Stranger-Interdimensional-Insurance-Agent-Audiobook/B01D0FJOAI?pf_rd_p=b0a63225-9612-46cb-9489-1de98768879a&pf_rd_r=MG3F1HT0258KWMP9727X&ref=a_hp_c7_bestsellers-d_1_3"
        # RUN HEADLESS MODE
        options = Options()
        options.headless = True

        driver = webdriver.Firefox(options = options)
        driver.get(url)
        print("OPEN OK")
        files = os.listdir()
        if "cookies.json" in files:
            print("Importing cookies")
            cookies = json.load(open("cookies.json"))
            for cookie in cookies:
                driver.add_cookie(cookie)
            driver.refresh()
            print("Login OK")
            sleep(5)
        else:
            driver.find_element_by_xpath("/html/body/div[1]/div[4]/div/div/div/header/div[1]/span/nav/span/ul/li[2]/a").click()
            #print("Login page opend")
            #sleep(5)

            email_imput = driver.find_element_by_xpath('//*[@id="ap_email"]')
            email_imput.send_keys(EMAIL)
            pass_imput = driver.find_element_by_xpath('//*[@id="ap_password"]')
            pass_imput.send_keys(PASS)
            sub_but = driver.find_element_by_xpath('//*[@id="signInSubmit"]').click()
            sleep(10)
            print("Creating cookies for the next time")
            cookies = driver.get_cookies()
            with open("cookies.json", "w") as f:
                f.write(json.dumps(cookies))
            print("Cookies created")

            
        driver.get(URL)
        print("url opend")
        body = driver.find_element_by_tag_name("body").get_attribute("innerHTML")
        driver.close()

        # CHECKING IF LOGIN OK
        soup = bs(body, "html.parser")
        try:
            name = soup.select("span.bc-text.navigation-do-underline-on-hover.ui-it-barker-text")[0].text.replace("\n", "").replace("Hi", "").replace("!", "").replace(",", "").strip()
            book_name = soup.select("h1.bc-heading.bc-color-base.bc-pub-break-word.bc-text-bold")[0].text
            print("You are logged in as: {}".format(name))
            print("You have html output for book name: {}".format(book_name))
            return body
        except IndexError as e:
            os.remove("cookies.json")
            message = "Something went wrong, please check your email and password and try again!\nIf this message happend again even if your mail and password are OK\nContact me for support!"
            return message


html = html_g()
print(html)
