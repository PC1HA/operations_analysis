import requests
import os
import logging
import random
from typing import List, Dict, Union, Any

directory = "C:/Users/PC1HA/My_Projects/operations analysis/logs"
file_path = os.path.join(directory, "log_data_home.json")


logging.basicConfig(
    filename=file_path,
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filemode='a',
    encoding="utf-8"
)

logger = logging.getLogger()


def get_all_currencies(api_key: str) -> List[str]:
    """
    Получает список всех доступных валют из API.

    Args:
        api_key (str): API ключ для доступа к API.

    Returns:
        List[str]: Список всех доступных валют.
    """
    print("Смотрим, какие валюты есть...")

    url = "https://api.apilayer.com/exchangerates_data/symbols"
    headers = {
        "apikey": api_key
    }
    logger.info('Запрос на получение всех валют')

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        logger.info('Успешно получен список валют')
        return list(data['symbols'].keys())
    else:
        logger.error(f"Ошибка при получении валют: {response.status_code}")
        return []


def get_exchange_rate(base_currency: str = 'RUB') -> List[Dict[str, Union[str, None]]]:
    """
    Получает текущий курс обмена из API.

    Args:
        base_currency (str): Исходная валюта. По умолчанию 'RUB'.

    Returns:
        List[Dict[str, Union[str, None]]]: Список словарей с курсами обмена для целевых валют.
    """
    print("Получаем данные о курсе валют...")

    target_currency = ['USD', 'EUR', 'CNY']
    api_key = os.getenv('API_KEY')

    logger.info(f'Получение курсов обмена для валют с базой {base_currency}')
    # Получаем все доступные валюты
    all_currencies = get_all_currencies(api_key)

    # Выбираем случайную валюту, которая не совпадает с уже имеющимися
    random_currency = random.choice(all_currencies)
    while random_currency in target_currency:
        random_currency = random.choice(all_currencies)

    # Добавляем случайную валюту в список
    target_currency.append(random_currency)

    rates = []
    url = (f"https://api.apilayer.com/exchangerates_data/latest?base="
           f"{base_currency}&symbols={','.join(target_currency)}")
    headers = {
        "apikey": api_key
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        for currency in target_currency:
            rate = data['rates'].get(currency)
            if rate is not None:
                # Преобразуем курс в нужный формат
                formatted_rate = round(1 / rate, 2)  # Обратное значение для отображения
                rates.append({"currency": currency, "rate": formatted_rate })
                logger.info(f'Курс для {currency}: {formatted_rate}')
            else:
                rates.append({"currency": currency, "rate": None})
                logger.warning(f'Курс для {currency} не найден')
    else:
        logger.error(f"Ошибка при получении данных: {response.status_code}")
        print(f"Ошибка при получении данных: {response.status_code}")
        for currency in target_currency:
            rates.append({"currency": currency, "rate": None})

    return rates


def get_stock_prices(stock_symbols: List[str]) -> List[Dict[str, Any]]:
    """
    Получает последние цены акций для заданных символов акций с использованием API Alpha Vantage.

    :param stock_symbols: Список символов акций, для которых необходимо получить цены.
    :return: Список словарей, каждый из которых содержит символ акции и его последнюю цену.
    """
    print("Получаем данные об ценах на акции...")

    stock_prices = []
    api_key = os.getenv('ALPHA_VANTAGE_API_KEY')

    for symbol in stock_symbols:
        url = (f"https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol="
               f"{symbol}&interval=1min&apikey={api_key}")
        logger.info(f'Запрос цен акций для символа {symbol}')
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            try:
                # Получаем последнюю запись
                last_refreshed = data['Meta Data']['3. Last Refreshed']
                last_price = data['Time Series (1min)'][last_refreshed]['1. open']
                stock_prices.append({"stock": symbol, "price": float(last_price)})
                logger.info(f'Полученная цена для {symbol}: {last_price}')
            except KeyError:
                logger.error(f'Ошибка получения данных для {symbol}: {data.get("Note", "Неизвестная ошибка")}')
        else:
            logger.error(f"Ошибка при запросе данных для {symbol}: {response.status_code}")

    return stock_prices
