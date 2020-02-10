#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Importing libraries
import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup
from urllib.request import urlopen

# Getting the HTML of the page of intreset
url = 'https://www.masoko.com/all-categories/phones-tablets/mobile-phones'
html = urlopen(url)
