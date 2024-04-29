import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Start the web browser (Chrome)
driver = webdriver.Chrome()

# Open the website
driver.get("https://clickcounter.io")

start_time = time.time()

try:
    # Wait until the element with id "currentValue" is visible
    value_element = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.ID, "currentValue"))
    )

    # Get the text content of the value element
    button_text = value_element.text.strip()

    # Convert the button text to an integer
    current_count = int(button_text)

    # Calculate the number of clicks needed to reach 2024
    clicks_needed = 2024 - current_count

    # Click the button the required number of times
    button = driver.find_element(By.ID, "up")
    for _ in range(clicks_needed):
        button.click()

    end_time = time.time()
    elapsed_time = end_time - start_time

    print("Counter set to 2024 successfully!")
    print("Time taken:", elapsed_time, "seconds")

    # Wait for 15 seconds before closing the browser
    time.sleep(15)

finally:
    # Close the browser after finishing
    driver.quit()
