import requests
import pandas as pd

def get_items(cached = False):
    if cached == False:
        items = []
        url = "https://python.zach.lol/api/v1/items"

        response = requests.get(url)
        data = response.json()
        n = data['payload']['max_page']


        for i in range(1, n+1):
            new_url = url + '?page=' + str(i)
            response = requests.get(new_url)
            data = response.json()
            page_items = data['payload']['items']
            items += page_items

        return pd.DataFrame(items)
    else:
        return pd.read_csv('items.csv', index_col = 0)

def get_stores(cached = False):
    if cached == False:
        stores = []
        url = "https://python.zach.lol/api/v1/stores"

        response = requests.get(url)
        data = response.json()
        n = data['payload']['max_page']


        for i in range(1, n+1):
            new_url = url + '?page=' + str(i)
            response = requests.get(new_url)
            data = response.json()
            page_items = data['payload']['stores']
            stores += page_items

        return pd.DataFrame(stores)
    else:
        return pd.read_csv('stores.csv', index_col = 0)

def get_sales(cached = False):
    if cached == False:
        sales = []
        url = "https://python.zach.lol/api/v1/sales"

        response = requests.get(url)
        data = response.json()
        n = data['payload']['max_page']


        for i in range(1, n+1):
            new_url = url + '?page=' + str(i)
            response = requests.get(new_url)
            data = response.json()
            page_items = data['payload']['sales']
            sales += page_items

        return pd.DataFrame(sales)
    else:
        return pd.read_csv('sales.csv', index_col = 0)

def store_them(sales, stores, items):
    sales.to_csv('sales.csv')
    stores.to_csv('stores.csv')
    items.to_csv('items.csv')

def complete_data(cached=False):
    if cached == False:
        items = get_items(cached=True)
        stores = get_stores(cached=True)
        sales = get_sales(cached=True)
        sales.columns = ['item_id', 'sale_amount', 'sale_date', 'sale_id', 'store_id']
        complete_data = sales.merge(stores, on='store_id')
        complete_data = complete_data.merge(items, on='item_id')
        complete_data.to_csv('complete_data.csv')
    else:
        complete_data = pd.read_csv('complete_data.csv', index_col=0)
    return complete_data