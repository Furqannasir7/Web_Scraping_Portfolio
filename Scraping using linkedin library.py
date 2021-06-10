from linkedin_scraper import Person, actions
from selenium import webdriver

driver = webdriver.Chrome('//Driver/chromedriver')

email = "nasirfurqan29@gmail.com"
password = "55552222BILLU"

actions.login(driver, email, password) # if email and password isnt given, it'll prompt in terminal
#This will take you to that person profile link (User Scraping)
person = Person("https://www.linkedin.com/in/andre-iguodala-65b48ab5", driver=driver,scrape=False)

person.scrape(close_on_complete=False)
#API
#A Person object can be created with the following inputs:
#Person(linkedin_url=None, name=None, about=[], experiences=[], educations=[], interests=[], accomplishments=[], company=None, job_title=None, driver=None, scrape=True)
#For Company
#Company(linkedin_url=None, name=None, about_us=None, website=None, headquarters=None, founded=None, company_type=None, company_size=None, specialties=None, showcase_pages=[], affiliated_companies=[], driver=None, scrape=True, get_employees=True)

