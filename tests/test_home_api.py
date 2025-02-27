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
