from src.views import home
from src.services import services_search
from src.reports import reports


front_page = (
    "Т БАНК    Частным лицам   Бизнесу   Премиум   Еще                    Личный кабинет"
    "\n\n Дебетовая карта, которую рекомендуют ваши друзья"
    "\n\n Кэшбэк рублями до 30%, переводы без комиссии"
    "\n\n Оформить карту"
    "\n\n Личный кабинет"
    "\n Интернет-банк"
)
def entry():
    print(front_page)
    user_name = input("Логин:  ")
    user_password = input("Пароль:  ")

    if user_name == 'admin' or user_password == 'admin':
        home()

        question = input('Хотите воспользоваться простым поиском?'
                         'да или нет:  ')

        if question.lower() == 'да':
            services_search()

        question_2 = input('Может бы хотите посмотреть траты по категориям?  ')

        if question_2.lower() == 'да':
            print(reports())

    else:
        print("Неверный логин или пароль")
