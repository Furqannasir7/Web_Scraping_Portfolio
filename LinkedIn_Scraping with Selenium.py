import parameters
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from parsel import Selector

driver = webdriver.Chrome('//Driver/chromedriver')
driver.get('https://www.linkedin.com')

username = driver.find_element_by_class_name('input__input')
username.send_keys(parameters.linkedin_username)
sleep(0.5)

password = driver.find_element_by_id('session_password')
password.send_keys(parameters.linkedin_password)
sleep(0.5)

sign_in_button = driver.find_element_by_xpath('//*[@type="submit"]')
sign_in_button.click()
sleep(0.5)

driver.get('https:www.google.com')
sleep(3)

search_query = driver.find_element_by_name('q')
search_query.send_keys(parameters.search_query)
sleep(0.5)

search_query.send_keys(Keys.RETURN)
sleep(3)

linkedin_urls = driver.find_elements_by_class_name('iUh30')
linkedin_urls = [url.text for url in linkedin_urls]
sleep(0.5)

driver.quit()

driver.get('https://uk.linkedin.com/in/pauljgarner')

driver.page_source

# continuing on from before
...
linkedin_urls = [url.text for url in linkedin_urls]
sleep(0.5)


# For loop to iterate over each URL in the list
for linkedin_url in linkedin_urls:

   # get the profile URL
   driver.get(linkedin_url)

   # add a 5 second pause loading each URL
   sleep(5)

   # assigning the source code for the webpage to variable sel
   sel = Selector(text=driver.page_source)

# terminates the application
driver.quit()

#xpath to extract the first h1 text
name = sel.xpath('//h1/text()').extract_first()

# xpath to extract the exact class containing the text
name = sel.xpath('//*[starts-with(@class, "pv-top-card-section__name")]/text()').extract_first()

# xpath to extract the text from the class containing the name
#name = sel.xpath('//*[starts-with(@class,
#"pv-top-card-section__name")]/text()').extract_first()

#if name:
 #   name = name.strip()


# xpath to extract the text from the class containing the job title
#job_title = sel.xpath('//*[starts-with(@class,
#"pv-top-card-section__headline")]/text()').extract_first()

#if job_title:
 #   job_title = job_title.strip()


# xpath to extract the text from the class containing the company
#company = sel.xpath('//*[starts-with(@class,
#"pv-top-card-v2-section__entity-name pv-top-card-v2-section__company-name")]/text()').extract_first()

#if company:
 #   company = company.strip()


# xpath to extract the text from the class containing the college
#college = sel.xpath('//*[starts-with(@class,
#"pv-top-card-v2-section__entity-name pv-top-card-v2-section__school-name")]/text()').extract_first()

#if college:
 #   college = college.strip()


# xpath to extract the text from the class containing the location
#location = sel.xpath('//*[starts-with(@class,
#"pv-top-card-section__location")]/text()').extract_first()

#if location:
 #   location = location.strip()


linkedin_url = driver.current_url

# printing the output to the terminal
print('\n')
print('Name: ' + name)
#print('Job Title: ' + job_title)
#print('Company: ' + company)
#print('College: ' + college)
#print('Location: ' + location)
#print('URL: ' + linkedin_url)
print('\n')

# defining new variable passing two parameters
#writer = csv.writer(open(parameters.file_name, 'wb'))

# writerow() method to the write to the file object
#writer.writerow(['Name','Job Title','Company','College', 'Location','URL'])

# writing the corresponding values to the header
#writer.writerow([name.encode('utf-8'),
 #                job_title.encode('utf-8'),
   #               company.encode('utf-8'),
    #             college.encode('utf-8'),
     #            location.encode('utf-8'),
      #           linkedin_url.encode('utf-8')])

# function to ensure all key data fields have a value
def validate_field(field):# if field is present pass if field:pass
# if field is not present print text else:
       field = 'No results'
#return field

# validating if the fields exist on the profile
name = validate_field(name)
#job_title = validate_field(job_title)
#company = validate_field(company)
#college = validate_field(college)
#location = validate_field(location)
#linkedin_url = validate_field(linkedin_url)



