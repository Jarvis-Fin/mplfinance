"""
Show how to make date plots in matplotlib using date tick locators and
formatters.  See major_minor_demo1.py for more information on
controlling major and minor ticks
"""

import matplotlib.pyplot as plt
import pandas as pd
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()
from matplotlib.dates import (MONDAY, DateFormatter, MonthLocator,
                              WeekdayLocator)
import os.path
import io

def test_date_demo2():

    date1 = "2002-1-5"
    date2 = "2003-12-1"
    
    # every monday
    mondays = WeekdayLocator(MONDAY)
    
    # every 3rd month
    months = MonthLocator(range(1, 13), bymonthday=1, interval=3)
    monthsFmt = DateFormatter("%b '%y")
    
    
    infile = os.path.join('examples','data','yahoofinance-INTC-19950101-20040412.csv')
    quotes = pd.read_csv(infile,
                         index_col=0,
                         parse_dates=True,
                         infer_datetime_format=True)
    
    # select desired range of dates
    quotes = quotes[(quotes.index >= date1) & (quotes.index <= date2)]
    
    dates = quotes.index
    opens = quotes['Open']
    
    
    fig, ax = plt.subplots()
    ax.plot_date(dates, opens, '-')
    ax.xaxis.set_major_locator(months)
    ax.xaxis.set_major_formatter(monthsFmt)
    ax.xaxis.set_minor_locator(mondays)
    ax.autoscale_view()
    # ax.xaxis.grid(False, 'major')
    # ax.xaxis.grid(True, 'minor')
    ax.grid(True)
    
    fig.autofmt_xdate()
    
    buf = io.BytesIO()
    plt.savefig(buf)
