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

for date in browser.find_elements_by_css_selector(os.getenv('DATE')):
  print('+----------------------------------------+')
  cDate = date.find_elements_by_css_selector(os.getenv('DATE_TITLE'))[0]
  print('| ' + cDate.text)
  print('+----------------------------------------+')
  for tournament in date.find_elements_by_css_selector(os.getenv('TOURNAMENT')):
    for title in tournament.find_elements_by_css_selector(os.getenv('TOURNAMENT_TITLE')):
      print(title.text)
    for ev in tournament.find_elements_by_css_selector(os.getenv('EVENT')):
      for events in ev.find_elements_by_css_selector(os.getenv('EVENT_SELECTOR')):
        hour = events.find_element_by_css_selector(os.getenv('CUSTOM1'))
        match = events.find_element_by_css_selector(os.getenv('CUSTOM2'))
        tv = events.find_element_by_css_selector(os.getenv('CUSTOM3'))
        print(hour.text)
        print(match.text)
        print(tv.text)
  print('+----------------------------------------+')

browser.quit()
