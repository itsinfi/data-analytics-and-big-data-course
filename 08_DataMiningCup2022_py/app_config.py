from datetime import datetime
from src.classes import ModelConfig
from tensorflow.keras import layers

# Global Parameters
CAT_HIERARCHY_CSV = 'data/category_hierarchy.csv'
ITEMS_CSV = 'data/items.csv'
ORDERS_CSV = 'data/orders.csv'
SUBMISSIONS_CSV = 'data/submission.csv'
CSV_DELIMITER = '|'
CSV_EOL = '\n'
CSV_LIMIT = 4000
DATE_FORMAT = '%Y-%m-%d'
LABEL_VARIABLE_NAME = 'parent_category'
DATA_FILTER = {
    'itemID': int,
    'userID': int,
    'date': datetime,
    'category': int,
    'parent_category': int,
    'feature_1': int,
    'feature_2': int,
    'feature_3': int,
    'feature_4': int,
    'feature_5': int,
}
MODEL_CFG = ModelConfig(
    model_settings=[
        layers.Dense(units=8, activation='relu', input_dim=15), # TODO:
        layers.Dense(units=16, activation='relu'),
        layers.Dense(units=1, activation='sigmoid'),

        # layers.Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)),
        # layers.MaxPooling2D((2, 2)),
        # layers.Conv2D(64, (3, 3), activation='relu'),
        # layers.MaxPooling2D((2, 2)),
        # layers.Flatten(),
        # layers.Dense(64, activation='relu'),
        # layers.Dense(10, activation='softmax')  
    ],
    train_test_ratio=0.8,
    training_epochs=10,
    training_batch_size=32,
    compiler_optimizer='sgd',
    compiler_loss='binary_crossentropy',
    compiler_metrics='accuracy',
)