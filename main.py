import src.read_list
import src.api_calls
if __name__ == '__main__':
    list_of_stocks = src.read_list.list_of_stocks()
    for stock in list_of_stocks:
        src.api_calls.query_stock_data(stock)

