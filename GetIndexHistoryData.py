import nsepy
from datetime import date
import pandas as pd

date_list = ()

nifty_val = nsepy.get_history(symbol="NIFTY", 
                    start=date(2020,9,23), 
                    end=date(2021,4,10),
					index=True)

print(nifty_val)

