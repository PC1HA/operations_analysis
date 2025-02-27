# operations_analysis

## Краткое описание

Данный проект представляет собой совокупностью функций
имитирующих работу реального банковского приложения
такого как Тинькофф(Т-банк)

## Установка и использование

- Для использования данной библиотеки необходимо иметь установленный Python версии 3.6 и выше.
Убедитесь, что у вас установлен пакет datetime, который входит в стандартную библиотеку Python.
- Склонируйте репозиторий:

    [git clone](https://github.com/PC1HA/operations_analysis)
- Убедитесь, что у вас установлен Python и необходимые библиотеки.
- Для корректной работы, надо поменять пути к файлам в ```views.py```, ```utils.py```
```spending_by_category.py```, ```services.py```, ```search.py```, 
```reports.py```, ```home_api.py```
- ```.env```
API_KEY=your_api_key_here
данные о валютах брал отсюда - "https://api.apilayer.com"
ALPHA_VANTAGE_API_KEY=your_api_key_here
данные об акциях брал тут - "https://www.alphavantage.co"
Вместо ```your_api_key_here``` вставьте свой ключ
## Примеры использования

### Файл main.py

```
Т БАНК    Частным лицам   Бизнесу   Премиум   Еще                    Личный кабинет

 Дебетовая карта, которую рекомендуют ваши друзья

 Кэшбэк рублями до 30%, переводы без комиссии

 Оформить карту

 Личный кабинет
 Интернет-банк
Логин:  admin
Пароль:  admin
Хотите посмотреть транзакции по картам по конкретной дате?
да или нет: нет
Анализируем данные...
Выстраиваем топ транзакций...
Получаем данные о курсе валют...
Смотрим, какие валюты есть...
Получаем данные об ценах на акции...
{'greeting': 'Добрый день',
 'cards':
  {
  '4615': {'total_spent': 0, 'cashback': 0},
  '8803': {'total_spent': 0, 'cashback': 0}
  },
   'top_transactions':
    [
    {'Дата платежа': '04.07.2023', 'Сумма платежа': 150000.0, 'Категория': 'Пополнения', 'Описание': 'Пополнение через НКО АО НРД'},
    {'Дата платежа': '28.08.2024', 'Сумма платежа': 147759.6, 'Категория': 'Кредиты', 'Описание': 'Получение кредита'},
    {'Дата платежа': '29.03.2023', 'Сумма платежа': 100000.0, 'Категория': 'Пополнения', 'Описание': 'Внесение наличных через банкомат Тинькофф'},
    {'Дата платежа': '11.04.2024', 'Сумма платежа': 41484.0, 'Категория': 'Переводы', 'Описание': 'Перевод между счетами'},
    {'Дата платежа': '11.04.2024', 'Сумма платежа': 41438.0, 'Категория': 'Переводы', 'Описание': 'Илья П.'}],
     'currency_rates':
      [
      {'currency': 'USD', 'rate': 86.79},
      {'currency': 'EUR', 'rate': 90.95},
      {'currency': 'CNY', 'rate': 11.93},
      {'currency': 'RUB', 'rate': 1.0}],
       'stock_prices':
        [
        {'stock': 'AAPL', 'price': 239.67}]}
Хотите воспользоваться простым поиском?да или нет:  да
Введите ключевое слово для поискапример: Инвесткопилка: инвесткопилка
Листаем файлы...
Ищу по вашему запросу...
[
    {
        "Дата операции":"12.08.2024 22:57:02",
        "Дата платежа":"13.08.2024",
        "Номер карты":null,
        "Статус":"OK",
        "Сумма операции":-3.0,
        "Валюта операции":"RUB",
        "Сумма платежа":-3.0,
        "Валюта платежа":"RUB",
        "Кэшбэк":null,
        "Категория":"Переводы",
        "MCC":null,
        "Описание":"Инвесткопилка",
        "Бонусы (включая кэшбэк)":0.0,
        "Округление на инвесткопилку":0,
        "Сумма операции с округлением":3.0
    },
    {
        "Дата операции":"12.07.2024 22:52:38",
        "Дата платежа":"13.07.2024",
        "Номер карты":null,
        "Статус":"OK",
        "Сумма операции":-53.0,
        "Валюта операции":"RUB",
        "Сумма платежа":-53.0,
        "Валюта платежа":"RUB",
        "Кэшбэк":null,
        "Категория":"Переводы",
        "MCC":null,
        "Описание":"Инвесткопилка",
        "Бонусы (включая кэшбэк)":0.0,
        "Округление на инвесткопилку":0,
        "Сумма операции с округлением":53.0
    },
    {
        "Дата операции":"12.06.2024 22:52:59",
        "Дата платежа":"13.06.2024",
        "Номер карты":null,
        "Статус":"OK",
        "Сумма операции":-141.0,
        "Валюта операции":"RUB",
        "Сумма платежа":-141.0,
        "Валюта платежа":"RUB",
        "Кэшбэк":null,
        "Категория":"Переводы",
        "MCC":null,
        "Описание":"Инвесткопилка",
        "Бонусы (включая кэшбэк)":0.0,
        "Округление на инвесткопилку":0,
        "Сумма операции с округлением":141.0
    },
    {
        "Дата операции":"12.05.2024 22:41:05",
        "Дата платежа":"13.05.2024",
        "Номер карты":null,
        "Статус":"OK",
        "Сумма операции":-100.0,
        "Валюта операции":"RUB",
        "Сумма платежа":-100.0,
        "Валюта платежа":"RUB",
        "Кэшбэк":null,
        "Категория":"Переводы",
        "MCC":null,
        "Описание":"Инвесткопилка",
        "Бонусы (включая кэшбэк)":0.0,
        "Округление на инвесткопилку":0,
        "Сумма операции с округлением":100.0
    },
    {
        "Дата операции":"12.04.2024 22:51:34",
        "Дата платежа":"13.04.2024",
        "Номер карты":null,
        "Статус":"OK",
        "Сумма операции":-105.0,
        "Валюта операции":"RUB",
        "Сумма платежа":-105.0,
        "Валюта платежа":"RUB",
        "Кэшбэк":null,
        "Категория":"Переводы",
        "MCC":null,
        "Описание":"Инвесткопилка",
        "Бонусы (включая кэшбэк)":0.0,
        "Округление на инвесткопилку":0,
        "Сумма операции с округлением":105.0
    },
    {
        "Дата операции":"12.03.2024 22:49:38",
        "Дата платежа":"13.03.2024",
        "Номер карты":null,
        "Статус":"OK",
        "Сумма операции":-147.0,
        "Валюта операции":"RUB",
        "Сумма платежа":-147.0,
        "Валюта платежа":"RUB",
        "Кэшбэк":null,
        "Категория":"Переводы",
        "MCC":null,
        "Описание":"Инвесткопилка",
        "Бонусы (включая кэшбэк)":0.0,
        "Округление на инвесткопилку":0,
        "Сумма операции с округлением":147.0
    },
    {
        "Дата операции":"12.02.2024 22:55:48",
        "Дата платежа":"13.02.2024",
        "Номер карты":null,
        "Статус":"OK",
        "Сумма операции":-175.0,
        "Валюта операции":"RUB",
        "Сумма платежа":-175.0,
        "Валюта платежа":"RUB",
        "Кэшбэк":null,
        "Категория":"Переводы",
        "MCC":null,
        "Описание":"Инвесткопилка",
        "Бонусы (включая кэшбэк)":0.0,
        "Округление на инвесткопилку":0,
        "Сумма операции с округлением":175.0
    },
    {
        "Дата операции":"12.09.2023 23:00:14",
        "Дата платежа":"13.09.2023",
        "Номер карты":null,
        "Статус":"OK",
        "Сумма операции":-70.0,
        "Валюта операции":"RUB",
        "Сумма платежа":-70.0,
        "Валюта платежа":"RUB",
        "Кэшбэк":null,
        "Категория":"Переводы",
        "MCC":null,
        "Описание":"Инвесткопилка",
        "Бонусы (включая кэшбэк)":0.0,
        "Округление на инвесткопилку":0,
        "Сумма операции с округлением":70.0
    },
    {
        "Дата операции":"12.08.2023 22:52:12",
        "Дата платежа":"13.08.2023",
        "Номер карты":null,
        "Статус":"OK",
        "Сумма операции":-4.0,
        "Валюта операции":"RUB",
        "Сумма платежа":-4.0,
        "Валюта платежа":"RUB",
        "Кэшбэк":null,
        "Категория":"Переводы",
        "MCC":null,
        "Описание":"Инвесткопилка",
        "Бонусы (включая кэшбэк)":0.0,
        "Округление на инвесткопилку":0,
        "Сумма операции с округлением":4.0
    },
    {
        "Дата операции":"12.04.2023 23:17:22",
        "Дата платежа":"13.04.2023",
        "Номер карты":null,
        "Статус":"OK",
        "Сумма операции":-14.0,
        "Валюта операции":"RUB",
        "Сумма платежа":-14.0,
        "Валюта платежа":"RUB",
        "Кэшбэк":null,
        "Категория":"Переводы",
        "MCC":null,
        "Описание":"Инвесткопилка",
        "Бонусы (включая кэшбэк)":0.0,
        "Округление на инвесткопилку":0,
        "Сумма операции с округлением":14.0
    },
    {
        "Дата операции":"12.03.2023 23:16:19",
        "Дата платежа":"13.03.2023",
        "Номер карты":null,
        "Статус":"OK",
        "Сумма операции":-6.0,
        "Валюта операции":"RUB",
        "Сумма платежа":-6.0,
        "Валюта платежа":"RUB",
        "Кэшбэк":null,
        "Категория":"Переводы",
        "MCC":null,
        "Описание":"Инвесткопилка",
        "Бонусы (включая кэшбэк)":0.0,
        "Округление на инвесткопилку":0,
        "Сумма операции с округлением":6.0
    }
]
Может бы хотите посмотреть траты по категориям?  да
Какая категория?Пример: Переводыпереводы
Посмотреть за определенный период?нет
Смотрим ваши траты...
None
```

## Ветка тестирования кода

### Папка tests

#### ```test_home_api.py```

```
import unittest
from unittest.mock import patch, Mock
from src.home_api import get_all_currencies, get_exchange_rate, get_stock_prices

class TestCurrencyFunctions(unittest.TestCase):

    @patch('src.home_api.requests.get')
    def test_get_all_currencies_success(self, mock_get: Mock) -> None:
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            'symbols': {
                'USD': 'United States Dollar',
                'EUR': 'Euro',
                'CNY': 'Chinese Yuan'
            }
        }
        mock_get.return_value = mock_response
        result = get_all_currencies('fake_api_key')
        expected_result = ['USD', 'EUR', 'CNY']
        self.assertEqual(result, expected_result)
        mock_get.assert_called_once_with("https://api.apilayer.com/exchangerates_data/symbols",
                                         headers={"apikey": 'fake_api_key'})

    @patch('src.home_api.requests.get')
    def test_get_all_currencies_failure(self, mock_get: Mock) -> None:
        mock_response = Mock()
        mock_response.status_code = 400
        mock_get.return_value = mock_response
        result = get_all_currencies('fake_api_key')
        expected_result = []
        self.assertEqual(result, expected_result)
        mock_get.assert_called_once()

    @patch('src.home_api.requests.get')
    @patch('src.home_api.get_all_currencies')
    def test_get_exchange_rate_success(self, mock_get_all_currencies: Mock, mock_get: Mock) -> None:
        mock_get_all_currencies.return_value = ['USD', 'EUR', 'CNY', 'JPY']
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            'rates': {
                'USD': 0.85,
                'EUR': 1.0,
                'CNY': 6.5,
                'JPY': 110.0
            }
        }
        mock_get.return_value = mock_response
        result = get_exchange_rate('RUB')
        expected_result = [
            {'currency': 'USD', 'rate': 1.18},
            {'currency': 'EUR', 'rate': 1.0},
            {'currency': 'CNY', 'rate': 0.15},
            {'currency': 'JPY', 'rate': 0.0091}
        ]
        self.assertEqual(len(result), 4)
        mock_get.assert_called_once()

    @patch('src.home_api.requests.get')
    def test_get_stock_prices_success(self, mock_get: Mock) -> None:
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            'Meta Data': {
                '3. Last Refreshed': '2023-10-01 16:00:00'
            },
            'Time Series (1min)': {
                '2023-10-01 16:00:00': {
                    '1. open': '150.00'
                }
            }
        }
        mock_get.return_value = mock_response
        result = get_stock_prices(['AAPL'])
        expected_result = [{'stock': 'AAPL', 'price': 150.0}]
        self.assertEqual(result, expected_result)
        mock_get.assert_called_once_with(
            "https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=AAPL&interval=1min&apikey=None"
        )

    @patch('src.home_api.requests.get')
    def test_get_stock_prices_failure(self, mock_get: Mock) -> None:
        mock_response = Mock()
        mock_response.status_code = 400
        mock_get.return_value = mock_response
        result = get_stock_prices(['AAPL'])
        expected_result = []
        self.assertEqual(result, expected_result)
        mock_get.assert_called_once()

```

#### ```test_search.py```

```
import unittest
from unittest.mock import patch, MagicMock
import pandas as pd
from src.search import load_transactions_from_excel, search_transactions


class TestTransactionFunctions(unittest.TestCase):

    @patch('pandas.read_excel')
    def test_load_transactions_from_excel_success(self, mock_read_excel: MagicMock) -> None:
        mock_read_excel.return_value = pd.DataFrame({
            'Описание': ['Транзакция 1', 'Транзакция 2'],
            'Категория': ['Категория A', 'Категория B']
        })
        df: pd.DataFrame = load_transactions_from_excel('fake_path.xlsx')
        self.assertIsInstance(df, pd.DataFrame)
        self.assertEqual(len(df), 2)
        self.assertEqual(df['Описание'][0], 'Транзакция 1')

    @patch('pandas.read_excel')
    def test_load_transactions_from_excel_failure(self, mock_read_excel: MagicMock) -> None:
        mock_read_excel.side_effect = Exception('File not found')
        df: pd.DataFrame = load_transactions_from_excel('fake_path.xlsx')
        self.assertIsInstance(df, pd.DataFrame)
        self.assertEqual(len(df), 0)

    def test_search_transactions_found(self) -> None:
        df: pd.DataFrame = pd.DataFrame({
            'Описание': ['Транзакция 1', 'Транзакция 2'],
            'Категория': ['Категория A', 'Категория B']
        })
        result_json: str = search_transactions(df, 'Транзакция 1')
        expected_json: str = '[\n    {\n        "Описание":"Транзакция 1",\n        "Категория":"Категория A"\n    }\n]'
        self.assertEqual(result_json, expected_json)

    def test_search_transactions_not_found(self) -> None:
        df: pd.DataFrame = pd.DataFrame({
            'Описание': ['Транзакция 1', 'Транзакция 2'],
            'Категория': ['Категория A', 'Категория B']
        })
        result_json: str = search_transactions(df, 'Транзакция 3')
        expected_json: str = '[]'
        self.assertEqual(result_json, expected_json)

    def test_search_transactions_case_insensitive(self) -> None:
        df: pd.DataFrame = pd.DataFrame({
            'Описание': ['Транзакция 1', 'Транзакция 2'],
            'Категория': ['Категория A', 'Категория B']
        })
        result_json: str = search_transactions(df, 'транзакция 1')
        expected_json: str = '[\n    {\n        "Описание":"Транзакция 1",\n        "Категория":"Категория A"\n    }\n]'
        self.assertEqual(result_json, expected_json)

```

#### ```test_spending_by_category.py```

```
import json
import unittest
import pandas as pd
from src.spending_by_category import get_expenses_by_category

class TestGetExpensesByCategoryWithNewData(unittest.TestCase):

    def setUp(self) -> None:
        self.test_data = [
            {
                "Дата операции": "31.01.2025 18:16:18",
                "Дата платежа": "31.01.2025",
                "Номер карты": None,
                "Статус": "OK",
                "Сумма операции": 1000.0,
                "Валюта операции": "RUB",
                "Сумма платежа": 1000.0,
                "Валюта платежа": "RUB",
                "Кэшбэк": None,
                "Категория": "Переводы",
                "MCC": None,
                "Описание": "Перевод между счетами",
                "Бонусы (включая кэшбэк)": 0.0,
                "Округление на инвесткопилку": 0,
                "Сумма операции с округлением": 1000.0
            }
        ]
        self.df: pd.DataFrame = pd.DataFrame(self.test_data)
        self.empty_df: pd.DataFrame = pd.DataFrame(columns=self.df.columns)

    def test_get_expenses_by_category_success(self) -> None:
        result_json: str = get_expenses_by_category(self.df, 'переводы')
        expected_json: str = json.dumps(self.test_data, ensure_ascii=False)
        self.assertEqual(json.loads(result_json), json.loads(expected_json))

    def test_get_expenses_by_category_empty_dataframe(self) -> None:
        result_json: str = get_expenses_by_category(self.empty_df, 'переводы')
        expected_json: str = json.dumps([], ensure_ascii=False)
        self.assertEqual(result_json, expected_json)

    def test_get_expenses_by_category_not_found(self) -> None:
        result_json: str = get_expenses_by_category(self.df, 'несуществующая категория')
        expected_json: str = json.dumps([], ensure_ascii=False)
        self.assertEqual(result_json, expected_json)

    def test_get_expenses_by_category_with_date_filter(self) -> None:
        custom_date: str = '2025-01-30'
        result_json: str = get_expenses_by_category(self.df, 'переводы', date=custom_date)
        expected_json: str = json.dumps([], ensure_ascii=False)
        self.assertEqual(result_json, expected_json)

```

#### ```test_utils.py```

```
import unittest
from unittest.mock import patch
import pandas as pd
from datetime import datetime
from typing import Any
from src.utils import get_greeting, get_card_data, get_top_transactions

class TestUtilsFunctions(unittest.TestCase):

    @patch('src.utils.logger')
    def test_get_greeting(self, mock_logger: Any) -> None:
        mock_logger.reset_mock()
        morning_time = datetime.strptime('2023-10-01 09:00:00', '%Y-%m-%d %H:%M:%S')
        self.assertEqual(get_greeting(morning_time), "Доброе утро")
        mock_logger.info.assert_called_once_with('Greeting returned: Доброе утро')

        mock_logger.reset_mock()
        afternoon_time = datetime.strptime('2023-10-01 15:00:00', '%Y-%m-%d %H:%M:%S')
        self.assertEqual(get_greeting(afternoon_time), "Добрый день")
        mock_logger.info.assert_called_once_with('Greeting returned: Добрый день')

        mock_logger.reset_mock()
        evening_time = datetime.strptime('2023-10-01 20:00:00', '%Y-%m-%d %H:%M:%S')
        self.assertEqual(get_greeting(evening_time), "Добрый вечер")
        mock_logger.info.assert_called_once_with('Greeting returned: Добрый вечер')

        mock_logger.reset_mock()
        night_time = datetime.strptime('2023-10-01 02:00:00', '%Y-%m-%d %H:%M:%S')
        self.assertEqual(get_greeting(night_time), "Доброй ночи")
        mock_logger.info.assert_called_once_with('Greeting returned: Доброй ночи')

    def setUp(self) -> None:
        self.test_data = {
            'Номер карты': ['3456', '4567', '1236'],
            'Дата операции': ['01.09.2023', '15.09.2023', '30.09.2023'],
            'Сумма операции': [2000, 1500, 1000],
            'Кэшбэк': [20, 15, 10]
        }
        self.transactions_df = pd.DataFrame(self.test_data)

    def test_get_card_data_no_analysis_date(self) -> None:
        expected_result = {
            '3456': {'total_spent': 0, 'cashback': 0},
            '4567': {'total_spent': 0, 'cashback': 0},
            '1236': {'total_spent': 0, 'cashback': 0}
        }
        result = get_card_data(self.transactions_df)
        self.assertEqual(result, expected_result)

    def test_get_card_data_with_analysis_date(self) -> None:
        expected_result = {
            '1236': {'total_spent': 1000, 'cashback': 10},
            '3456': {'total_spent': 2000, 'cashback': 20},
            '4567': {'total_spent': 1500, 'cashback': 15},
        }
        result = get_card_data(self.transactions_df, analysis_date='30.09.2023')
        self.assertEqual(result, expected_result)

    def test_get_top_transactions(self) -> None:
        test_data = {
            'Дата платежа': ['2023-10-01', '2023-09-15', '2023-10-02', '2023-09-30', '2023-09-10', '2023-08-15'],
            'Сумма платежа': [1000, 1500, 2000, 2500, 3000, 500],
            'Категория': ['Еда', 'Транспорт', 'Развлечения', 'Еда', 'Транспорт', 'Еда'],
            'Описание': ['Покупка 1', 'Покупка 2', 'Покупка 3', 'Покупка 4', 'Покупка 5', 'Покупка 6']
        }
        transactions_df = pd.DataFrame(test_data)

        expected_result = [
            {'Дата платежа': '2023-09-10', 'Сумма платежа': 3000, 'Категория': 'Транспорт', 'Описание': 'Покупка 5'},
            {'Дата платежа': '2023-09-30', 'Сумма платежа': 2500, 'Категория': 'Еда', 'Описание': 'Покупка 4'},
            {'Дата платежа': '2023-10-02', 'Сумма платежа': 2000, 'Категория': 'Развлечения', 'Описание': 'Покупка 3'},
            {'Дата платежа': '2023-09-15', 'Сумма платежа': 1500, 'Категория': 'Транспорт', 'Описание': 'Покупка 2'},
            {'Дата платежа': '2023-10-01', 'Сумма платежа': 1000, 'Категория': 'Еда', 'Описание': 'Покупка 1'}
        ]

        result = get_top_transactions(transactions_df)
        self.assertEqual(result, expected_result)

```

## Лицензия

### MIT License

**Copyright (c) 2025 Попов Илья Игоревич**

*Разрешение предоставляется, бесплатно, любому, кто получает копию этого программного обеспечения и*
*связанных с ним документов (далее — "Программное обеспечение"), использовать Программное обеспечение без ограничений,*
*включая, но не ограничиваясь правами на использование, копирование, изменение, слияние, публикацию, распространение,*
*сублицензирование и/или продажу копий Программного обеспечения, а также разрешение лицам,*
*которым предоставляется Программное обеспечение, делать это, при соблюдении следующих условий:*

*Вышеуказанное уведомление о авторских правах и это разрешение должны быть включены во все копии или*
*значительные части Программного обеспечения.*

*Программное обеспечение предоставляется "как есть", без каких-либо гарантий, явных или подразумеваемых, включая,*
*но не ограничиваясь, гарантии товарной пригодности, соответствия определенной цели и ненарушения.*
*В любом случае авторы или правообладатели не несут ответственности за любые претензии, ущерб или*
*другие обязательства, будь то в действии, контракте или ином, возникающие из,*
*в связи с или в результате использования Программного обеспечения или других действий с ним.*