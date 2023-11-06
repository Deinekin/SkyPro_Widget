def get_list_by_key(input_list: list[dict], key: str = "EXECUTED") -> list[dict]:
    """
    принимает на вход список словарей и значение для ключа state
    и возвращает новый список, содержащий только те словари, у которых ключ
    state содержит переданное в функцию значение
    :param input_list: список словарей
    :param key: значение для ключа state, по умолчанию == EXECUTED
    :return: список словарей по значению ключа state
    """
    new_list: list[dict] = []
    for element in input_list:
        if element['state'] == key:
            new_list.append(element)
    return new_list


def sort_by_date(input_list: list[dict], by_raise: bool = True) -> list[dict]:
    """
    принимает на вход список словарей и возвращает новый список, в котором исходные словари отсортированы
    по убыванию даты
    :param input_list: список словарей
    :param by_raise: сортируем по убыванию или по возрастанию, True = по убыванию
    :return: отсортированный по дате список словарей
    """
    return sorted(input_list, key=lambda element: element['date'], reverse=by_raise)
