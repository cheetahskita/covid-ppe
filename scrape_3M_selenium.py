from selenium import webdriver
import time
import re

driver = webdriver.Chrome(r'C:\Users\moth1\chromedriver.exe')

# driver = webdriver.Chrome()
# Go to the page that we want to scrape
driver.get("https://www.3m.com/3M/en_US/company-us/all-3m-products/~/3M-Integrated-Protective-Eyewear/?N=5002385+8707795+3290055770&rt=rud")

# Click review button to go to the review section
time.sleep(2)
product_button = driver.find_element_by_xpath('//div[@class="MMM--childcount js-hdrChildCnt"]')
product_button.click()

# 3M has security against Selenium, so this approach was abandoned. Instead, the page was manually downloaded and scraped for all the product links at once.
# see scrape_3M_bsoup.ipnyb for remaining work