import traceback
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.keys import Keys

browser = webdriver.Remote(
    command_executor='http://127.0.0.1:4444/wd/hub',
    desired_capabilities=DesiredCapabilities.CHROME,    
)

browser.get("http://www.google.com")
try:
    browser.find_element_by_class_name("gLFyf").send_keys("python")
    browser.find_element_by_name("btnK").send_keys(Keys.ENTER)
    titles = browser.find_elements_by_xpath(".//h3[@class='r']//a")
    print([i.text for i in titles])
except Exception:
    print(traceback.print_exc())

browser.quit()
