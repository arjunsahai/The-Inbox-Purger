from selenium import webdriver
import time

def login(username, driver):
    driver.get('http://www.google.com/xhtml')
    signin = driver.find_element_by_link_text('Sign in')
    signin.click()
    userinput = driver.find_element_by_id('identifierId')
    userinput.send_keys(username)
    driver.find_element_by_id('identifierNext').click()
    print('passwordPage')

def enterpassword(password, driver):
    userpassword = driver.find_element_by_name('password')
    print('successfully logged in')
    userpassword.send_keys(password)
    driver.find_element_by_id('passwordNext').click()

def gmail(driver):
    driver.find_element_by_link_text('Gmail').click()

def purge(driver):
    # checkID = 'T-Jo-auq'
    # markID = 'T-I-Zf-aw2'
    # check = driver.find_element_by_class_name(checkID)
    buttons = driver.find_elements_by_class_name("T-I")
    threedots = buttons[13]
    buttons[13].click()
    menuitems = driver.find_elements_by_xpath("//div[@role='menuitem']")
    threedots.click()
    next = driver.find_element_by_xpath("//div[@aria-label='Older']")
    inboxcount = len(driver.find_element_by_class_name('UKr6le').text)
    if (inboxcount > 5):
        while (inboxcount != 5):
            threedots.click()
            time.sleep(1.5)
            for menuitem in menuitems:
                if menuitem.text == "Mark all as read":
                    menuitem.click()
            time.sleep(1.5)
            next.click()
            time.sleep(1.5)
            inboxcount = len(driver.find_element_by_class_name('UKr6le').text)
            next = driver.find_element_by_xpath("//div[@aria-label='Older']")
            time.sleep(3)
    print("inbox PURGED")
    driver.quit()


if (__name__ == "__main__"):
    username = '!!!!!!!!!PUT GMAIL USERNAME HERE!!!!!!!!!!'
    password = '!!!!!!!!!PUT GMAIL PASSWORD HERE!!!!!!!!!!'
    driver = webdriver.Chrome()
    login(username, driver)
    time.sleep(3)
    enterpassword(password, driver)
    time.sleep(3)
    gmail(driver)
    time.sleep(3)
    purge(driver)
