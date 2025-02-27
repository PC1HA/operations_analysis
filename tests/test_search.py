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
