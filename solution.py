from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException
from time import sleep

FB_EMAIL = "cinnamonsnap@msn.com"
FB_PASSWORD = "1H4t3Th1sS1t3"

chrome_driver_path = "/Users/abigailnottingham/Development/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://www.tinder.com")

sleep(2)
login_button = driver.find_element_by_xpath('//*[@id="t-1801132545"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/button')
login_button.click()

sleep(2)
facebook_login = driver.find_element_by_css_selector('img[src="/static/build/m/607412d0d342547e47e3935a57b79940.svg"]')
facebook_login.click()

sleep(2)
base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)
print(driver.title)

email = driver.find_element_by_xpath('//*[@id="email"]')
password = driver.find_element_by_xpath('//*[@id="pass"]')

email.send_keys(FB_EMAIL)
password.send_keys(FB_PASSWORD)
password.send_keys(Keys.ENTER)

driver.switch_to.window(base_window)
print(driver.title)

sleep(7)
accept_cookies = driver.find_element_by_xpath('//*[@id="t-1801132545"]/div/div[2]/div/div/div[1]/button')
accept_cookies.click()
allow_location_tracking = driver.find_element_by_xpath('//*[@id="t--239073259"]/div/div/div/div/div[3]/button[1]')
allow_location_tracking.click()
deny_notifications = driver.find_element_by_xpath('//*[@id="t--239073259"]/div/div/div/div/div[3]/button[2]/span')
deny_notifications.click()
sleep(10)

for n in range(100):
    sleep(1)
    try:
        print("called")
        like_button = driver.find_element_by_xpath(
            '//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[4]/button')
        like_button.click()
    except ElementClickInterceptedException:
        try:
            match_popup = driver.find_element_by_css_selector(".itsAMatch a")
            match_popup.click()
        except NoSuchElementException:
            sleep(2)

driver.quit()