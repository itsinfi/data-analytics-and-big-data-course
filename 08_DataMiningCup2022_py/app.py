from src import read_data
from src import prepare_data
from src import train_cnn
from datetime import datetime

# Global Parameters
cat_hierarchy_file = 'data/category_hierarchy.csv'
items_file = 'data/items.csv'
orders_file = 'data/orders.csv'
submissions_file = 'data/submission.csv'
delimiter = '|'
eol = '\n'
limit = 4000
filter = {
    'itemID': int,
    'userID': int,
    'date': datetime,
    'category': int,
    'parent_category': int,
    'feature_1': int,
    'feature_2': int,
    'feature_3': int,
    'feature_4': int,
    'feature_5': int,
}
date_format = '%Y-%m-%d'
label_name = 'parent_category'


# Read data
print('--- Start reading data...')
joined_list = read_data(
    cat_hierarchy_file=cat_hierarchy_file, 
    items_file=items_file,
    orders_file=orders_file, 
    submissions_file=submissions_file,
    delimiter=delimiter, 
    eol=eol, 
    limit=limit,
)
print('--- Finish reading data...')


# Prepare data
print('--- Start preparing data...')
prepared_data = prepare_data(
    data=joined_list,
    filter=filter,
    date_format=date_format,
    label_name=label_name
)
print('--- Finish preparing data... ---')

# Train model
print('--- Start training neural network...')
train_cnn(data=prepared_data)
print('--- Finish training neural network...')


