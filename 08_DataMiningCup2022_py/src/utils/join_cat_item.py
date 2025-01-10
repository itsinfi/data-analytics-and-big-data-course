import ast

def join_cat_item(items: list[dict[str, str]], cat_hierarchy: list[dict[str, str]]) -> list[dict[str, str]]:
    item_cat_join = []
    for item in items:
        if item['categories']:
            cat_ids: list[int] = ast.literal_eval(item['categories'])
            for cat_id in cat_ids:
                for cat in cat_hierarchy:
                    parent_id = int(cat['category'])
                    if cat_id == parent_id:
                        merged_dict = {**item, **cat}
                        item_cat_join.append(merged_dict)
                        break
    return item_cat_join