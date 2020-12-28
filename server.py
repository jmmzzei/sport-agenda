from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from dotenv import load_dotenv 
import os
import re
import curses

load_dotenv('.env')

browser = webdriver.Firefox()
browser.get(os.getenv('BASE_URL'))
browser.implicitly_wait(1)

screen = curses.initscr()
screen.refresh()
i = 4
j = 1

for date in browser.find_elements_by_css_selector(os.getenv('DATE')):
  screen.addstr(1,0,"----------------------------------------")
  cDate = date.find_elements_by_css_selector(os.getenv('DATE_TITLE'))[0]
  screen.addstr(2,0,'| ' + cDate.text)
  screen.addstr(3,0,"----------------------------------------")
  for tournament in date.find_elements_by_css_selector(os.getenv('TOURNAMENT')):
    for title in tournament.find_elements_by_css_selector(os.getenv('TOURNAMENT_TITLE')):
      i = i + 1
      screen.addstr(i,0,title.text)
      # screen.refresh()
      # screen.clrtoeol()
      curses.napms(800)
      screen.refresh()

    for ev in tournament.find_elements_by_css_selector(os.getenv('EVENT')):
      for events in ev.find_elements_by_css_selector(os.getenv('EVENT_SELECTOR')):
        hour = events.find_element_by_css_selector(os.getenv('CUSTOM1'))
        match = events.find_element_by_css_selector(os.getenv('CUSTOM2'))
        tv = events.find_element_by_css_selector(os.getenv('CUSTOM3'))
        screen.addstr(i + j + 1,0,'PARTIDO: '+ match.text)
        screen.addstr(i + j,0, 'HORA: '+ hour.text)
        screen.addstr(i + j + 2,0,'TV: '+ tv.text)
        curses.napms(2000)
        screen.refresh()
    j = 1
  i = 4
  curses.napms(800)
  screen.clear()
  screen.refresh()

screen.clear()
screen.refresh()
curses.endwin()
browser.quit()
