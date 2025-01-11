from pandas import read_csv, get_dummies
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from tensorflow.keras.models import Sequential, load_model
from tensorflow.keras.layers import Dense

csv = read_csv('data/category_hierarchy.csv', delimiter='|')

x = get_dummies(csv.drop(['parent_category'], axis=1))
y = csv['parent_category'].apply(lambda x: 1 if int(x) > 3000 else 0)

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=.2)

x_train.head()
y_train.head()

model = Sequential([
    Dense(units=32, activation='relu', input_dim=len(x_train.columns)),
    Dense(units=64, activation='relu'),
    Dense(units=1, activation='sigmoid'),
])

model.compile(
    loss='binary_crossentropy',
    optimizer='sgd',
    metrics=['accuracy'],
)

model.fit(
    x_train,
    y_train,
    epochs=200,
    batch_size=32,
)

loss, accuracy = model.evaluate(x_test, y_test)
print('--- Accuracy:', accuracy)
print('--- Loss:', loss)


y_hat = [0 if val < 0.5 else 1 for val in model.predict(x_test)]
print(y_hat)