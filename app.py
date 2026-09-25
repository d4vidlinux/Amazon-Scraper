#!/usr/bin/env python3

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()
wait = WebDriverWait(driver, 30)

driver.get("https://amazon.com.br")

wait.until(
    EC.presence_of_element_located((By.XPATH, "//div[@class='_single-video-card_style_video-container__1hKS1 _single-video-card_style_overlay__3Sx3u']"))
)

names = wait.until(
    EC.presence_of_all_elements_located((By.XPATH, "//div[@class='a-section a-spacing-none _cXVhZ_asin-title_16ABS']"))
)

prices = wait.until(
    EC.presence_of_all_elements_located((By.XPATH, "//div[@class='a-section a-spacing-none _cXVhZ_asin-title_16ABS']/following-sibling::div"))
)


produtos = {
    "name": [i.text for i in names],
    "price": [i.text.replace("\n", ",") for i in prices]
}

for name, price in zip(produtos["name"], produtos["price"]):
    print(name, price)



input("\nPress Enter to Exit...")

driver.quit()  
