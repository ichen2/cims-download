from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome()

driver.get(
    "https://cims.coastal.louisiana.gov/DataDownload/DataDownload.aspx?type=soil_properties")
project_element = driver.find_element(By.ID, "MainContent_DDL_ProjectList")
project_select = Select(project_element)
options = project_element.find_elements(By.TAG_NAME, "option")
station_element = driver.find_element(By.ID, "MainContent_DDL_Stations")
station_select = Select(station_element)
# for option in options:
#     project_select.select_by_value(option.value)
#     WebDriverWait(driver, timeout=3)

driver.quit()
