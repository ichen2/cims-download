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
option_values = []
for option in options:
    option_values.append(option.get_attribute("value"))
station_element = driver.find_element(By.ID, "MainContent_DDL_Stations")
station_select = Select(station_element)
for option_value in option_values:
    # need to get the project selector again since the page reloads
    project_select = Select(driver.find_element(
        By.ID, "MainContent_DDL_ProjectList"))
    project_select.select_by_value(option_value)
    WebDriverWait(driver, timeout=3)

driver.quit()
