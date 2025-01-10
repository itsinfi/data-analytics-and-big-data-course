from datetime import datetime

def filter_data(data: list[dict[str, str]], filter: dict[str, type], date_format: str) -> list[dict[str, int]]:
    new_list = []
    
    for element in data:
        new_dict = {}
        
        for key in filter.keys():
            if key in element.keys():
                
                if filter[key] == int:
                    new_dict[key] = int(element[key])
                
                elif filter[key] == datetime:
                    date = datetime.strptime(element[key], date_format)
                    new_dict[key + '_year'] = date.year
                    new_dict[key + '_month'] = date.month
                    new_dict[key + '_day'] = date.day
                
                # TODO: add other types
        
        new_list.append(new_dict)

    return new_list
