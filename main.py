import datetime
import random
import time

import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
import urllib
import time

executable_path = "D:\\ChatBot\\PythonWebScrapping_driver\\chromedriver_win32.exe"
serviceob1=Service(executable_path)

driver = webdriver.Chrome(service=serviceob1)
driver.maximize_window()

#driver.get("https://timbresonic.com/products/rhythm") #redirecting to to website
driver.get('https://timbresonic.com/products/aerdock-pro')

file_name = 'Scrapped_data' + str(random.randint(1, 1000)) + '.txt'
print(random.randint)

#stroing content of web page in text file
el = driver.find_element(By.TAG_NAME, 'body')
with open(file_name , 'w', encoding="utf-8") as f:
    f.write(el.text)

driver.close()


# Install the chrome web driver from selenium.
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome('chromedriver', chrome_options=chrome_options)
# Create url variable containing the webpage for a Google image search.
url = ("https://timbresonic.com/products/aerdock-pro")
# Launch the browser and open the given url in the webdriver.
driver.get(url.format(s='Pets'))
# Scroll down the body of the web page and load the images.
driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
time.sleep(5)

def findJPGImages():
    # Find the images.
    imgResults = driver.find_elements(By.XPATH, "//*[contains(@src,'.png')]")
    # Access and store the scr list of image url's.
    print(len(imgResults))
    src = []

    for img in imgResults:
        src.append(img.get_attribute('src'))

    # Retrieve and download the images.
    try:
        for i in range(len(imgResults)):
            urllib.request.urlretrieve(str(src[i]), "sample_data/pets{}.png".format(i))

    except exception:
        print(exception)
    finally:
        print("downloaded jpeg images")


def findPNGImages():
    # Find the images.
    imgResults = driver.find_elements(By.XPATH, "//*[contains(@src,'.jpg')]")
    # Access and store the scr list of image url's.
    print(len(imgResults))
    src = []
    src_png = []
    for img in imgResults:
        src.append(img.get_attribute('src'))

    # Retrieve and download the images.
    try:
        for i in range(len(imgResults)):
            urllib.request.urlretrieve(str(src[i]), "sample_data/pets2{}.jpg".format(i))
    except Exception:
        print(Exception)
    finally:
        print("Done")


findJPGImages()
findPNGImages()


driver.close()

