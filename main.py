from src.masks import get_mask_card_number, get_mask_account

if __name__ == "__main__":
    input_card_number = 1234567891234568
    input_account_number = 12345678912345685748

    print(get_mask_card_number(input_card_number))
    print(get_mask_account(input_account_number))
