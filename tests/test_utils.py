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
