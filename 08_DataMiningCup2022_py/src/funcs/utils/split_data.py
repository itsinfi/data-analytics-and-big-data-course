from pandas import get_dummies, DataFrame
from sklearn.model_selection import train_test_split

def split_data(joined_csv: DataFrame, label_name: str, test_size: float) -> tuple[any]:
    # split dependent and independent variables
    x = get_dummies(joined_csv.drop([label_name], axis=1))
    y = joined_csv[label_name].apply(lambda x: 1 if int(x) > 3000 else 0)

    x.head()
    y.head()

    # split training and testing data
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=test_size)
    print('x_train:', x_train)
    print('y_train:', y_train)
    print('x_test:', x_test)
    print('y_test:', y_test)
    print(type(x_train))
    return x_train, x_test, y_train, y_test