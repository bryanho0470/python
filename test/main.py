from bs4 import BeautifulSoup
import os

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
browser.get("https://jp.indeed.com/jobs?q=java")
soup = BeautifulSoup(browser.page_source, "html.parser")
print(soup)




