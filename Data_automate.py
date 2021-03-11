#Importing packages
#command to install selenium - pip install selenium
from selenium import webdriver
#command to install BeautifulSoup - pip install BeautifulSoup4
from bs4 import BeautifulSoup
#command to install pandas - pip install pandas
import pandas as pd


#Path in your computer where you have installed chromedriver
driver = webdriver.Chrome('C:\Program Files (x86)\chromeDriver\chromedriver.exe')

#Accessing website through chrome automatedly

divs=[] #List all button of the product
#prices=[] #List to store price of the product
#ratings=[] #List to store rating of the product
driver.get("http://marketingdoctor.ca/")
# Extract the Data
content = driver.page_source
soup = BeautifulSoup(content,"html.parser")

#OLD CODE
#for div in soup.findAll('div',href=True, attrs={'class':'et_pb_section'}):
#    button=a.find('a', attrs={'class':'et_pb_button'})
#    price=a.find('div', attrs={'class':'_1vC4OE _2rQ-NK'})
#    rating=a.find('div', attrs={'class':'hGSR34 _2beYZw'})
#    buttons.append(button.text)
#    prices.append(price.text)
#    ratings.append(rating.text) 
# END OF OLD CODE 

mydivs = soup.find_all("div", {"class": "et_pb_row"})
divs.append(mydivs)

# Store the Data
df = pd.DataFrame({'Divs html':divs}) 
df.to_csv('divs.csv', index=False, encoding='utf-8')