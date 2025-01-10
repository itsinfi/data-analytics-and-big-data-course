from datetime import datetime;

def typecast_data(data: list[dict[str, str]], typecasts: dict[str, type], date_format: str) -> list[dict[str, any]]:
    new_list: list[dict[str, any]] = [];
    
    for element in data:
        new_dict: dict[str, any] = {};
        for key in typecasts.keys():
            if key in element.keys():
                if typecasts[key] == int:
                    new_dict[key] = int(element[key]);
                elif typecasts[key] == datetime:
                    new_dict[key] = datetime.strptime(element[key], date_format);
                    # TODO: add other types
        new_list.append(new_dict);

    return new_list;
