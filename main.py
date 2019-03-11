import selenium
import re
from selenium import webdriver


driver = webdriver.Chrome(executable_path='/Users/biancalisle/Downloads/chromedriver')
driver.get("https://play.google.com/store/apps/top")

free_apps = driver.find_element_by_name('Top gratuitos em Apps Android')
free_apps.click()


# driver.quit()
