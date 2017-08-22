from selenium import webdriver
import getpass
import time
import pickle

CPickle = True

def onstart():

    path = '' #set to path of driver on computer
    driver = webdriver.Chrome(path)
    url = '' #slack url
    driver.get(url)

    return driver

def SignIn(username,password,driver):

    """

    :type driver: object
    """
    driver.find_element_by_xpath("//*[@id=\"email\"]").send_keys(username)
    driver.find_element_by_xpath("//*[@id=\"password\"]").send_keys(password)
    driver.find_element_by_xpath("//*[@id=\"signin_btn\"]").click()
    _Code = input("What is the 2fa code?")
    driver.find_element_by_xpath('''//*[@id="auth_code"]''').send_keys(_Code)
    driver.find_element_by_xpath('''//*[@id="signin_btn"]''').click()


    pickle.dump(driver.get_cookies(), open("MYcookies.pkl","wb"))

    time.sleep(30)



def main():

    global CPickle

    if not CPickle:
        driver = onstart()
        username = input("What is your username")
        password = getpass.getpass("What is your password")
        SignIn(username, password, driver)

    else:
        driver = onstart()
        cookies = pickle.load(open("MYcookies.pkl", "rb"))
        for c in cookies:
            driver.add_cookie(c)

        driver.refresh()

        time.sleep(5)



main()
