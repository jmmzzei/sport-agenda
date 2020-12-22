from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from dotenv import load_dotenv 
import os

load_dotenv('.env')

browser = webdriver.Firefox()
browser.get(os.getenv('BASE_URL'))
browser.implicitly_wait(1)

for tournament in browser.find_elements_by_css_selector(os.getenv('TOURNAMENT_SELECTOR')):
  print(tournament.text)
  print('----------------------------------------')

browser.quit()
