import src.locate_files as locate_files
def list_of_stocks():
    file_path = locate_files.list_of_stocks()
    with open(file_path, 'r') as f:
        stock_symbols = [line.strip() for line in f]
        return stock_symbols