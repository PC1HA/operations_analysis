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
