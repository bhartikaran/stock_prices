import os

current_dir = os.path.dirname(os.path.abspath(__file__))
def list_of_stocks():
    return os.path.join(current_dir,"..", "data",'list_of_stocks.txt')

def pickle_file():
    return os.path.join(current_dir, "..", "data", 'token_pickle')