from tensorflow.keras.layers import Dense

CSV_FILE = 'data/category_hierarchy.csv'
CSV_FILTER = ['parent_category']
CSV_FILTER_AXIS = 1
DELIMITER = '|'
TEST_SIZE = .2
MODEL_CFG = [
    Dense(units=32, activation='relu'), #input_dim=len(x_train.columns)#/),
    Dense(units=64, activation='relu'),
    Dense(units=1, activation='sigmoid'),
]
COMPILER_CFG = {
    'LOSS': 'binary_crossentropy',
    'OPTIMIZER': 'sgd',
    'METRICS': [
        'accuracy'
    ],
}
TRAINING_CFG = {
    'EPOCHS': 100,
    'BATCH_SIZE': 32,
}