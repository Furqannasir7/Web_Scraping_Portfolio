from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException


def configure_driver():
    # Add additional Options to the webdriver
    chrome_options = Options()
    # add the argument and make the browser Headless.
    chrome_options.add_argument("--headless")
    # Instantiate the Webdriver: Mention the executable path of the webdriver you have downloaded
    # For linux/Mac
    driver = webdriver.Chrome(executable_path="//Driver/chromedriver", options = chrome_options)
    # For windows
    #driver = webdriver.Chrome(executable_path="./chromedriver.exe", options = chrome_options)
    return driver


def getCourses(driver, search_keyword):
    # Step 1: Go to pluralsight.com, category section with selected search keyword
    driver.get(f"https://www.pluralsight.com/search?q={search_keyword}&categories=course")
    # wait for the element to load
    try:
        WebDriverWait(driver, 5).until(lambda s: s.find_element_by_id("search-results-category-target").is_displayed())
    except TimeoutException:
        print("TimeoutException: Element not found")
        return None

    # Step 2: Create a parse tree of page sources after searching
    soup = BeautifulSoup(driver.page_source, "lxml")
    # Step 3: Iterate over the search result and fetch the course
    for course_page in soup.select("div.search-results-page"):
        for course in course_page.select("div.search-result"):
            title_selector = "div.search-result__info div.search-result__title a"
            author_selector = "div.search-result__details div.search-result__author"
            level_selector = "div.search-result__details div.search-result__level"
            length_selector = "div.search-result__details div.search-result__length"
            print({
                "title": course.select_one(title_selector).text,
                "author": course.select_one(author_selector).text,
                "level": course.select_one(level_selector).text,
                "length": course.select_one(length_selector).text,
            })

# create the driver object.
driver = configure_driver()
search_keyword = "Web Scraping"
getCourses(driver, search_keyword)
# close the driver.
driver.close()