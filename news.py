#Pandas - Data analysis library used to create and manipulate data
# within structures called dataframes

#Requests - An HTTP library for Python with a built-in JSON decoder

#Datetime - Functions to create & format date and time objects in Python

#Calendar - Contains a method to retrieve the # of days in a month given a year

import requests, pandas, datetime, calendar

class DivCalendar:
    #class attributes
    calendar = []
    url = 'https://api.nasdaq.com/api/calendar/dividends'
    headers = {'Accept': 'application/jsopn, text/plain, */*', 
                'DNT': "1", 
                'Origin': 'https://www.nasdaq.com/',
                'Sec-Fetch-Mode': 'cors', 
                'User-Agent': 'Mozilla/5.0 (Macintosh)'}
    
    def __init__(self, year, month):
        '''
        Parameters
        ----------
        year: of type int
        month: of type int
        Returns
        -------
        Sets instance attributes for year and month of objects.
        '''

        #instance attributes
        self.year = int(year)
        self.month = int(month)