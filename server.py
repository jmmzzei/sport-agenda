from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from dotenv import load_dotenv 
import os
import re

load_dotenv('.env')

browser = webdriver.Firefox()
browser.get(os.getenv('BASE_URL'))
browser.implicitly_wait(1)

for tournament in browser.find_elements_by_css_selector(os.getenv('TOURNAMENT_SELECTOR')):
  events = re.split("^[A-Z\s\W\Ú\Ñ]+", tournament.text)
  title = re.match("^[A-Z\s\W\Ú\Ñ(1 DE FRANCIA)+]+", tournament.text)
  print(title.group(0)[:-1])
  print(events[1])
  print('----------------------------------------')

browser.quit()
