from src import read_data;
from src import prepare_data;
from datetime import datetime;

# Global Parameters
cat_hierarchy_file: str = 'data/category_hierarchy.csv';
items_file: str = 'data/items.csv';
orders_file: str = 'data/orders.csv';
submissions_file: str = 'data/submission.csv';
delimiter: str = '|';
eol: str = '\n';
limit: int = 5000;
keys_to_include: list[str] = [
    'itemID',
    'userID',
    'date',
    'category',
    'parent_category',
    'feature_1',
    'feature_2',
    'feature_3',
    'feature_4',
    'feature_5',
];
typecasts: dict[str, type] = {
    'itemID': int,
    'userID': int,
    'date': datetime,
    'category': int,
    'parent_cat': int,
    'feature_1': int,
    'feature_2': int,
    'feature_3': int,
    'feature_4': int,
    'feature_5': int,
};
date_format: str = '%Y-%m-%d';


# Read data
print('--- Start reading data...');
joined_list: list[dict[str, str]] = read_data(
    cat_hierarchy_file=cat_hierarchy_file, 
    items_file=items_file,
    orders_file=orders_file, 
    submissions_file=submissions_file,
    delimiter=delimiter, 
    eol=eol, 
    limit=limit,
);
print('--- Finish reading data...');


# Prepare data
print('--- Start preparing data...');
prepared_data: list[dict[str, any]] = prepare_data(
    data=joined_list,
    keys_to_include=keys_to_include,
    typecasts=typecasts,
    date_format=date_format,
);
print('--- Finish preparing data... ---');


# TODO: continue

