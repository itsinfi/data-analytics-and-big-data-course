from .utils.read_csv import read_csv;
from .utils.join_by_id import join_by_id;
from .utils.join_cat_item import join_cat_item;

id_name: str = 'itemID';

def read_data(cat_hierarchy_file: str, items_file: str, orders_file: str, submissions_file: str, delimiter: str, eol: str, limit: int) -> list[dict[str, str]]:
    # Read csv
    cat_hierarchy: list[dict[str, str]] = read_csv(csv_file=cat_hierarchy_file, delimiter=delimiter, eol=eol, limit=limit);
    items: list[dict[str, str]] = read_csv(csv_file=items_file, delimiter=delimiter, eol=eol, limit=limit);
    orders: list[dict[str, str]] = read_csv(csv_file=orders_file, delimiter=delimiter, eol=eol, limit=limit);
    submissions: list[dict[str, str]] = read_csv(csv_file=submissions_file, delimiter=delimiter, eol=eol, limit=limit);
    
    # Join lists
    print(f'     --- Start joining data...');
    cat_item_join: list[dict[str, str]] = join_cat_item(items=items, cat_hierarchy=cat_hierarchy);
    submission_order_join: list[dict[str, str]] = join_by_id(id_name=id_name, list1=submissions, list2=orders);
    result: list[dict[str, str]] = join_by_id(id_name=id_name, list1=cat_item_join, list2=submission_order_join);
    print(f'     --- Data: f{result}...');
    print(f'     --- Finish joining data...');
    return result;