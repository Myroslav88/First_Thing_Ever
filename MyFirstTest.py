from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.implicitly_wait(5)

import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)


driver.get("https://keplercode.com/")
driver.maximize_window()
drop_menu = driver.find_element(By.CSS_SELECTOR, "span[class*='avia-menu-text']")
action_chains = ActionChains(driver)
action_chains.move_to_element(drop_menu).perform()


driver.find_element(By.CSS_SELECTOR, "#menu-item-3237 > a:nth-child(1) > span:nth-child(2)").click()


Title = driver.find_element(By.CSS_SELECTOR, "h1[class*=av-special-heading-tag").text
Title1 = "About Us"


assert Title == Title1, f"Test failed - {Title}"

time.sleep(5)
