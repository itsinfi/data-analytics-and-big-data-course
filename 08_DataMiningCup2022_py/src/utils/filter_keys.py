def filter_keys(data: list[dict[str, any]], keys_to_include: list[str]) -> list[dict[str, any]]:
    new_list: list[dict[str, any]] = [];

    for element in data:
        new_element: dict[str, any] = {};
        for key in keys_to_include:
            if key in element.keys():
                new_element[key] = element[key];
        new_list.append(new_element);
    
    return new_list;