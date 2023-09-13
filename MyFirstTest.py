
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)

driver.get("https://keplercode.com/")
driver.maximize_window()
drop_menu = driver.find_element(By.XPATH,"/html/body/div[2]/header/div[1]/div/div/nav/div/ul/li[1]/a/span[2]")
action_chains = ActionChains(driver)
action_chains.move_to_element(drop_menu).perform()

time.sleep(3)

driver.find_element(By.XPATH, "/html/body/div[2]/header/div[1]/div/div/nav/div/ul/li[1]/ul/li[1]/a/span[2]").click()
time.sleep(3)
Title = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[1]/div/div[2]/main/div/div/div[1]/div/h1").text
Title1 = "About Us"
if Title == Title1:
    print("Test was successful.")
else: print("Test failed.")
