# Importing all necessery packages
import requests
from bs4 import BeautifulSoup
import urllib.request, urllib.error
import pandas as pd

# creating a empty list for all the link extensions
company_extension = []

# for loop to test the company IDs; I split into four parts
# You can also just use one for loop, by changing your range to (0,30_000)
"""

for i in range(100,10000):
    company_extension.append(i)
for i in range(10001,20000):
    company_extension.append(i)
for i in range(20001,30000):
    company_extension.append(i)

"""
for i in range(0,100):
    company_extension.append(i)

# creating an empty list to store the links
links = []

links = ["https://www.ycombinator.com/companies/" + str(a) for a in company_extension]

working_links = []

## for loop to check is url valid and not; if valid the url will be stored in new list
for url in links:

    try:
        conn = urllib.request.urlopen(url)
    except urllib.error.HTTPError as e:
        # Return code error (e.g. 404, 501, ...)
        # ...
        print('HTTPError: {}'.format(e.code))
    except urllib.error.URLError as e:
        # Not an HTTP-specific error (e.g. connection refused)
        # ...
        print('URLError: {}'.format(e.reason))
    else:
        # 200
        # ...
        print('good')
        working_links.append(url)

df_working_links = pd.DataFrame(working_links)

## Saving the links into a csv file
df_working_links.to_csv("working_links_0-100.csv")
