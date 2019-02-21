# -*- coding: utf-8 -*-
"""
Created on Tue Feb 19 10:26:41 2019

@author: Christian.GANDON
"""
import requests as requests
import pandas as pd
import os
from urllib.parse import urlparse
import urllib.request

# go to https://cse.google.fr to create your own custom search engine (free) 
# create a key.txt file in root folder and store your Google API key in it
# create a cse.txt file in root folder and store your Google CSE code in it
f_key = open("key.txt", "r") 
f_cse = open("cse.txt", "r") 

key = f_key.read() 
cse = f_cse.read()

# this is the google query 
q = 'boucheron+quatre+bague'

# the "bank" will be the consolidated list of images URL
bank = []

# API works with pagination, fetching results 10 by 10, up to 100 results (hard constraint). We'll loop and call the API wiht incremental 'startIndex'
startIndex = 1

while startIndex < 100:
    function url ()
    url = 'https://www.googleapis.com/customsearch/v1?' + 'key=' + key + '&cx=' + cse + '&q=' + q + '&searchType=image' + '&start=' + str(startIndex) 
    result = requests.request("GET", url)
    images = result.json()
#loop over the 10 results and append to your image bank
    for i in range(len(images['items'])):
        bank.append(images['items'][i]['link'])
#search returns results by groups of 10, increment for next run
    startIndex += 10
    print(startIndex)


# our "bank" of images is filled, now we can proceed and loop over the bank to download the files
    
for i in range(len(bank)):
    try:
        file_path = urlparse(bank[i]) 
        #split file extension from root...
        (root, ext) = os.path.splitext(file_path.path)
        #rebuild your path with generic incremental number to avoid errors during file saving 
        path = q +"_"+str(i) + ext
    except Exception as e:
        print(e)
        continue 
    try:
        urllib.request.urlretrieve(bank[i], os.path.basename(path))
    except Exception as e:
        print(path)
        print(e)
    continue


