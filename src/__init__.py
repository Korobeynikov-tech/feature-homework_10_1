from datetime import datetime


def get_mask_card_number(card_number: str) -> str:
    """Маскирует номер карты, оставляя видимыми первые 6 и последние 4 цифры.

    Args:
        card_number (str): Номер карты в виде строки.

    Returns:
        str: Замаскированный номер карты.
    """
    return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"


def get_mask_account(account_number: str) -> str:
    """Маскирует номер счета, оставляя видимыми только последние 4 цифры.

    Args:
        account_number (str): Номер счета в виде строки.

    Returns:
        str: Замаскированный номер счета.
    """
    return f"**{account_number[-4:]}"


# Пример использования функций:
card_num = "7000792289606361"
account_num = "73654108430135874305"

print(get_mask_card_number(card_num))  # Вывод: 7000 79** **** 6361
print(get_mask_account(account_num))   # Вывод: **4305


def get_date(date_str: str) -> str:
    """
    Преобразует строку с датой из формата "YYYY-MM-DDTHH:MM:SS.ssssss" в формат "ДД.ММ.ГГГГ".
    Args:
        date_str (str): Строка с датой в формате "YYYY-MM-DDTHH:MM:SS.ssssss".
    Returns:
        str: Строка с датой в формате "ДД.ММ.ГГГГ".
    """
    # Парсим строку с датой в объект datetime
    date_obj = datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%S.%f")
    # Преобразуем объект datetime в строку формата "ДД.ММ.ГГГГ"
    return date_obj.strftime("%d.%m.%Y")


# Примеры использования функции
print(get_date("2024-03-11T02:26:18.671407"))  # Выведет: 11.03.2024
print(get_date("2024-07-13T14:11:29.000000"))  # Выведет: 13.07.2024


def get_date(date_str: str) ->str:
    """
    Преобразует строку с датой из формата "YYYY-MM-DDTHH:MM:SS.ssssss" в формат "ДД.ММ.ГГГГ".
    Args:
        date_str (str): Строка с датой в формате "YYYY-MM-DDTHH:MM:SS.ssssss".
    Returns:
        str: Строка с датой в формате "ДД.ММ.ГГГГ".
    """
    # Парсим строку с датой в объект datetime
    date_obj = datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%S.%f")
    # Преобразуем объект datetime в строку формата "ДД.ММ.ГГГГ"
    return date_obj.strftime("%d.%m.%Y")


print(get_date("2024-03-11T02:26:18.671407"))  # Выведет: 11.03.2024
print(get_date("2024-07-13T14:11:29.000000"))  # Выведет: 13.07.2024


def filter_by_state(list_of_dicts: list, state: str ='EXECUTED'):

    """Фильтрование списка словарей по указанному состоянию.

        data:
            args: List[Dict[str, Any]] - Список словарей для фильтрации

        state:
            str: Состояние, по которому выполняется фильтрация

        return:
             List[Dict[str, Any]] - Список словарей с указанным состоянием
    """

    return [d for d in list_of_dicts if d.get('state') == state]


# Пример использования
data = [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
        {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
        {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]

filtered_list = filter_by_state(data)
print(filtered_list)


def sort_by_date(dict_list: list, reverse=True):

    """Сортировка списка словарей по дате.

        data:
            args: List[Dict[str, Any]] - Список словарей для сортировки

        return:
            args: List[Dict[str, Any]] - Список словарей, отсортированных по дате
    """

    return sorted(dict_list, key = lambda x: x.get("date"), reverse=reverse)


# Пример использования
data = [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
        {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
        {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]

sorted_data = sort_by_date(data)
print(sorted_data)
