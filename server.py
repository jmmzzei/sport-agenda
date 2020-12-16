from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from dotenv import load_dotenv 
import os

load_dotenv('.env')

browser = webdriver.Firefox()
browser.get(os.getenv('BASE_URL'))
browser.implicitly_wait(1)
titles = []
i = 0

for tournament in browser.find_elements_by_css_selector(os.getenv('TOURNAMENT_SELECTOR')):
  titles.append(tournament.text)

for event in browser.find_elements_by_css_selector(os.getenv('EVENT_SELECTOR')):
  print('----------------------------------------')
  print(titles[i])
  print('----------------------------------------')
  i = i + 1
  print(event.text)

browser.quit()
