from .utils.filter_data import filter_data
from .utils.label_data import label_data
from numpy import ndarray

def prepare_data(data: list[dict[str, str]], filter: dict[str, type], date_format: str, label_name: str) -> tuple[ndarray[ndarray[int]], ndarray[int]]:

    print('        --- Start filtering & typecasting data')
    typecasted_data = filter_data(data=data, filter=filter, date_format=date_format)
    print(f'        --- Finish filtering & typecasting data') 

    print('     --- Start labelizing data')
    data_array, label_array = label_data(data=typecasted_data, label_name=label_name)
    print('     --- Finish labelizing data')
    
    return data_array, label_array