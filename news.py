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

    def scraper(self, dateStr):
        '''
        Scrapes JSON object from page using requests module
        Parameters
        ----------
        url: URL string
        headers: Header info.
        dateStr: string in yyyy-mm-dd format

        Returns
        -------
        dictionary: Returns a JSON dictionary at a given URL.

        Scraping information from JSON objects can be faster and more 
        convenient than parsing HTML data using XPaths.
        '''

        params = {'date': dateStr}
        page = requests.get(self.url, headers= self.headers, params=params)
        dictionary = page.json()
        return dictionary

    def dateStr(self, day):
        date_obj = datetime.date(self.year, self.month, day)
        date_str = date_obj.strftime(format ='%Y-%m-%d')
        return date_str

    def dict_to_df(self, dicti):
        '''
        Converts the JSON dictionary into a pandas dataframe.
        Appends the dataframe to calendars class attribute

        Parameters
        ----------
        dicti: Output from the scraper method as input .

        Returns
        -------
        calendar: Dataframe of stocks with that exdividend date

        Will append a dataframe to the calendars list (clas
        attribute). otherwise, it will return an empty dataframe.
        '''

        rows = dicti.get('data').get('calendar').get('rows')
        calendar = pandas.DataFame(rows)
        self.calendar.append(calendar) 
        #append df to calendars
        return calendar

    def calendar(self, day):
        '''
        Combines the date_str, scraper, and dict_to_df methods

        Parameters
        ----------
        day: day of the month as a string/number.

        Returns
        -------
        dictionary: Returns a JSON dictionary with keys
        dictionary.keys() => data, message, status

        Net Levels:
        dictionary['data'].keys() => calendar, timeframe
        dictionary['data']['calendar'].keys() => headers, rows
        dictionary['data']['calendar]['headers'] => column names
        dictionary['data']['calendar']['rows'] => dictionary list

        '''

        day = int(day)
        date_str = self.date_str(day)
        dictionary = self.scraper(date_str)
        self.dict_to_df(dictionary)
        reutrn dictionary
