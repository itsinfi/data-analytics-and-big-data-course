from .funcs.filter_data import filter_data
from .funcs.label_data import label_data
from numpy import ndarray
from random import shuffle
from typing import List, Dict, Tuple

def prepare_data(data: List[Dict[str, str]], filter: Dict[str, type], date_format: str, label_name: str) -> Tuple[ndarray[ndarray[int]], ndarray[int]]:

    print('     --- Start filtering & typecasting data')
    filtered_data = filter_data(data=data, filter=filter, date_format=date_format)
    print('     --- Finish filtering & typecasting data')

    print('     --- Start shuffling data')
    shuffle(filtered_data)
    print('     --- Finish shuffling data')

    print('     --- Start labelizing data')
    data_array, label_array = label_data(data=filtered_data, label_name=label_name)
    print('     --- Finish labelizing data')
    
    return data_array, label_array