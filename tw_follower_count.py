# Selenium stuff.
from selenium import webdriver
#from selenium.webdriver.common.by import By
#from selenium.common.exceptions import TimeoutException
#from selenium.webdriver.support.ui import WebDriverWait
#from selenium.webdriver.support.ui import Select
#from selenium.webdriver.support import expected_conditions as EC

# System, time and regex stuff.
import sys
#import time
#import re
import csv

handles = []
follower_counts = []

with open(sys.argv[1]) as dataFile:
    data = csv.reader(dataFile)
    for handle in data:
        handles.append(handle[0])


# Create a new instance of the Firefox driver.
driver = webdriver.Firefox()

for handle in handles:
  try:
    driver.get("http://twitter.com/" + handle)
    followers = driver.find_element_by_css_selector('li.ProfileNav-item--followers span.ProfileNav-value')
    follower_counts.append(followers.text)
  except:
    print sys.exc_info()

driver.quit()

# Write out to CSV
csvFile = csv.writer(open(sys.argv[1] + "-counts.csv", "wb+"))
for i,handle in enumerate(handles):
  csvFile.writerow([handle, follower_counts[i]])
