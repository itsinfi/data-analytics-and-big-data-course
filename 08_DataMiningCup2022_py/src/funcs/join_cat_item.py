import ast
from typing import List, Dict

def join_cat_item(items: List[Dict[str, str]], cat_hierarchy: List[Dict[str, str]]) -> List[Dict[str, str]]:
    item_cat_join = []
    for item in items:
        if item['categories']:
            cat_ids: List[int] = ast.literal_eval(item['categories'])
            for cat_id in cat_ids:
                for cat in cat_hierarchy:
                    parent_id = int(cat['category'])
                    if cat_id == parent_id:
                        merged_dict = {**item, **cat}
                        item_cat_join.append(merged_dict)
                        break
    return item_cat_join