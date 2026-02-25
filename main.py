# from typing import Any
# from src.decorators import log
# from src.processing import filter_by_state, sort_by_date
# from src.utils import get_transactions_from_json
# # from src.widget import get_date, mask_account_card
# from src.external_api import currency_conversion


if __name__ == "__main__":
    pass
    # file_json = 'data/operations.json'
    # transaction_data = get_transactions_from_json(file_json)
    # print(currency_conversion(transaction_data[2]))

    # print(type(get_transactions_from_json(file_json)))
    # input_info = "Visa Classic 6831982476737658"
    # # input_info = "счет 56456831982476737658"
    # input_date = "2024-03-11T02:26:18.671407"
    #
    # print(mask_account_card(input_info))
    # print(get_date(input_date))
    #
    # user_info = [
    #     {
    #         "id": 41428829,
    #         "state": "EXECUTED",
    #         "date": "2019-07-03T18:35:29.512364",
    #     },
    #     {
    #         "id": 939719570,
    #         "state": "EXECUTED",
    #         "date": "2018-06-30T02:08:58.425572",
    #     },
    #     {
    #         "id": 594226727,
    #         "state": "CANCELED",
    #         "date": "2018-09-12T21:27:25.241689",
    #     },
    #     {
    #         "id": 615064591,
    #         "state": "CANCELED",
    #         "date": "2018-10-14T08:21:33.419441",
    #     },
    # ]
    #
    # date_info = [
    #     {
    #         "id": 41428829,
    #         "state": "EXECUTED",
    #         "date": "2019-07-03T18:35:29.512364",
    #     },
    #     {
    #         "id": 615064591,
    #         "state": "CANCELED",
    #         "date": "2018-10-14T08:21:33.419441",
    #     },
    #     {
    #         "id": 594226727,
    #         "state": "CANCELED",
    #         "date": "2018-09-12T21:27:25.241689",
    #     },
    #     {
    #         "id": 939719570,
    #         "state": "EXECUTED",
    #         "date": "2018-06-30T02:08:58.425572",
    #     },
    # ]
    #
    # print(filter_by_state(user_info))
    # print(sort_by_date(date_info))
    #
    # @log(filename=None)
    # def log_testing_main(x: int, y: int) -> Any:
    #     return x / y
    #
    # log_testing_main(1, 1)
    # print(log_testing_main(1, 0))
