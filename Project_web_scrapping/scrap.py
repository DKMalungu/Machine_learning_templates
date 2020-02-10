#
# Core Libraries
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd 

#Configuring webdriver
driver = webdriver.Chrome('/usr/bin/chromedriver')

# Items lists to scrap
product_name = [] #Name of the product
current_price = [] #Price of the product 
discount = [] # Product discount 
features = [] # Product features
driver.get('https://www.masoko.com/all-categories/phones-tablets/mobile-phones')

# Extracting the data fro the website
content = driver.page_source
soup = BeautifulSoup(content)
for a in soup.findAll('a',href=True, attrs={'class':'productListingList'}):
    name=a.find('div',attrs={'class':'MuiTypography-root jss544 MuiTypography-body1'},features="lxml")
    price=a.find('p',attrs={'class':"MuiGrid-root MuiGrid-item MuiGrid-grid-xs-8"})
    dis=a.find('p',attrs={'class':'MuiTypography-root jss557 false MuiTypography-body1'})
    fea=a.find('p',attrs={'class':'MuiTypography-root jss545 MuiTypography-body2'})
    product_name.append(name.text)
    current_price.append(price.text)
    discount.append(dis.text)
    features.append(fea.text)


df = pd.DataFrame({'Product Name':product_name,'Price':current_price,'Discount':discount,'Features':features}) 
df.to_csv('products.csv', index=False, encoding='utf-8')SSSSSS