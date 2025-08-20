from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
import requests
zillow_url="https://appbrewery.github.io/Zillow-Clone/"
result=requests.get(zillow_url)
soup=BeautifulSoup(result.text,"html.parser")
cards=soup.find_all("li",class_="ListItem-c11n-8-84-3-StyledListCardWrapper")
property_links=[]
property_addresses=[]
property_prices=[]
for card in cards:
    property_links.append(card.find("a").get("href"))
    property_addresses.append(card.find("img").get("alt"))
    price=card.find("span", attrs={"data-test": "property-card-price"}).text.split('+')[0].split('/')[0]
    property_prices.append(price)
print(property_links)
print(property_addresses)
print(property_prices)
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach',True)
driver = webdriver.Chrome(options=chrome_options)
google_form_url="https://docs.google.com/forms/d/e/1FAIpQLSdkisYNuvDEhygFg2z--f-AmijVKlGIRJr-hLG91MALtnS72g/viewform?usp=header"
driver.get(google_form_url)
time.sleep(5)
for i in range(10):
    input_boxes = driver.find_elements(By.CSS_SELECTOR, "input.whsOnd.zHQkBf")
    input_boxes[0].send_keys(property_addresses[i])
    input_boxes[1].send_keys(property_prices[i])
    input_boxes[2].send_keys(property_links[i])
    submit_button = driver.find_element(By.XPATH, "//span[text()='Submit']")
    submit_button.click()
    time.sleep(3)
    another_response = driver.find_element(By.LINK_TEXT, "Submit another response")
    another_response.click()
    time.sleep(3)