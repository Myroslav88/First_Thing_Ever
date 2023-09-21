from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

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

for indx in range(6):
    drop_menu_1 = WebDriverWait(driver, 5).until(
        EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "ul[class*=sub-menu]>span")))
    drop_menu_1[indx].click()
    time.sleep(5)
    driver.back()











