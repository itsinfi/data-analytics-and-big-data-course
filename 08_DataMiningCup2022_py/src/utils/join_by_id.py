def join_by_id(id_name: str, list1: list[dict[str, str]], list2: list[dict[str, str]]) -> list[dict[str, str]]:
    merged_list: list[dict[str, str]] = [];
    for element1 in list1:
        for element2 in list2:
            if element1[id_name] == element2[id_name]:
                merged_dict: dict[str, str] = {**element1, **element2};
                merged_list.append(merged_dict);
                break;
    return merged_list;