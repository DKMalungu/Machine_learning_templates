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
driver.get('https://www.kilimall.co.ke/new/commoditysearch?c=1057&aside=Phones%20%26%20Accessories&gc_id=1057')

# Extracting the data fro the website
content = driver.page_source
soup = BeautifulSoup(content)
for a in soup.findAll('a',href=True, attrs={'class':'productListingList'}):
    name=a.find('a',attrs={'class':'MuiTypography-root jss394 MuiTypography-body1'})
    price=a.find('p',attrs={'class':"MuiTypography-root jss413 false MuiTypography-body1"})
    dis=a.find('p',attrs={'class':'MuiTypography-root jss407 false MuiTypography-body1'})
    fea=a.find('p',attrs={'class':'MuiTypography-root jss545 MuiTypography-body2'})
    product_name.append(name)
    current_price.append(price)
    discount.append(dis)
    features.append(fea)


df = pd.DataFrame({'Product Name':product_name,'Price':current_price,'Discount':discount,'Features':features}) 
df.to_csv('products.csv', index=False, encoding='utf-8')