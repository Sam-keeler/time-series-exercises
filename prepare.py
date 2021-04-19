import pandas as pd
from datetime import timedelta, datetime
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings("ignore")

import requests

def prepare_items(df):
    df['sale_date'] = pd.to_datetime(df.sale_date)
    df = df.set_index('sale_date').sort_index()
    df['month'] = df.index.month
    df['day_of_week'] = df.index.day_name()
    df['sales_total'] = df.sale_amount * df.item_price
    return df

def prep_power(power):
    power['Date'] = power.Date.apply(lambda x: pd.to_datetime(x))
    power = power.set_index('Date').sort_index()
    power['year'] = power.index.year
    power['month'] = power.index.month
    power = power.fillna(0)
    return power