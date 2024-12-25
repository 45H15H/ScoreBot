import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.service import Service


# Read roll numbers and DOBs from the text file
def read_rollnumbers_and_dobs(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    data = [line.strip().split() for line in lines]
    return data

# Initialize the web driver
def init_driver():

    driver = webdriver.Chrome()
    return driver

# Fetch the result and take a screenshot
def fetch_result(driver, rollnumber, dob):
    driver.get('https://mis.nitgoa.ac.in/misnitgoa/result.aspx')
    
    # Enter roll number
    rollnumber_field = driver.find_element(By.ID, 'txtRegno')
    rollnumber_field.send_keys(rollnumber)
    
    time.sleep(1)

    # Click on show button
    show_button = driver.find_element(By.ID, 'btnimgShow')
    show_button.click()
    
    # Select the second option in semester dropdown
    time.sleep(1)
    semester_dropdown = Select(driver.find_element(By.ID, 'ddlSemester'))
    semester_dropdown.select_by_index(1)
    
    time.sleep(1)

    # Enter DOB
    dob_field = driver.find_element(By.ID, 'txtDateOfBirth')
    dob_parts = dob.split('-')
    formatted_dob = f"{dob_parts[0]}-{dob_parts[1]}-{dob_parts[2]}"  # Ensure the format is YYYY-MM-DD
    driver.execute_script("arguments[0].value = arguments[1];", dob_field, formatted_dob)

    time.sleep(1)
    
    # Click fetch result button
    fetch_result_button = driver.find_element(By.ID, 'btnimgShowResult')
    fetch_result_button.click()
    
    # Wait for the results to load
    time.sleep(1)
    
    # Scroll down a little bit
    driver.execute_script("window.scrollBy(0, 600);")
    
    # Take a screenshot
    screenshot_path = os.path.join('output', f'{rollnumber}.png')
    driver.save_screenshot(screenshot_path)

    time.sleep(0.5)

# Main function
def main():
    data = read_rollnumbers_and_dobs('DOBs.txt')
    driver = init_driver()
    
    if not os.path.exists('output'):
        os.makedirs('output')
    
    for rollnumber, dob in data:
        fetch_result(driver, rollnumber, dob)
    
    driver.quit()

if __name__ == '__main__':
    main()