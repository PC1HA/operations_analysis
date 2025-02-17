import pandas as pd
import logging
import os

directory = "C:/Users/PC1HA/My_Projects/operations analysis/logs"
file_path = os.path.join(directory, "log_data_search.json")


logging.basicConfig(
    filename=file_path,
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filemode='a',
    encoding="utf-8"
)

logger = logging.getLogger()


def load_transactions_from_excel(file_path: str) -> pd.DataFrame:
    """
    Загружает данные транзакций из Excel.

    Args:
        file_path (str): Путь к файлу Excel.

    Returns:
        pd.DataFrame: Датафрейм с данными транзакций.
    """
    try:
        df = pd.read_excel(file_path)
        logging.info("Данные успешно загружены из файла: %s", file_path)
        return df
    except Exception as e:
        logging.error("Ошибка при загрузке данных: %s", e)
        return pd.DataFrame()


def search_transactions(df: pd.DataFrame, query: str) -> str:
    """
    Ищет транзакции по запросу в описании или категории.

    Args:
        df (pd.DataFrame): Датафрейм с данными транзакций.
        query (str): Строка для поиска.

    Returns:
        str: JSON-ответ с найденными транзакциями.
    """
    query_lower = query.lower()
    logging.info("Поиск транзакций по запросу: %s", query)

    filtered_transactions = df[
        df['Описание'].str.contains(query_lower, case=False, na=False) |
        df['Категория'].str.contains(query_lower, case=False, na=False)
        ]

    if filtered_transactions.empty:
        logging.warning("Не найдено транзакций по запросу: %s", query)
    else:
        logging.info("Найдено %d транзакций по запросу: %s", len(filtered_transactions), query)

    json_response = filtered_transactions.to_json(orient='records', force_ascii=False, indent=4)

    return json_response
