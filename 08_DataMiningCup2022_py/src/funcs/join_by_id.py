from typing import List, Dict

def join_by_id(id_name: str, list1: List[Dict[str, str]], list2: List[Dict[str, str]]) -> List[Dict[str, str]]:
    merged_list = []
    for element1 in list1:
        for element2 in list2:
            if element1[id_name] == element2[id_name]:
                merged_dict = {**element1, **element2}
                merged_list.append(merged_dict)
                break
    return merged_list