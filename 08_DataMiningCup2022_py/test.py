from test_config import *
from pandas import read_csv, get_dummies
from sklearn.model_selection import train_test_split
from tensorflow.keras.models import Sequential#, load_model TODO:

csv = read_csv(CSV_FILE, delimiter=DELIMITER)

x = get_dummies(csv.drop(CSV_FILTER, axis=CSV_FILTER_AXIS))
y = csv['parent_category'].apply(lambda x: 1 if int(x) > 3000 else 0)

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=TEST_SIZE)

x_train.head()
y_train.head()

model = Sequential(
    MODEL_CFG
)

model.compile(
    loss=COMPILER_CFG['LOSS'],
    optimizer=COMPILER_CFG['OPTIMIZER'],
    metrics=COMPILER_CFG['METRICS'],
)

model.fit(
    x_train,
    y_train,
    epochs=TRAINING_CFG['EPOCHS'],
    batch_size=TRAINING_CFG['BATCH_SIZE'],
)

loss, accuracy = model.evaluate(x_test, y_test)
if 'accuracy' in COMPILER_CFG['METRICS']:
    print('--- Accuracy:', accuracy)
print('--- Loss:', loss)


y_hat = [0 if val < 0.5 else 1 for val in model.predict(x_test)]
print(y_hat)