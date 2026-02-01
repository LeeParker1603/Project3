from src.widget import mask_account_card, get_date

if __name__ == "__main__":
    input_info = "Visa Classic 6831982476737658"
    #input_info = "счет 56456831982476737658"
    input_date = "2024-03-11T02:26:18.671407"

    print(mask_account_card(input_info))
    print(get_date(input_date))
