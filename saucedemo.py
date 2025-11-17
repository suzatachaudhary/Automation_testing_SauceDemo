from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://www.saucedemo.com/")
time.sleep(2)

driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()
time.sleep(2)

print("Login successful!")

driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
time.sleep(1)

print("Product added to cart!")

driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
time.sleep(2)

item_name = driver.find_element(By.CLASS_NAME, "inventory_item_name").text
print("Item in cart:", item_name)

driver.find_element(By.ID, "react-burger-menu-btn").click()
time.sleep(1)
driver.find_element(By.ID, "logout_sidebar_link").click()
time.sleep(2)

print("Logout successful!")

driver.quit()
