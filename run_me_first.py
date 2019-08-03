'''
Hi, just to be shore that everything goes well we need to do some things first

We will run selenium webdriver in non headles mode

so we can create cookies, hopefoly after this you dont need to run me again.

Here we basicly need to login for the first time manualy.

'''
from selenium import webdriver
from acc import acount_info
from time import sleep
import json


class First_run():

    def __init__(self):
        self.text = '''
            Hi, just to be shore that everything goes well we need to do some things first

            We will run selenium webdriver in non headles mode

            so we can create cookies, hopefoly after this you dont need to run me again.

            Here we basicly need to login for the first time manualy.
            
            No more talking lets start
            '''
    def start_message(self):
        print(self.text)

    def login(self):
        driver = webdriver.Firefox()
        driver.get("https://www.audible.com/")
        EMAIL, PASS = acount_info()
        driver.find_element_by_xpath("/html/body/div[1]/div[4]/div/div/div/header/div[1]/span/nav/span/ul/li[2]/a").click()
        #print("Login page opend")
        #sleep(5)

        email_imput = driver.find_element_by_xpath('//*[@id="ap_email"]')
        email_imput.send_keys(EMAIL)
        pass_imput = driver.find_element_by_xpath('//*[@id="ap_password"]')
        pass_imput.send_keys(PASS)
        sleep(5)
        sub_but = driver.find_element_by_xpath('//*[@id="signInSubmit"]').click()
        print("PLEASE CHECK IF LOGIN IS OK\nIF LOGIN IS NOT SUCCESFUL YOU NEED TO ENTER PASSWORDAND VERIFICATION CODE!!!")
        print("WHEN YOU LOGIN SUCCESFULY WE WILL CREATE COOKIES FOR THE NEXT TIME")
        while True:
            q = input("DID YOU LOGIN SUCCESSFULY?(Y/N/Q)\n")
            if q.lower() == "y":
                print("OK wee will create cookies now")
                sleep(5)
                cookies = driver.get_cookies()
                with open("cookies.json", "w") as f:
                    f.write(json.dumps(cookies))
                print("Cookies created")
                print("The driver will close automaticly, please wait")
                driver.close()
                print("Driver closed")
                print("You can run get_html.py script now")
                break
            elif q.lower() == "n":
                print("Please try to login again")
                sleep(5)

            elif q.lower() == "q":
                print("Closing the script!!!")
                driver.close()
                print("BYE")
                break


def main():
    f = First_run()
    f.start_message()
    f.login()

if __name__=="__main__":
    main()
