#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Importing libraries
import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup
from urllib.request import urlopen

# Getting the HTML of the page of intreset
url = 'https://www.kilimall.co.ke/new/commoditysearch?c=1057&aside=Phones%20%26%20Accessories&gc_id=1057'
html = urlopen(url)

# Creating Beautiful Soup 
soup = BeautifulSoup(html,'lxml')
print(type(soup))

#Getting the page title
title = soup.title
print(title)

# Page Text
text = soup.get_text()
print(text)

# Extracting useful html tages within the webpage
soup.find_all('div')

#Getting additional information from html tags
all_links = soup.find_all('a')
for link in all_links:
    print(link.find('p'))
    #print(link.get('class'))





