from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

data_types = ["hydro_monthly", "accretion", "forestveg", "marshveg", "biomass", "soil_properties", "surface_elevation"]
for data_type in data_types:
    driver.get("https://cims.coastal.louisiana.gov/DataDownload/DataDownload.aspx?type=" + data_type)
    project_element = driver.find_element(By.ID, "MainContent_DDL_ProjectList")
    options = project_element.find_elements(By.TAG_NAME, "option")
    option_values = []
    for option in options:
        option_values.append(option.get_attribute("value"))

    station_element = driver.find_element(By.ID, "MainContent_DDL_Stations")
    station_select = Select(station_element)

    for index, option_value in enumerate(option_values[1:]):
        project_select = Select(driver.find_element(
            By.ID, "MainContent_DDL_ProjectList"))
        project_select.select_by_value(option_value)
        driver.find_element(By.ID, "MainContent_BTN_DownLoad").click()
        input_box = driver.find_element(By.ID, "MainContent_TB_Filename")
        input_box.send_keys(data_type + "_" + str(index + 1))
        driver.find_element(By.ID, "MainContent_BTN_OkFilename").click()
        WebDriverWait(driver, timeout=3)

driver.quit()
