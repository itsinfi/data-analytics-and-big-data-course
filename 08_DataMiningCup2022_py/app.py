from src import read_data
from src import prepare_data
from src import train_cnn
from config import *

# Read data
print('--- Start reading data...')
joined_list = read_data(
    cat_hierarchy_file=CAT_HIERARCHY_CSV, 
    items_file=ITEMS_CSV,
    orders_file=ORDERS_CSV, 
    submissions_file=SUBMISSIONS_CSV,
    delimiter=CSV_DELIMITER, 
    eol=CSV_EOL, 
    limit=CSV_LIMIT,
)
print('--- Finish reading data...')


# Prepare data
print('--- Start preparing data...')
data_array, label_array = prepare_data(
    data=joined_list,
    filter=DATA_FILTER,
    date_format=DATE_FORMAT,
    label_name=LABEL_VARIABLE_NAME,
)
print('--- Finish preparing data... ---')

# Train model TODO:
print('--- Start training neural network...')
train_cnn(
    data=data_array,
    labels=label_array,
    cfg=MODEL_CFG,
)
print('--- Finish training neural network...')


