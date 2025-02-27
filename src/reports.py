from src.spending_by_category import get_expenses_by_category
import pandas as pd
import os


def reports():
    file_path = 'C:/Users/PC1HA/My_Projects/operations analysis/data/my_operations.xls'
    transactions_df = pd.read_excel(file_path)


    category = input('Какая категория?'
                     'Пример: Переводы' )
    question = input('Посмотреть за определенный период?'  )

    if question.lower() == 'да':
        date = input("Введите дату в формате"
                     "Дата в формате 'YYYY-MM-DD' " )
        result = get_expenses_by_category(transactions_df, category, date)
    else:
        result = get_expenses_by_category(transactions_df, category)

    directory = "C:/Users/PC1HA/My_Projects/operations analysis/data"
    file_path = os.path.join(directory, "data_category.json")
    with open(file_path, "w", encoding="utf-8") as json_file:
        json_file.write(result)