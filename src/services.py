import os
from src.search import load_transactions_from_excel, search_transactions


if __name__ == "__main__":
    file_path = 'C:/Users/PC1HA/My_Projects/operations analysis/data/my_operations.xls'
    query = 'Инвесткопилка'

    transactions_df = load_transactions_from_excel(file_path)

    if not transactions_df.empty:
        result = search_transactions(transactions_df, query)
        directory = "C:/Users/PC1HA/My_Projects/operations analysis/data"
        file_path = os.path.join(directory, "data_search.json")
        with open(file_path, "w", encoding="utf-8") as json_file:
            json_file.write(result)
    else:
        result = "Нет данных для поиска."
        directory = "C:/Users/PC1HA/My_Projects/operations analysis/data"
        file_path = os.path.join(directory, "data_search.json")
        with open(file_path, "w", encoding="utf-8") as json_file:
            json_file.write(result)
