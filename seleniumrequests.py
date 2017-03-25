#coding=utf-8
from seleniumrequests import *

# Simple usage with built-in WebDrivers:
webdriver = Chrome()
response = webdriver.request('GET', 'https://www.google.com/')
print(response)