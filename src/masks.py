def get_mask_card_number(card_number: int) -> str:
    """
    :param card_number: Принимает номер карты.
    :return: Возвращает маску номера карты.
    """
    card_number_str = str(card_number)
    if card_number is None or len(card_number_str) != 16:
        raise ValueError('Неверный номер карты')
    masked_nums_list = [i for i in range(6, 12)]
    mask = ""
    for i in range(len(card_number_str)):
        if i != 0 and i % 4 == 0:
            mask += " "
        if i in masked_nums_list:
            mask += "*"
        else:
            mask += card_number_str[i]
    return mask



def get_mask_account(account_number: int) -> str:
    """
    :param account_number: Принимает номер счёта.
    :return: Возвращает маску номера счёта.
    """
    if account_number is None or len(str(account_number)) != 20:
        raise ValueError('Неверный номер счета')
    account_number_str = str(account_number)
    return "**" + account_number_str[-4:]
