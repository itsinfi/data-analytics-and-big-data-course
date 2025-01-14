from numpy import array, ndarray
from typing import List, Dict, Tuple

def label_data(data: List[Dict[str, int]], label_name: str) -> Tuple[ndarray[ndarray[int]], ndarray[int]]:
    
    data_array = []
    label_array = []
    
    for element in data:
        data_element_array = []
        
        label = element[label_name]
        element.pop(label_name)

        for value in element.values():
            data_element_array.append(value)
        
        data_array.append(array(data_element_array))
        label_array.append(array(label))
    
    return data_array, label_array
