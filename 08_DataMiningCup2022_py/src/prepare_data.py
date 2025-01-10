from .utils.filter_keys import filter_keys;
from .utils.typecast_data import typecast_data;

def prepare_data(data: list[dict[str, str]], keys_to_include: list[str], typecasts: dict[str, type], date_format: str) -> list[dict[str, any]]:

    print(f'        --- Start filtering data by these attributes: {keys_to_include}');
    filtered_data: list[dict[str, str]] = filter_keys(data=data, keys_to_include=keys_to_include);
    print(f'        --- Finish filtering data: {filtered_data}');

    print('        --- Start typecasting data');
    typecasted_data: list[dict[str, str]] = typecast_data(data=filtered_data, typecasts=typecasts, date_format=date_format);
    print(f'        --- Finish typecasting data: {typecasted_data}'); 
    
    return typecasted_data;