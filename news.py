#Pandas - Data analysis library used to create and manipulate data
# within structures called dataframes

#Requests - An HTTP library for Python with a built-in JSON decoder

#Datetime - Functions to create & format date and time objects in Python

#Calendar - Contains a method to retrieve the # of days in a month given a year

import requests, pandas, datetime, calendar

activeUrl = https://www.nasdaq.com/market-activity/stocks/screener
req = requests.get(activeUrl)
data = req.text
soup = BeautifulSoup(data)

table = soup.find_all('div', attrs={&quot})