import os
import logging
from datetime import datetime
import pandas as pd
from typing import Dict, Any, Optional, List
from dotenv import load_dotenv


load_dotenv()


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


def get_greeting(current_time: datetime) -> str:
    """
    Возвращает приветствие в зависимости от времени суток.

    :param current_time: Текущая дата и время.
    :return: Приветствие в виде строки.
    """
    hour = current_time.hour
    if 5 <= hour < 12:
        greeting = "Доброе утро"
    elif 12 <= hour < 18:
        greeting = "Добрый день"
    elif 18 <= hour < 23:
        greeting = "Добрый вечер"
    else:
        greeting = "Доброй ночи"

    logger.info(f'Greeting returned: {greeting}')

    return greeting

def get_card_data(transactions: pd.DataFrame, analysis_date: Optional[str] = None) -> Dict[str, Dict[str, float]]:
    """
    Получает сводные данные по картам на основе транзакций за указанный месяц.

    :param transactions: DataFrame с данными о транзакциях.
    :param analysis_date: Дата для анализа в формате 'дд.мм.гггг'. Если не указана, используется текущая дата.
    :return: Словарь с итогами расходов и кешбека по картам.
    """
    if analysis_date is None:
        analysis_date = pd.Timestamp.now()
    else:
        analysis_date = pd.to_datetime(analysis_date, format='%d.%m.%Y')

    start_date = analysis_date.replace(day=1)
    end_date = analysis_date

    transactions['Дата операции'] = transactions['Дата операции'].str.strip()
    transactions['Дата операции'] = transactions['Дата операции'].str.split(' ').str[0]
    transactions['Дата операции'] = pd.to_datetime(transactions['Дата операции'], format='%d.%m.%Y', errors='coerce')

    unique_cards = transactions['Номер карты'].dropna().unique()
    card_summary = {str(card)[-4:]: {'total_spent': 0, 'cashback': 0} for card in unique_cards}

    filtered_transactions = transactions[(transactions['Дата операции'] >= start_date) & (transactions['Дата операции'] <= end_date)]

    for index, row in filtered_transactions.iterrows():
        card_number = str(row['Номер карты'])[-4:]
        amount_spent = row['Сумма операции'] if 'Сумма операции' in row else 0

        if card_number in card_summary:
            card_summary[card_number]['total_spent'] += amount_spent
            card_summary[card_number]['cashback'] += amount_spent // 100

    for card in card_summary:
        card_summary[card]['total_spent'] = round(card_summary[card]['total_spent'], 2)
        card_summary[card]['cashback'] = round(card_summary[card]['cashback'], 2)

    logger.info(f'Card summary: {card_summary}')
    return card_summary


def get_top_transactions(transactions: pd.DataFrame) -> List[Dict[str, Any]]:
    """
    Получает топ-5 транзакций по сумме платежа.

    :param transactions: DataFrame с данными о транзакциях.
    :return: Список словарей с данными о топ-5 транзакциях.
    """
    top_transactions = transactions.nlargest(5, 'Сумма платежа')
    result = top_transactions[['Дата платежа', 'Сумма платежа', 'Категория', 'Описание']].to_dict(orient='records')

    logger.info(f'Top transactions: {result}')
    return result
