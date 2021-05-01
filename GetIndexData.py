import nsepy
from datetime import date
import pandas as pd


def NiftyEOD(startdate,enddate):
    nifty_val = nsepy.get_history(symbol="NIFTY", 
                    start=date(int(startdate[0:4]),int(startdate[4:6]),int(startdate[6:8])), 
                    end=date(int(enddate[0:4]),int(enddate[4:6]),int(enddate[6:8])),
					index=True)
    return(nifty_val)

