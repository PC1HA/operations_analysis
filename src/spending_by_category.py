import os
import pandas as pd
import logging
from datetime import datetime


directory = "C:/Users/PC1HA/My_Projects/operations analysis/logs"
file_path = os.path.join(directory, "log_data_category.json")

logging.basicConfig(
    filename=file_path,
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filemode='a',
    encoding="utf-8"
)

logger = logging.getLogger()


def get_expenses_by_category(df: pd.DataFrame, category: str, date: str = None) -> str:
    """
    Возвращает траты по заданной категории за последние три месяца.

    Args:
        df (pd.DataFrame): Датафрейм с данными транзакций.
        category (str): Название категории для фильтрации.
        date (str, optional): Дата в формате 'YYYY-MM-DD'. Если не указана, используется текущая дата.

    Returns:
        str: JSON-ответ с найденными транзакциями.
    """
    if date is None:
        date = datetime.now().strftime('%Y-%m-%d')

    current_date = pd.to_datetime(date)
    three_months_ago = current_date - pd.DateOffset(months=3)

    filtered_transactions = df[
        (df['Категория'].str.contains(category, case=False, na=False)) &
        (pd.to_datetime(df['Дата платежа'], dayfirst=True) >= three_months_ago) &
        (pd.to_datetime(df['Дата платежа'], dayfirst=True) <= current_date)
        ]

    if filtered_transactions.empty:
        logging.warning("Не найдено транзакций по категории: %s за последние три месяца", category)
    else:
        logging.info("Найдено %d транзакций по категории: %s за последние три месяца", len(filtered_transactions),
                     category)

    json_response = filtered_transactions.to_json(orient='records', force_ascii=False, indent=4)

    return json_response
