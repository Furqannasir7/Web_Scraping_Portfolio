from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time

# path to chromedriver.exe
path = '//Driver/chromedriver'
# create instance of webdriver
driver = webdriver.Chrome(path)
# google url
url = 'https://www.google.com'
# Code to open a specific url
driver.get(url)
# set the keyword you want to search for
keyword = 'stocks'
# we find the search bar using it's name attribute value
searchBar = driver.find_element_by_name('q')
# first we send our keyword to the search bar followed by the enter # key
searchBar.send_keys(keyword)
searchBar.send_keys('\n')
#Set 10 secs delay for loading content fully
#time.sleep(10)

#Function for scraping
def scrape():
    pageInfo = []
    try:
        # wait for search results to be fetched
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "g"))
        )
    except Exception as e:
        print(e)
        driver.quit()
    # contains the search results
    searchResults = driver.find_elements_by_class_name('g')

    for result in searchResults:
        element = result.find_element_by_css_selector('a')
        link = element.get_attribute('href')
        header = result.find_element_by_css_selector('h3').text
        text = result.find_element_by_class_name('aCOpRe').text
        pageInfo.append({'header' : header, 'link' : link, 'text': text })
        return pageInfo

#Results from next pages
# Number of pages to scrape
numPages = 5
# All the scraped data
infoAll = []
# Scraped data from page 1
infoAll.extend(scrape())
for i in range(0 , numPages - 1):
   nextButton = driver.find_element_by_link_text('Next')
   nextButton.click()
   infoAll.extend(scrape())

#Saving Data into CSV with pandas
df = pd.DataFrame(infoAll)
fileName = keyword + '_' + str(numPages) + '.csv'
df.to_csv(fileName)