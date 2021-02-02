import pandas as pd

# This is a demo loader
# Change back
def my_data_loader():
    dataset_csv_url = "https://raw.githubusercontent.com/adobe/acp-data-services-dsw-reference/master/datasets/retail/retail.csv"

    # Load data into a Pandas DataFrame
    df = pd.read_csv(dataset_csv_url)
    return df