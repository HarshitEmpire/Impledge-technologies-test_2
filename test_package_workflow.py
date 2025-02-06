from selenium import webdriver  
from selenium.webdriver.common.by import By  
from selenium.webdriver.support.ui import WebDriverWait  
from selenium.webdriver.support import expected_conditions as EC  
import random  
import time  

# Configurations  
URL = "https://ecspro-qa.kloudship.com"  
USER = "kloudship.qa.automation@mailinator.com"  
PASSWORD = "Password1"  
PACKAGE_NAME = "John_Doe"  # Replace with your name  

def test_add_delete_package():  
    driver = webdriver.Chrome()  
    driver.get(URL)  

    # Login  
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "username"))).send_keys(USER)  
    driver.find_element(By.ID, "password").send_keys(PASSWORD)  
    driver.find_element(By.XPATH, "//button[contains(text(),'Login')]").click()  

    # Navigate to Package Types  
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'Package Types')]"))).click()  

    # Add Package  
    driver.find_element(By.XPATH, "//button[contains(text(),'Add Manually')]").click()  
    driver.find_element(By.ID, "name").send_keys(PACKAGE_NAME)  
    dimensions = random.randint(1, 19)  
    driver.find_element(By.ID, "length").send_keys(dimensions)  
    driver.find_element(By.XPATH, "//button[contains(text(),'Save')]").click()  
    time.sleep(2)  # Allow time for save  

    # Logout  
    driver.find_element(By.XPATH, "//a[contains(text(),'Logout')]").click()  

    # Verify package exists (Test 01)  
    driver.get(URL)  
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "username"))).send_keys(USER)  
    driver.find_element(By.ID, "password").send_keys(PASSWORD)  
    driver.find_element(By.XPATH, "//button[contains(text(),'Login')]").click()  
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'Package Types')]"))).click()  
    assert PACKAGE_NAME in driver.page_source  

    # Delete Package (Test 02)  
    package_row = driver.find_element(By.XPATH, f"//td[contains(text(),'{PACKAGE_NAME}')]/..")  
    package_row.find_element(By.CLASS_NAME, "delete-btn").click()  
    WebDriverWait(driver, 10).until(EC.alert_is_present()).accept()  
    time.sleep(2)  

    # Logout  
    driver.find_element(By.XPATH, "//a[contains(text(),'Logout')]").click()  
    driver.quit()  

if __name__ == "__main__":  
    test_add_delete_package()  