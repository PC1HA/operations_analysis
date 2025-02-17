import os
from src.utils import get_card_data, get_top_transactions, get_greeting
from src.home_api import get_exchange_rate, get_stock_prices
import pandas as pd
from datetime import datetime
import json

if __name__ == "__main__":
    transactions = pd.read_excel('C:/Users/PC1HA/My_Projects/operations analysis/data/my_operations.xls')

    greeting = get_greeting(datetime.now())
    cards = get_card_data(transactions)
    top_transactions = get_top_transactions(transactions)
    currency_rates = get_exchange_rate()
    stock_prices = get_stock_prices(["AAPL", "AMZN", "GOOGL", "MSFT", "TSLA"])

    data = {
        "greeting": greeting,
        "cards": cards,
        "top_transactions": top_transactions,
        "currency_rates" : currency_rates,
        "stock_prices": stock_prices
    }
    directory  = "C:/Users/PC1HA/My_Projects/operations analysis/data"
    file_path = os.path.join(directory, "data_home.json")
    json_str = json.dumps(data, ensure_ascii=False, indent=4)
    with open(file_path, "w", encoding="utf-8") as json_file:
        json_file.write(json_str)