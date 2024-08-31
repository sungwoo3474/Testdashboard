# data_loader.py
import pandas as pd
def load_data() :
    df = pd.read_csv("C:/worktest/Testdashboard/stock_data.csv")
    return df